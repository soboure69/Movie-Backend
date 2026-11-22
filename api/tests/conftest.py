"""Configuration des tests : l'API est testée sur la base movies.db du dépôt, sans serveur."""
import os
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

API_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(API_DIR))
os.chdir(API_DIR)  # database.py ouvre "sqlite:///./movies.db", relatif au dossier courant

from main import app  # noqa: E402


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c
