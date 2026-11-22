"""Tests du SDK : nouvelles tentatives (backoff) et appels de bout en bout contre l'API du dépôt."""
import sys
from pathlib import Path

import httpx
import pytest

from films_sdk_sbre import MovieClient, MovieConfig

URL = "https://api.exemple.test"


@pytest.fixture(autouse=True)
def sans_attente(monkeypatch):
    """Les délais entre tentatives sont supprimés pour que les tests restent rapides."""
    monkeypatch.setattr("backoff._sync.time.sleep", lambda secondes: None)


def faux_serveur(monkeypatch, reponses):
    """Remplace httpx.get : renvoie les réponses dans l'ordre et compte les appels."""
    appels = []

    def get(url, params=None):
        appels.append(url)
        r = reponses[min(len(appels), len(reponses)) - 1]
        if isinstance(r, Exception):
            raise r
        statut, contenu = r
        return httpx.Response(statut, json=contenu, request=httpx.Request("GET", url))

    monkeypatch.setattr(httpx, "get", get)
    return appels


def test_reessaie_apres_des_erreurs_503(monkeypatch):
    appels = faux_serveur(monkeypatch, [(503, {}), (503, {}), (200, {"message": "ok"})])
    assert MovieClient(MovieConfig(URL)).health_check() == {"message": "ok"}
    assert len(appels) == 3


def test_reessaie_apres_une_erreur_reseau(monkeypatch):
    appels = faux_serveur(monkeypatch, [httpx.ConnectError("refusé"), (200, {"message": "ok"})])
    assert MovieClient(MovieConfig(URL)).health_check() == {"message": "ok"}
    assert len(appels) == 2


def test_ne_reessaie_pas_une_erreur_404(monkeypatch):
    appels = faux_serveur(monkeypatch, [(404, {"detail": "absent"})])
    with pytest.raises(httpx.HTTPStatusError):
        MovieClient(MovieConfig(URL)).get_movie(999)
    assert len(appels) == 1


def test_reessaie_une_erreur_429(monkeypatch):
    appels = faux_serveur(monkeypatch, [(429, {}), (200, {"message": "ok"})])
    MovieClient(MovieConfig(URL)).health_check()
    assert len(appels) == 2


def test_sans_backoff_une_seule_tentative(monkeypatch):
    appels = faux_serveur(monkeypatch, [(503, {})])
    with pytest.raises(httpx.HTTPStatusError):
        MovieClient(MovieConfig(URL, backoff=False)).health_check()
    assert len(appels) == 1


def test_abandonne_apres_le_delai_maximal(monkeypatch):
    appels = faux_serveur(monkeypatch, [(503, {})])
    with pytest.raises(httpx.HTTPStatusError):
        MovieClient(MovieConfig(URL, backoff_max_time=0)).health_check()
    assert len(appels) == 1


# --- De bout en bout : le SDK interroge l'API du dépôt, exécutée sans serveur ---

API_DIR = Path(__file__).resolve().parents[2] / "api"


@pytest.fixture
def client_sur_api_locale(monkeypatch):
    pytest.importorskip("fastapi")
    pytest.importorskip("sqlalchemy")
    from fastapi.testclient import TestClient

    monkeypatch.chdir(API_DIR)
    monkeypatch.syspath_prepend(str(API_DIR))
    from main import app

    api = TestClient(app)
    monkeypatch.setattr(httpx, "get", lambda url, params=None: api.get(url.replace(URL, ""), params=params))
    return MovieClient(MovieConfig(URL))


def test_sdk_contre_api_film_et_liste(client_sur_api_locale):
    c = client_sur_api_locale
    assert c.get_movie(1).title == "Toy Story (1995)"
    df = c.list_movies(genre="Comedy", limit=50, output_format="pandas")
    assert len(df) == 50 and df["genres"].str.contains("Comedy").all()


def test_sdk_contre_api_lien_sans_tmdb(client_sur_api_locale):
    assert client_sur_api_locale.get_link(791).tmdbId is None


def test_sdk_contre_api_statistiques(client_sur_api_locale):
    stats = client_sur_api_locale.get_analytics()
    assert (stats.movie_count, stats.rating_count) == (9742, 100836)
