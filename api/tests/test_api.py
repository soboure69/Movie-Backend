"""Tests de l'API MovieLens : contrats des points d'accès, filtres, pagination et erreurs."""
import pytest


def test_etat_de_l_api(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "API MovieLens opérationnelle"}


def test_analytics_correspond_au_jeu_ml_latest_small(client):
    assert client.get("/analytics").json() == {
        "movie_count": 9742, "rating_count": 100836, "tag_count": 3683, "link_count": 9742,
    }


# --- Films ---

def test_film_par_id_avec_notes_et_tags(client):
    film = client.get("/movies/1").json()
    assert film["title"] == "Toy Story (1995)"
    assert "Animation" in film["genres"]
    assert any(n["userId"] == 1 and n["rating"] == 4.0 for n in film["ratings"])


def test_film_inexistant_renvoie_404(client):
    r = client.get("/movies/999999999")
    assert r.status_code == 404
    assert "999999999" in r.json()["detail"]


def test_liste_des_films_pagination_par_defaut_et_skip(client):
    page1 = client.get("/movies").json()
    assert len(page1) == 100
    page2 = client.get("/movies", params={"skip": 100, "limit": 100}).json()
    assert {f["movieId"] for f in page1}.isdisjoint({f["movieId"] for f in page2})


def test_filtre_par_genre(client):
    films = client.get("/movies", params={"genre": "Documentary", "limit": 1000}).json()
    assert films and all("Documentary" in f["genres"] for f in films)


def test_filtre_par_titre(client):
    films = client.get("/movies", params={"title": "Toy Story"}).json()
    assert films and all("Toy Story" in f["title"] for f in films)


@pytest.mark.parametrize("route", ["/movies", "/ratings", "/tags", "/links"])
def test_limite_superieure_a_1000_refusee(client, route):
    assert client.get(route, params={"limit": 1001}).status_code == 422


@pytest.mark.parametrize("route", ["/movies", "/ratings", "/tags", "/links"])
def test_skip_negatif_refuse(client, route):
    assert client.get(route, params={"skip": -1}).status_code == 422


@pytest.mark.parametrize("route", ["/movies", "/ratings", "/tags", "/links"])
def test_limite_negative_ne_contourne_pas_le_plafond(client, route):
    r = client.get(route, params={"limit": -1})
    assert r.status_code == 422


# --- Notes ---

def test_note_par_utilisateur_et_film(client):
    assert client.get("/ratings/1/1").json()["rating"] == 4.0


def test_note_inexistante_renvoie_404(client):
    assert client.get("/ratings/1/999999999").status_code == 404


def test_filtres_des_notes(client):
    notes = client.get("/ratings", params={"movie_id": 1, "min_rating": 4.5, "limit": 1000}).json()
    assert notes and all(n["movieId"] == 1 and n["rating"] >= 4.5 for n in notes)


def test_note_minimale_hors_bornes_refusee(client):
    assert client.get("/ratings", params={"min_rating": 6}).status_code == 422


# --- Tags ---

def test_tag_exact(client):
    tag = client.get("/tags/2/60756/funny").json()
    assert (tag["userId"], tag["movieId"], tag["tag"]) == (2, 60756, "funny")


def test_tag_inexistant_renvoie_404(client):
    assert client.get("/tags/2/60756/inexistant").status_code == 404


def test_filtre_des_tags_par_utilisateur(client):
    tags = client.get("/tags", params={"user_id": 2, "limit": 1000}).json()
    assert tags and all(t["userId"] == 2 for t in tags)


# --- Liens ---

def test_lien_imdb_et_tmdb(client):
    lien = client.get("/links/1").json()
    assert str(lien["imdbId"]).lstrip("0") == "114709"
    assert int(lien["tmdbId"]) == 862


def test_lien_inexistant_renvoie_404(client):
    assert client.get("/links/999999999").status_code == 404


# --- Films sans identifiant TMDb (8 dans le jeu, dont le film 791) ---

def test_lien_sans_tmdb_renvoie_none(client):
    lien = client.get("/links/791")
    assert lien.status_code == 200
    assert lien.json()["tmdbId"] is None


def test_page_de_liens_contenant_un_film_sans_tmdb(client):
    assert client.get("/links", params={"skip": 600, "limit": 100}).status_code == 200


def test_film_sans_tmdb(client):
    assert client.get("/movies/791").status_code == 200
