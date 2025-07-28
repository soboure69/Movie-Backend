# Movie-Backend
Phase 1 du Projet CinéData

# Mission : **Construire un Écosystème Data Centré sur le Cinéma avec Python, FastAPI et Streamlit** 

**Contexte : Plongez dans l’univers du cinéma et de la Data Science**  

Une entreprise fictive, **CineData Insights** souhaite révolutionner l'expérience cinéphile grâce à une plateforme intelligente exploitant les données de films. Leur ambition : **Créer un système ultra-performant d'analyse de leurs données** à destination des plateformes de streaming, des cinéphiles et des studios de production.  

Mais il y a un problème... **Leurs données sont dans un état chaotique !** 
Elles sont éparpillées dans quelques fichiers CSV, rendant toute exploitation fastidieuse. Aucun système centralisé ne permet de requêter efficacement les informations sur les films, les notes attribuées par les utilisateurs ou encore les tags associés.  

C'est là que j'interviens en tant que **Consultant Data polyvalent / Ingénieur Data** ! Ma mission: Transformer ce chaos en un écosystème data performant et interactif. Je suis **le chef d’orchestre** de ce projet, portant successivement trois casquettes :  

---

## **Phase 1 : Développeur Python & Architecte API**  

![](architecture.png)

**Objectif : Construire une API robuste pour centraliser et exposer les données MovieLens.**  

🔹 **Design de la base de données** :  
- Modéliser la base de données en SQL à partir des fichiers CSV.  
- Utiliser **SQLite** pour stocker les données de manière efficace.  
- Gérer les relations entre les films, les utilisateurs, les notes et les tags.  

🔹 **Développement de l’API avec FastAPI** :  
- Concevoir un **API RESTful** permettant d'interroger facilement les films et les notes des utilisateurs.  
- Intégrer **Pydantic** pour la validation des données entrantes.  
- Utiliser **SQLAlchemy** pour la gestion des requêtes à la base de données.  

🔹 **Déploiement de l’API** :  
- Héberger l’API sur un cloud public (**Render, AWS, Azure, GCP**).  
- Prévoir une version **on-premise** avec Docker.  
- Sécuriser les endpoints et optimiser les performances.  

🔹 **Création d’un SDK en Python** :  
- Développer un **package Python** permettant aux utilisateurs d'interagir facilement avec l’API.  
- Publier ce package sur **PyPI**, afin qu’il puisse être utilisé dans d'autres projets.  

**Livrables** :  
- Une base de données centralisée et prête à l’emploi.  
- Une API FastAPI documentée et déployée.  
- Un SDK Python simple d'utilisation et bien documenté

---

## **Phase 2 : Data Analyst - Exploration et Visualisation**  

![](architecturephase.png)

**Objectif : Explorer et analyser les données en interrogeant l’API.**  

🔹 **Analyse Exploratoire des Données (EDA)** :  
- Utiliser le **SDK Python** pour requêter l’API et récupérer les données.  
- Identifier les tendances dans les notes des films.  
- Étudier les genres les plus populaires et les préférences des utilisateurs.  

🔹 **Construction d’une Data App avec Streamlit** :  
- Créer une **application interactive** qui permet de visualiser les tendances du cinéma.  
- Intégrer des **tableaux dynamiques** et des **graphiques interactifs**.  
- Offrir une **recherche avancée** des films en fonction des notes et des genres.  

**Livrables** :  
- Un notebook d'analyse exploratoire interactif.  
- Une **application web Streamlit** connectée à l’API qui présente, de manière interactive, les insights aux parties prenantes.

---

## **Pourquoi cette mission est incontournable pour tout Consultant Data / Ingénieur Data ?**  

- **Expérience complète et immersive** : On touche **à toutes les facettes** d’un projet Data moderne.  
- **Projet concret et impactant** : Qui n’a jamais rêvé d’un système intelligent pour découvrir les meilleurs films ?  
- **Compétences ultra-prisées** : manipuler **FastAPI, SQLAlchemy, Streamlit, Machine Learning, Cloud, et Docker**.  
 


---


# Dataset MovieLens - Description des Données

Le dataset MovieLens est un ensemble de données publiques fournies par GroupLens, contenant des informations sur des films, des évaluations d'utilisateurs, ainsi que des tags attribués aux films. Il est souvent utilisé pour la recherche et l'expérimentation dans le domaine des systèmes de recommandation.

## Fichiers et Structure des Données

### 1. movies.csv
Contient la liste des films avec leur identifiant unique, leur titre et leurs genres.

**Colonnes :**
- `movieId` : Identifiant unique du film (clé primaire).
- `title` : Titre du film, incluant l'année de sortie entre parenthèses.
- `genres` : Liste des genres associés au film, séparés par "|".

**Exemple :**
```
movieId,title,genres
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
2,Jumanji (1995),Adventure|Children|Fantasy
```

---

### 2. ratings.csv
Contient les évaluations des films par les utilisateurs.

**Colonnes :**
- `userId` : Identifiant unique de l'utilisateur (clé primaire avec `movieId`).
- `movieId` : Identifiant du film évalué (clé étrangère vers `movies.movieId`).
- `rating` : Note attribuée au film par l'utilisateur (de 0.5 à 5.0, par incréments de 0.5).
- `timestamp` : Horodatage de l'évaluation.

**Exemple :**
```
userId,movieId,rating,timestamp
1,1,4.0,964982703
2,1,4.5,847434962
```

---

### 3. tags.csv
Contient des tags attribués aux films par les utilisateurs.

**Colonnes :**
- `userId` : Identifiant unique de l'utilisateur.
- `movieId` : Identifiant du film concerné (clé étrangère vers `movies.movieId`).
- `tag` : Tag textuel associé au film.
- `timestamp` : Horodatage de l'ajout du tag.

**Exemple :**
```
userId,movieId,tag,timestamp
15,339,atmospheric,1138537770
```

---

### 4. links.csv
Contient les identifiants externes des films dans d'autres bases de données (IMDB et TMDb).

**Colonnes :**
- `movieId` : Identifiant du film (clé primaire, référence `movies.movieId`).
- `imdbId` : Identifiant IMDB du film.
- `tmdbId` : Identifiant TMDb (The Movie Database) du film.

**Exemple :**
```
movieId,imdbId,tmdbId
1,0114709,862
2,0113497,8844
```

---

## Structure de la Base de Données SQLite3

Pour stocker ces données dans une base SQLite3, on définit la structure suivante :

### Table `movies`
```sql
CREATE TABLE movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genres TEXT
);
```

### Table `ratings`
```sql
CREATE TABLE ratings (
    userId INTEGER,
    movieId INTEGER,
    rating REAL CHECK(rating >= 0.5 AND rating <= 5.0),
    timestamp INTEGER,
    PRIMARY KEY (userId, movieId),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

### Table `tags`
```sql
CREATE TABLE tags (
    userId INTEGER,
    movieId INTEGER,
    tag TEXT,
    timestamp INTEGER,
    PRIMARY KEY (userId, movieId, tag),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

### Table `links`
```sql
CREATE TABLE links (
    movieId INTEGER PRIMARY KEY,
    imdbId TEXT,
    tmdbId INTEGER,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

## Relations entre les Tables
- `ratings.movieId`, `tags.movieId`, et `links.movieId` sont des clés étrangères référencées depuis `movies.movieId`.
- Les tables `ratings` et `tags` utilisent `userId` et `movieId` comme clé primaire composite.

Cette structure permet d'assurer l'intégrité des données tout en facilitant les analyses et la recommandation de films.

# Création de la Base de Données SQLite3 et de ses tables

```bash
(.venv) bello@Bello_Sbre_PC:~/Documents/Movie-backend$ sqlite3 movies.db
```

```sql
CREATE TABLE movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genres TEXT
);
```

```sql
CREATE TABLE ratings (
    userId INTEGER,
    movieId INTEGER,
    rating REAL CHECK(rating >= 0.5 AND rating <= 5.0),
    timestamp INTEGER,
    PRIMARY KEY (userId, movieId),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

```sql
CREATE TABLE tags (
    userId INTEGER,
    movieId INTEGER,
    tag TEXT,
    timestamp INTEGER,
    PRIMARY KEY (userId, movieId, tag),
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

```sql
CREATE TABLE links (
    movieId INTEGER PRIMARY KEY,
    imdbId TEXT,
    tmdbId INTEGER,
    FOREIGN KEY (movieId) REFERENCES movies(movieId)
);
```

# Chargement des Données dans les Tables SQLite3

## Activation des clés étrangères

```sql
PRAGMA foreign_keys = ON;
```

La commande **`PRAGMA foreign_keys = ON;`** dans SQLite sert à **activer les clés étrangères**.  Cela garantit que toutes les contraintes de clés étrangères seront respectées.

### **Explication** :

- SQLite **ne vérifie pas** les contraintes de clé étrangère par défaut.
- Cette commande **active** l'intégrité référentielle, ce qui signifie que :
  - Une valeur de clé étrangère doit correspondre à une clé primaire existante.
  - Si une ligne référencée est supprimée ou modifiée, cela peut entraîner une erreur ou déclencher une action définie (ex: `ON DELETE CASCADE`).

### **Bonnes pratiques** :

- Toujours activer les clés étrangères en début de session SQLite :
  ```sql
  PRAGMA foreign_keys = ON;
  ```
- Pour vérifier si les clés étrangères sont activées :
  ```sql
  PRAGMA foreign_keys;
  ```
  - Retourne `1` si activé, `0` sinon.


## Préparez l'instruction d'importation pour reconnaître le format CSV avec la commande suivante :

```sql
.mode csv
```

## Chargement des données des fichiers csv dans les tables

### Chargement

```sql
.import --skip 1 data/movies.csv movies
```

```sql
.import --skip 1 data/ratings.csv ratings
```

```sql
.import --skip 1 data/tags.csv tags
```

```sql
.import --skip 1 data/links.csv links
```

### **Vérifier que les données ont été chargées** :

```sql
SELECT * FROM movies LIMIT 5;
```

```
1,"Toy Story (1995)",Adventure|Animation|Children|Comedy|Fantasy
2,"Jumanji (1995)",Adventure|Children|Fantasy
3,"Grumpier Old Men (1995)",Comedy|Romance
4,"Waiting to Exhale (1995)",Comedy|Drama|Romance
5,"Father of the Bride Part II (1995)",Comedy
```

```sql
SELECT COUNT(*) FROM movies;
```

```
9742
```

```sql
SELECT * FROM ratings LIMIT 5;
```

```
1,1,4.0,964982703
1,3,4.0,964981247
1,6,4.0,964982224
1,47,5.0,964983815
1,50,5.0,964982931
```

```sql
SELECT COUNT(*) FROM ratings;
```

```
100836
```

```sql
SELECT * FROM tags LIMIT 5;
```

```
2,60756,funny,1445714994
2,60756,"Highly quotable",1445714996
2,60756,"will ferrell",1445714992
2,89774,"Boxing story",1445715207
2,89774,MMA,1445715200
```

```sql
SELECT COUNT(*) FROM tags;
```

```
3683
```

```sql
sqlite> SELECT * FROM links LIMIT 5;
```

```
1,0114709,862
2,0113497,8844
3,0113228,15602
4,0114885,31357
5,0113041,11862
```

```sql
SELECT COUNT(*) FROM links;
```

```
9742
```

Pour quitter l'interface en lignes de commandes de SQLite, cette commande :

```sql
.exit
```

# Phase 1 : Développeur Python & Architecte API

## Introduction

![](architecture.png)


### Explication du diagramme

Une API (Application Programming Interface) est une interface qui permet à des applications ou des utilisateurs d'interagir avec un système. Ce diagramme représente comment une API fonctionne pour gérer des données et interagir avec une base de données.

#### Étape par étape :

1. **Les utilisateurs de l'API** (`API Users`)  
   - Ce sont les personnes ou applications qui utilisent l'API pour envoyer ou récupérer des données.
   - Pour interagir avec l'API, ils utilisent un **SDK** (Software Development Kit), qui est une bibliothèque (un package) Python facilitant l'envoi de requêtes.

2. **Le transfert et la validation des données** (`Pydantic`)  
   - Lorsque l'utilisateur envoie des requêtes à l'API, elles passent d'abord par **Pydantic**.  On parlera davantage de Pydantic dans une autre session.
   - Pydantic vérifie que les données sont correctes (par exemple, s'il manque une valeur ou si un type est incorrect).  

3. **Le contrôleur API** (`FastAPI`)  
   - FastAPI est le cœur de l'API. Il reçoit les requêtes des utilisateurs, traite les données et décide de ce qu'il faut faire (ex. : insérer de nouvelles données, récupérer des informations, etc.).
   - Il agit comme un intermédiaire entre l'utilisateur et la base de données.

4. **Les classes de base de données** (`SQLAlchemy`)  
   - SQLAlchemy est une bibliothèque qui permet de communiquer avec la base de données de manière organisée.
   - Il traduit les requêtes Python en instructions compréhensibles par la base de données.

5. **La base de données** (`SQLite`)  
   - SQLite est la database où se trouve les données.
   - L'API envoie des requêtes pour récupérer des données de la database SQLite.

#### En résumé :
- L'utilisateur envoie des données via l'**SDK**.
- Ces données sont **validées** (`Pydantic`).
- L'API décide quoi faire (`FastAPI`).
- Si nécessaire, elle stocke ou récupère des données via **SQLAlchemy**.
- La base de données **SQLite** garde les informations de manière structurée.

---

L'API fonctionne comme un **restaurant moderne avec une tablette pour commander** :  

1. **Le client (API Users)** arrive au restaurant et veut commander un plat.  
2. **Le menu numérique (SDK en Python)** lui permet de passer commande facilement sans parler directement au serveur. Il peut sélectionner un plat en quelques clics.  
3. **Le serveur (FastAPI)** reçoit la commande, la vérifie et la transmet en cuisine.  
4. **Le chef (SQLAlchemy)** prépare le plat en récupérant les ingrédients depuis **la réserve (SQLite, la base de données)**.  
5. Une fois le plat prêt, **le serveur revient avec la commande** et la sert au client.  

**Pourquoi le SDK est important ?**  
C’est comme une tablette qui facilite la commande : au lieu d’écrire une requête compliquée ou d’appeler directement le serveur, le client peut utiliser une interface simple et intuitive (le SDK) pour interagir avec l’API.

## Classes SQLAlchemy

### Pourquoi utiliser SQLAlchemy dans l'API ?  

Lorsqu'on crée une application qui interagit avec une base de données, comme  l'API de films, on a deux choix pour gérer les données :  

1. **Exécuter des requêtes SQL directement**  
   - établir une connexion avec SQLite.  
   - écrire des requêtes SQL brutes pour insérer, récupérer et modifier des données.  
   - gérer manuellement les types de données (convertir entre les formats SQLite et Python).  
   - Il faut se protéger contre les attaques par injection SQL.  

2. **Utiliser un ORM (Object-Relational Mapper) comme SQLAlchemy**  
   - SQLAlchemy permet d’interagir avec la base de données en manipulant des objets Python au lieu d’écrire du SQL brut.  
   - Il simplifie la gestion des requêtes tout en garantissant la sécurité contre les injections SQL.  
   - Il convertit automatiquement les données entre Python et SQLite.  
   - Il facilite la migration de la base de données si on change de moteur SQL (ex: passer de SQLite à PostgreSQL).  

Dans ce projet, SQLAlchemy joue un rôle clé dans la couche "Database Classes". Il agit comme **un intermédiaire entre l'API (FastAPI) et la base de données (SQLite)**, en traduisant les requêtes API en opérations sur la base de données tout en maintenant un code propre et sécurisé. 

---

Pour utiliser SQLAlchemy, préalablement on l'installe dans l'environnement virtuel :

```bash
pip install sqlalchemy
```

---

## Fichiers nécessaires pour requêter la database SQLite à l'aide de Python

### database.py

```python
"""Database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

# # Créer un moteur de base de données (engine) qui établit la connexion avec la base SQLite (movies.db).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Définir SessionLocal, qui permet de créer des sessions pour interagir avec la base de données.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définir Base, qui servira de classe de base pour les modèles SQLAlchemy.
Base = declarative_base()

# # Optionnel : pour exécuter une vérification de la connexion à la base de données
# # (peut être utile pour le débogage ou la configuration initiale).
# if __name__ == "__main__":
#     try:
#         with engine.connect() as conn:
#             print("Connexion à la base de données réussie.")
#     except Exception as e:
#         print(f"Erreur de connexion : {e}")
```

---

Voici une explication claire et simple de ce que font les trois instructions, avec un focus sur **les arguments** :

#### 1. `create_engine(...)`

```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
```

Cette ligne **crée un moteur de base de données SQLAlchemy** qui va permettre à l'application Python d’interagir avec la base SQLite.

##### Explication des arguments :
- **`SQLALCHEMY_DATABASE_URL`** : c’est l’URL de connexion à la base. Exemple ici :
  ```
  "sqlite:///./movies.db"
  ```
  > Cela veut dire : utiliser SQLite et se connecter à un fichier nommé `movies.db` situé dans le même dossier que ce fichier Python.

- **`connect_args={"check_same_thread": False}`** :
  - SQLite, par défaut, **interdit l'utilisation de la même connexion dans plusieurs threads**.
  - Or, FastAPI (et d'autres frameworks web) peuvent utiliser du **multithreading** pour gérer plusieurs requêtes en parallèle.
  - Donc `check_same_thread=False` **désactive cette restriction**.
  - Attention : À utiliser uniquement si **l'on gère bien les sessions SQLAlchemy** (ce que fait FastAPI avec dépendances `Depends()`).

---

#### 2. `sessionmaker(...)`

```python
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

`sessionmaker` est une **fabrique de sessions**. On l’utilise pour créer des sessions qui vont  permettre de lire/écrire dans la base de données.

##### Explication des arguments :
- **`autocommit=False`** :
  - Cela signifie que **on doit valider les transactions manuellement** (avec `.commit()`).
  - C’est plus sûr : on peut rollback en cas d’erreur.

- **`autoflush=False`** :
  - Si c'était `True`, SQLAlchemy enverrait automatiquement les changements en base **avant certaines requêtes SELECT**.
  - Ici, on veut plus de contrôle. Donc on met `False` : les changements sont flushés **manuellement ou au moment du commit**.

- **`bind=engine`** :
  - Lie la session à l’**engine**  créé plus haut.
  - Ainsi, toutes les sessions créées avec `SessionLocal()` vont utiliser la base `movies.db`.


##### 🧪 Exemple d'utilisation de `SessionLocal` :

```python
db = SessionLocal()
try:
    movies = db.query(Movie).all()
finally:
    db.close()
```

---

#### 3. `declarative_base()`

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()
```

Cette ligne crée une **classe de base** nommée `Base` à partir de laquelle **tous les modèles (tables)** vont hériter.

##### Pourquoi c’est utile ?

Lorsqu'on définis une classe comme ceci :

```python
class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
```

On est en train de créer :
- une **classe Python** (`Movie`)
- qui est **liée à une table SQL** (`movies`)
- avec des **colonnes** (`id`, `title`…)

Mais pour que SQLAlchemy comprenne que `Movie` doit être **une table dans la base de données**, il faut qu’elle hérite d’une **classe spéciale**, et c’est justement ce que `Base = declarative_base()` fournit.

##### En résumé :

| Élément                  | Rôle                                                                 |
|--------------------------|----------------------------------------------------------------------|
| `declarative_base()`     | Crée une superclasse `Base`                                          |
| `Base`                   | Sert de base à tous les modèles SQLAlchemy                          |
| Classe qui hérite de `Base` | Devient une table dans la base de données via la **declarative mapping** |


### models.py

Un Modèle dans SQLAlchemy est une classe Python qui représente une table de la base de données. Chaque attribut de la classe correspond à une colonne de la table.

Le fichier models.py contiendra la représentation pythonique des tables de la base de données. Les classes de ce fichier seront utilisées lorsque les utilisateurs de l'API interrogereront la base de données.

```python
"""SQLAlchemy models"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship # permet des relations de clé étrangère entre les tables.
from database import Base

class Movie(Base):
    __tablename__ = "movies"

    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genres = Column(String)

    ratings = relationship("Rating", back_populates="movie")
    tags = relationship("Tag", back_populates="movie")
    link = relationship("Link", uselist=False, back_populates="movie")


class Rating(Base):
    __tablename__ = "ratings"

    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    rating = Column(Float)
    timestamp = Column(Integer)

    movie = relationship("Movie", back_populates="ratings")


class Tag(Base):
    __tablename__ = "tags"

    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    tag = Column(String, primary_key=True)
    timestamp = Column(Integer)

    movie = relationship("Movie", back_populates="tags")


class Link(Base):
    __tablename__ = "links"

    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    imdbId = Column(String)
    tmdbId = Column(Integer)

    movie = relationship("Movie", back_populates="link")
```

Chaque table est bien représentée avec ses clés primaires, clés étrangères et types.

#### Explication de la classe Movie

Maintenant définir la classe `Movie`, qui est la classe Python utilisée pour stocker les données de la table SQLite `movies`. Cette classe est une sous-classe de `Base`, un modèle de base importé depuis le fichier `database.py`.  

Nous utilisons l’attribut spécial `__tablename__` pour indiquer à SQLAlchemy que cette classe est associée à la table `movies`. Ainsi, lorsque nous interrogerons SQLAlchemy avec la classe `Movie`, il saura automatiquement qu’il doit récupérer les données de la table `movies`. C’est l’un des principaux avantages d’un ORM : il permet de mapper le code Python à la base de données sous-jacente de manière transparente.  

```python
class Movie(Base):
    __tablename__ = "movies"
```

Le reste de la définition de la classe `Movie` permet de mapper les colonnes de la base de données aux attributs Python correspondants. Chaque attribut est défini à l’aide de la fonction `Column` fournie par SQLAlchemy :  

```python
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genres = Column(String)
```

Voici quelques points à noter sur ces définitions :  

- **Les noms des attributs** (`movieId`, `title`, `genres`) correspondent directement aux noms des colonnes dans la base de données.  
- **Les types de données** utilisés (`Integer`, `String`) sont fournis par SQLAlchemy et doivent être importés avant d’être utilisés. Ils correspondent aux types SQL sous-jacents dans SQLite.  
- **La clé primaire** (`movieId`) est définie avec `primary_key=True`, ce qui permet d’assurer l’unicité des enregistrements et d’optimiser les requêtes.  

En plus des colonnes, on définit des **relations** entre les tables en utilisant la fonction `relationship()`. Cela permet d’accéder facilement aux données associées sans avoir à écrire des jointures SQL complexes :  

```python
    ratings = relationship("Rating", back_populates="movie", cascade="all, delete")
    tags = relationship("Tag", back_populates="movie", cascade="all, delete")
    link = relationship("Link", back_populates="movie", uselist=False, cascade="all, delete")
```

Explication des relations :  

- **`ratings = relationship("Rating", back_populates="movie")`**  
  - Cela établit une relation entre la classe `Movie` et `Rating`.  
  - `back_populates="movie"` signifie que chaque objet `Rating` aura aussi un attribut `movie` pointant vers le film correspondant.  

- **`tags = relationship("Tag", back_populates="movie")`**  
  - De la même manière, cette relation permet de récupérer tous les tags associés à un film.  

- **`link = relationship("Link", back_populates="movie", uselist=False)`**  
  - Cette relation est un peu différente : `uselist=False` signifie qu’il ne peut y avoir qu’un seul lien (`Link`) pour chaque film (`Movie`).  

Grâce à ces relations, nous pourrons écrire du code comme ceci pour récupérer les évaluations d’un film :  

```python
movie = session.query(Movie).filter_by(movieId=1).first()
print(movie.ratings)  # Affichera toutes les évaluations associées au film avec ID 1
```

Cela permet d’exploiter la puissance de SQLAlchemy pour manipuler les données de manière simple et intuitive.


#### Test de chaque classe avec le fichier test_models.py 

```python
# %% Importer les modules et créer une session
from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# %% Tester la récupération de quelques films
movies = db.query(Movie).limit(5).all()

if movies:
    for movie in movies:
        print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")
else:
    print("Aucun film trouvé dans la base de données.")

# %% Récupérer les films d'un genre spécifique (ex: Action)
action_movies = db.query(Movie).filter(Movie.genres.like("%Action%")).limit(5).all()

if action_movies:
    for movie in action_movies:
        print(f"[Action] ID: {movie.movieId}, Titre: {movie.title}")
else:
    print("Aucun film d'action trouvé.")

# %% Tester la récupération des évaluations (ratings)
ratings = db.query(Rating).limit(5).all()

if ratings:
    for rating in ratings:
        print(f"User {rating.userId} a noté le film {rating.movieId} avec {rating.rating}/5")
else:
    print("Aucune évaluation trouvée.")

# %% Récupérer les films avec une note >= 4.0
high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating, Movie.movieId == Rating.movieId)
    .filter(Rating.rating >= 4.0)
    .limit(5)
    .all()
)

if high_rated_movies:
    for title, rating in high_rated_movies:
        print(f"Film: {title}, Note: {rating}/5")
else:
    print("Aucun film avec une note >= 4 trouvé.")

# %% Tester la récupération des tags associés aux films
tags = db.query(Tag).limit(5).all()

if tags:
    for tag in tags:
        print(f"User {tag.userId} a tagué le film {tag.movieId} avec '{tag.tag}'")
else:
    print("Aucun tag trouvé.")

# %% Tester la récupération des liens (IMDB, TMDB)
links = db.query(Link).limit(5).all()

if links:
    for link in links:
        print(f"Film ID {link.movieId} → IMDB: {link.imdbId}, TMDB: {link.tmdbId}")
else:
    print("Aucun lien trouvé.")

# %% Fermer la session
db.close()
```

Ce fichier permet de tester facilement et de manière interactive (cellule par cellule comme dans un notebook) chaque classe du Modèle de données de notre API en lecture seule.


### query_helpers.py

Les fichiers *database.py* et *models.py* nous permettent de nous connecter à la base de données et aux classes qui représentent les tables.

Pour tester les classes, on a utilisé des requêtes définies dans le fichier test_models.py

Afin de faciliter le travail pour les fucturs développement notemment lors de la construction de l'API avec FastAPI, il serait bien de définir des **fonctions d'aide** pour écrire plus simplement les requêtes. C'est l'objectif du fichier query_helpers.py.


```python
"""SQLAlchemy Query Functions for MovieLens API"""
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

import models

# --- Films ---
def get_movie(db: Session, movie_id: int):
    """Récupère un film par son ID."""
    return db.query(models.Movie).filter(models.Movie.movieId == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100, title: str = None, genre: str = None):
    """Récupère une liste de films avec filtres optionnels."""
    query = db.query(models.Movie)
    
    if title:
        query = query.filter(models.Movie.title.ilike(f"%{title}%"))
    if genre:
        query = query.filter(models.Movie.genres.ilike(f"%{genre}%"))
    
    return query.offset(skip).limit(limit).all()

# --- Évaluations ---
def get_rating(db: Session, rating_id: int):
    """Récupère une évaluation par son ID."""
    return db.query(models.Rating).filter(models.Rating.id == rating_id).first()

def get_ratings(db: Session, skip: int = 0, limit: int = 100, movie_id: int = None, user_id: int = None, min_rating: float = None):
    """Récupère une liste d'évaluations avec filtres optionnels."""
    query = db.query(models.Rating)
    
    if movie_id:
        query = query.filter(models.Rating.movieId == movie_id)
    if user_id:
        query = query.filter(models.Rating.userId == user_id)
    if min_rating:
        query = query.filter(models.Rating.rating >= min_rating)
    
    return query.offset(skip).limit(limit).all()

# --- Tags ---
def get_tag(db: Session, tag_id: int):
    """Récupère un tag par son ID."""
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

def get_tags(db: Session, skip: int = 0, limit: int = 100, movie_id: int = None, user_id: int = None):
    """Récupère une liste de tags avec filtres optionnels."""
    query = db.query(models.Tag)
    
    if movie_id:
        query = query.filter(models.Tag.movieId == movie_id)
    if user_id:
        query = query.filter(models.Tag.userId == user_id)
    
    return query.offset(skip).limit(limit).all()

# --- Liens ---
def get_link(db: Session, movie_id: int):
    """Récupère les liens IMDB et TMDB pour un film donné."""
    return db.query(models.Link).filter(models.Link.movieId == movie_id).first()

def get_links(db: Session, skip: int = 0, limit: int = 100):
    """Récupère une liste de liens IMDB et TMDB."""
    return db.query(models.Link).offset(skip).limit(limit).all()

# --- Requêtes analytiques ---
def get_movie_count(db: Session):
    """Retourne le nombre total de films."""
    return db.query(models.Movie).count()

def get_rating_count(db: Session):
    """Retourne le nombre total d'évaluations."""
    return db.query(models.Rating).count()

def get_tag_count(db: Session):
    """Retourne le nombre total de tags."""
    return db.query(models.Tag).count()

def get_link_count(db: Session):
    """Retourne le nombre total de liens."""
    return db.query(models.Link).count()
```

Ces fonctions vont **simplifier l'accès aux données** pour l'API tout en rendant le code **plus propre et maintenable**.

---

### Test d'utilisation des fonctions d'aide avec le fichier test_query_helpers.py

Exemple de test interactif dans un script :

```python
# %%
from database import SessionLocal
import api.query_helpers as query_helpers

# Créer une session
db = SessionLocal()

# %%
# Tester la récupération de films
movies = query_helpers.get_movies(db, limit=5, genre="Comedy")

for movie in movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")

# %%
# Fermer la session
db.close()
```

## FastAPI

### Qu'est-ce que FastAPI ?

FastAPI est un **framework web en Python** spécialement conçu pour créer des **API** (interfaces de programmation d’applications). Un framework web, c’est un ensemble d’outils qui simplifie la création d’applications web. Il existe plusieurs frameworks populaires comme Flask, Django ou encore Express (pour JavaScript). FastAPI se distingue par sa simplicité, sa rapidité et sa puissance.

#### Pourquoi utiliser FastAPI ?

FastAPI a été créé pour que les développeurs puissent construire des APIs **rapides**, **fiables** et **faciles à maintenir**. Il gère toute la "plomberie" du web : la gestion des requêtes HTTP, des réponses, des erreurs, etc., avec très peu de code.

Voici quelques raisons pour lesquelles FastAPI est un excellent choix :

- **Rapide** : Les performances sont comparables à celles de Node.js ou Go.
- **Productivité élevée** : Grâce à la syntaxe simple et l’auto-complétion dans les éditeurs comme VS Code.
- **Documentation interactive** : Une fois l’API lancée, FastAPI génère automatiquement une documentation complète et interactive à l’adresse `/docs`.
- **Spécifications OpenAPI** : FastAPI produit automatiquement une description standardisée de l'API, utile pour l’intégration avec d’autres outils.
- **Support de fonctionnalités avancées** : comme la validation automatique des données, la gestion de la sécurité, le versionnement d’API, etc.

#### Un framework jeune mais puissant

FastAPI est un projet **open source**, lancé en **2018** par **Sebastián Ramírez Montaño**. Malgré sa jeunesse, il est déjà largement adopté dans la communauté Python pour le développement d’APIs modernes et performantes.

Pour utiliser FastAPI, on doit préalablement l'installer :

```bash
pip install "fastapi[standard]"
```

L'installation du Framework *FastAPI* permet d'installer automatiquement les outils *httpx*, *Pydantic* ainsi que *Uvicorn* qui  jouent chacun un rôle bien défini et complémentaire.

Dans l’écosystème **FastAPI**, ces trois outils — **httpx**, **Pydantic**, et **Uvicorn** — jouent chacun un rôle bien défini et complémentaire :

**Pydantic** – La validation de données

- **Rôle** : Fournit des modèles de données avec validation automatique.
- **Utilisé par FastAPI pour** :
  - Définir les **schemas** d’entrée/sortie (requêtes et réponses).
  - Valider automatiquement les données (types, formats, etc.).
  - Générer la documentation interactive (OpenAPI / Swagger).

**Uvicorn** – Le serveur ASGI

- **Rôle** : Serveur d'application **ASGI** ultra-rapide, utilisé pour exécuter les applications FastAPI.
- **Pourquoi ASGI ?** : Parce que FastAPI est **asynchrone** (gère plusieurs requêtes en même temps).
- **Alternative** : On peut aussi utiliser `Hypercorn`, mais `Uvicorn` est le plus courant.

**httpx** – Le client HTTP asynchrone

- **Rôle** : Faire des appels HTTP vers d'autres APIs (comme `requests`, mais **async**).
- **Utilisé pour** :
  - Consommer d'autres APIs dans tes endpoints FastAPI.
  - Tester des endpoints pendant le développement.

---

### Schémas Pydantic dans un projet FastAPI

Quand on construit une **API**, il est important de **contrôler les données** qui entrent dans l’application (par exemple via une requête POST) et celles qui sortent (les réponses envoyées au client).

C’est là que **Pydantic** entre en jeu.

#### Qu’est-ce qu’un schéma Pydantic ?
Un schéma Pydantic est une **classe spéciale** (basée sur `BaseModel`) qui permet de :

- **Valider automatiquement** les données (types, formats…).
- **Sérialiser** les données (par exemple, convertir un objet SQLAlchemy en JSON).
- **Générer automatiquement la documentation Swagger** avec les bons champs et les bons types.

#### Dans le cadre de ce projet (API MovieLens en lecture seule)

Notre API permet uniquement de **consulter les données** (films, évaluations, etc.), donc :

- On utilise les schémas Pydantic pour **structurer les réponses** que l’API envoie.
- Cela garantit que seules les données utiles et bien formatées sont retournées.
- Cela évite aussi d’exposer des champs sensibles ou inutiles (comme des IDs techniques ou des relations complexes inutiles dans la réponse).


#### Résumé

| Rôle des schémas Pydantic | Pourquoi c’est utile |
|---------------------------|----------------------|
| Validation des données    | Évite les erreurs et les mauvaises entrées |
| Contrôle des réponses     | Sécurité + simplicité côté client |
| Documentation automatique | Swagger bien généré, lisible pour tous |
| Compatible avec SQLAlchemy| Conversion facile des objets ORM |

---

Voici le fichier *schemas.py* qui définit les schémas Pydantic :

```python
from pydantic import BaseModel
from typing import Optional, List


# --- Schémas secondaires ---

class RatingBase(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int

    class Config:
        orm_mode = True


class TagBase(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int

    class Config:
        orm_mode = True


class LinkBase(BaseModel):
    imdbId: Optional[str]
    tmdbId: Optional[int]

    class Config:
        orm_mode = True


# --- Schéma principal pour Movie ---
class MovieBase(BaseModel):
    movieId: int
    title: str
    genres: Optional[str] = None

    class Config:
        orm_mode = True


class MovieDetailed(MovieBase):
    ratings: List[RatingBase] = []
    tags: List[TagBase] = []
    link: Optional[LinkBase] = None


# --- Schéma pour liste de films (sans détails imbriqués) ---
class MovieSimple(BaseModel):
    movieId: int
    title: str
    genres: Optional[str]

    class Config:
        orm_mode = True


# --- Pour les endpoints de /ratings et /tags si appelés seuls ---
class RatingSimple(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int

    class Config:
        orm_mode = True


class TagSimple(BaseModel):
    userId: int
    movieId: int
    tag: str
    timestamp: int

    class Config:
        orm_mode = True


class LinkSimple(BaseModel):
    movieId: int
    imdbId: Optional[str]
    tmdbId: Optional[int]

    class Config:
        orm_mode = True

```

Ce fichier définit les **schémas de données** utilisés dans l'API pour :
- structurer ce que l’API **envoie** (en sortie, dans les réponses),
- valider ce que l’API **reçoit** (en entrée, dans les requêtes POST/PUT).

Ces schémas utilisent **Pydantic**, une bibliothèque de validation de données très utilisée avec FastAPI.

Ci-dessous l'explication du fichier :

* **Importations**

```python
from pydantic import BaseModel
from typing import Optional, List
```

- `BaseModel` : classe de base fournie par Pydantic. Tous les schémas doivent en hériter.
- `Optional[X]` : signifie que le champ peut être `None` (il est facultatif).
- `List[X]` : signifie qu’on attend une **liste d’éléments** de type `X`.

---

* **Schémas secondaires (associés aux films)**

Ces classes représentent les **données associées** à un film : notes, tags, et liens.

    ***`RatingBase`***

```python
class RatingBase(BaseModel):
    userId: int
    movieId: int
    rating: float
    timestamp: int

    class Config:
        orm_mode = True
```

- Représente une **note** donnée par un utilisateur à un film.
- `orm_mode = True` indique à FastAPI qu'on peut créer ce schéma à partir d’un objet SQLAlchemy (ce qui est le cas dans ce projet).

---

    ***`TagBase`***

Même principe que `RatingBase`, mais pour les **tags** (mots-clés ajoutés par les utilisateurs).

---

    ***`LinkBase`***

Représente les **liens externes** d’un film :
- `imdbId` (IMDb)
- `tmdbId` (The Movie DB)

---

* **Schéma principal pour les films**

    ***`MovieBase`***

```python
class MovieBase(BaseModel):
    movieId: int
    title: str
    genres: Optional[str] = None

    class Config:
        orm_mode = True
```

- Schéma de base pour un film.
- Contient juste les **infos essentielles** : ID, titre et genres.

---

    ***`MovieDetailed`***

```python
class MovieDetailed(MovieBase):
    ratings: List[RatingBase] = []
    tags: List[TagBase] = []
    link: Optional[LinkBase] = None
```

- Hérite de `MovieBase`.
- Ajoute les **détails imbriqués** :
  - `ratings` : liste des notes
  - `tags` : liste des tags
  - `link` : les identifiants externes (IMDb, TMDb)

➡️ C’est ce schéma qui est utilisé pour des **détails complets sur un film**, ex: `/movies/1`.

---

* **Schéma simplifié pour les listes de films**

```python
class MovieSimple(BaseModel):
    movieId: int
    title: str
    genres: Optional[str]

    class Config:
        orm_mode = True
```

- Identique à `MovieBase` mais utilisé **sans détails imbriqués**, pour les **listes de films** (ex: endpoint `/movies`).

---

* **Schémas "simples" pour utiliser indépendamment**

Si on expose un jour des endpoints `/ratings` ou `/tags` seuls, on pourra utiliser ces schémas :

- `RatingSimple` : une note
- `TagSimple` : un tag
- `LinkSimple` : un lien (inclut aussi `movieId` contrairement à `LinkBase`)

---

* **En résumé**

| Schéma          | Utilisé pour...                          |
|-----------------|-------------------------------------------|
| `MovieSimple`   | Liste de films, sans détails              |
| `MovieDetailed` | Détails complets d’un film                |
| `RatingBase`    | Note liée à un film (imbriquée ou non)    |
| `TagBase`       | Tag lié à un film                         |
| `LinkBase`      | Lien IMDb ou TMDb (imbriqué)              |
| `LinkSimple`    | Lien utilisé seul, avec `movieId`         |


### Code de l'API : fichier main.py

On va construire pas à pas l'API avec FastAPI en ajoutant progressivement les Endpoints (points de terminaison).

#### Endoint de vérification que l'API MovieLens fonctionne

```python
from fastapi import FastAPI, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional

from database import SessionLocal
import models
import query_helpers as helpers
import schemas  # Ajouté pour utiliser les schémas Pydantic

# Initialisation de l'application FastAPI
app = FastAPI(
    title="MovieLens API", 
    description="API pour interroger la base de données MovieLens", 
    version="0.1"
)

# Dépendance pour récupérer une session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint de health check
@app.get(
    "/",
    summary="Vérifie si l'API MovieLens fonctionne",
    description="""
    Ce point d'entrée permet de vérifier si l'API MovieLens est opérationnelle. 
    """,
    response_description="Un message de confirmation si l'API fonctionne correctement.",
    operation_id="health_check_movies_api",
    tags=["monitoring"],
)
async def root():
    return {"message": "API MovieLens opérationnelle"}
```

Exécutons FastAPI en mode développement avec rechargement automatique à chaque modification du fichier *main.py* :

```bash
(.venv) vant@MOOVE15:~/Documents/business/movielens-project$ cd api
(.venv) vant@MOOVE15:~/Documents/business/movielens-project/api$ uvicorn main:app --reload
```

Accéder ensuite à l'API : http://127.0.0.1:8000/

L'API s'ouvre dans le navigateur par défaut de la machine ( de l'ordinateur ) et on voit bien apparaître : {"message":"API MovieLens opérationnelle"}

On peut aussi accéder à la doc interactive Swagger sur http://127.0.0.1:8000/docs

Rajoutons un autre point de terminaison (endpoint).

#### Endpoint pour obtenir un film par son identifiant

```python
# Endpoint pour obtenir un film par son ID
@app.get(
    "/movies/{movie_id}",
    summary="Obtenir un film par son ID",
    description="Retourne les informations d’un film en utilisant son `movieId`.",
    response_description="Détails du film",
    response_model=schemas.MovieDetailed,
    tags=["films"],
)
def read_movie(movie_id: int = Path(..., description="L'identifiant unique du film"), db: Session = Depends(get_db)):
    movie = helpers.get_movie(db, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail=f"Film avec l'ID {movie_id} non trouvé")
    return movie
```

Si besoin actualiser l'API au niveau du navigateur.

Au cours du développement de l'API, on peut tester un point de terminaison de deux manières :

##### Méthode 1 : Utiliser Swagger UI (recommandée)

1. **Lance ton app** (si ce n’est pas déjà fait) :
   ```bash
   uvicorn main:app --reload
   ```

2. Aller dans le navigateur à l'adresse :
   ```
   http://127.0.0.1:8000/docs
   ```

3. On voit une interface interactive avec **tous tes endpoints**. Cliquer sur :
   - **GET** `/movies/{movie_id}`  
   - Cliquer sur le bouton **"Try it out"**  
   - Entrer un `movie_id` (par exemple `1`)  
   - Cliquer sur **"Execute"**

4. On voit la requête envoyée, la réponse JSON, et le code de retour HTTP (200, 404, etc.)

---

##### Méthode 2 : Entrer directement l’URL dans le navigateur

Si on veut tester sans passer par Swagger, il suffit de taper simplement dans la barre d’adresse :

```
http://127.0.0.1:8000/movies/1
```

(remplace `1` par n’importe quel `movie_id` qui existe dans la base)

---

##### Remarques

- Si l'on reçoit une **erreur 404**, c’est que :
  - Le `movie_id` n'existe pas dans la base
  - Ou bien l’endpoint `/movies/{movie_id}` n’est pas encore bien défini dans `main.py`

Pour tous les autres tests de point de terminaison, on utilisera Swagger.

Rajoutons un autre point de terminaison.

#### Endpoint pour obtenir une liste des films (avec pagination et filtres facultatifs title, genre, skip, limit)

```python
@app.get(
    "/movies",
    summary="Lister les films",
    description="Retourne une liste de films avec pagination et filtres optionnels par titre ou genre.",
    response_description="Liste de films",
    response_model=List[schemas.MovieSimple],
    tags=["films"],
)
def list_movies(
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"),
    title: str = Query(None, description="Filtre par titre"),
    genre: str = Query(None, description="Filtre par genre"),
    db: Session = Depends(get_db)
):
    movies = helpers.get_movies(db, skip=skip, limit=limit, title=title, genre=genre)
    return movies
```

Pour tester le endpoint `/movies`, voici des **exemples de requêtes HTTP**  entrés dans le navigateur ou via Swagger UI :

---

##### 1. **Obtenir la liste des 100 premiers films (valeurs par défaut)**

 URL :
```
http://127.0.0.1:8000/movies
```

 Résultat attendu :  
Une liste de 100 films (ou moins s’il y en a moins en base).

---

##### 2. **Pagination – Obtenir les 20 films suivants après les 100 premiers**

 URL :
```
http://127.0.0.1:8000/movies?skip=100&limit=20
```

 Résultat :  
Les films allant de l’index 101 à 120.

---

##### 3. **Filtrer par titre (recherche partielle)**

 URL :
```
http://127.0.0.1:8000/movies?title=story
```

 Résultat :  
Tous les films dont le titre contient “story” (ex: *Toy Story*, *Love Story*…).

---

##### 4. **Filtrer par genre**

 URL :
```
http://127.0.0.1:8000/movies?genre=Comedy
```

 Résultat :  
Tous les films dont le genre contient “Comedy”.

---

##### 5. **Combiner filtres : titre + genre + pagination**

 URL :
```
http://127.0.0.1:8000/movies?title=story&genre=Adventure&skip=0&limit=5
```

 Résultat :  
Les 5 premiers films dont le titre contient “story” **et** le genre contient “Adventure”.

---

On peut aussi faire tout ça dans Swagger UI :  
 http://127.0.0.1:8000/docs → sélectionne `/movies` → *Try it out*

---

Rajouter un autre point de terminaison dans le fichier main.py

#### Endpoint pour obtenir une évaluation par utilisateur et film

**Objectif de l’endpoint** : Récupérer une **évaluation (rating)** donnée par un utilisateur (`user_id`) pour un film (`movie_id`).

```python
# Endpoint pour obtenir une évaluation par utilisateur et film
@app.get(
    "/ratings/{user_id}/{movie_id}",
    summary="Obtenir une évaluation par utilisateur et film",
    description="Retourne l'évaluation d'un utilisateur pour un film donné.",
    response_description="Détails de l'évaluation",
    response_model=schemas.RatingSimple,
    tags=["évaluations"],
)
def read_rating(
    user_id: int = Path(..., description="ID de l'utilisateur"),
    movie_id: int = Path(..., description="ID du film"),
    db: Session = Depends(get_db)
):
    rating = helpers.get_rating(db, user_id=user_id, movie_id=movie_id)
    if rating is None:
        raise HTTPException(
            status_code=404,
            detail=f"Aucune évaluation trouvée pour l'utilisateur {user_id} et le film {movie_id}"
        )
    return rating
```

Voici des exemples concrets qu'on peut tester dans ton navigateur pour le nouvel **endpoint `/ratings/{user_id}/{movie_id}`**.

---

**Format URL :**
```
http://localhost:8000/ratings/{user_id}/{movie_id}
```

---

##### **Cas 1 : L'utilisateur a évalué le film**

**Exemple URL (à adapter à la base de données) :**
```
http://localhost:8000/ratings/1/1
```

Cela recherche l’évaluation laissée par **l’utilisateur 1** pour **le film 1**.

 **Réponse JSON attendue :**
```json
{
  "userId": 1,
  "movieId": 1,
  "rating": 4.0,
  "timestamp": 964982703
}
```

---

##### **Cas 2 : L'utilisateur N’A PAS évalué ce film**

**Exemple URL :**
```
http://localhost:8000/ratings/1/999999
```

 **Réponse attendue :**
```json
{
  "detail": "Aucune évaluation trouvée pour l'utilisateur 1 et le film 999999"
}
```
Statut HTTP : `404 Not Found`

---

##### **Cas 3 : L’`user_id` ou le `movie_id` n’existe pas dans la base**

**Exemple :**
```
http://localhost:8000/ratings/999999/999999
```

Même résultat que le cas 2 : **404 Not Found**

---

##### **Cas 4 : Valeurs invalides (ex : texte au lieu d’un entier)**

**Exemple :**
```
http://localhost:8000/ratings/abc/def
```

 **FastAPI va répondre automatiquement** avec un message d’erreur de validation :
```json
{
  "detail": [
    {
      "loc": ["path", "user_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    },
    {
      "loc": ["path", "movie_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```
Statut HTTP : `422 Unprocessable Entity`

---

##### Astuce : Utiliser l’interface Swagger UI

On peut aussi **tester facilement cet endpoint dans le navigateur à l’adresse :**

```
http://localhost:8000/docs
```

 Cliquer sur `GET /ratings/{user_id}/{movie_id}` → **Try it out** → entrer des valeurs → **Execute**

---

Rajouter un autre point de terminaison dans le fichier main.py

#### Endpoint pour obtenir une liste d’évaluations avec pagination et filtres optionnels (film, utilisateur, note min)

```http
GET /ratings
```

Ce endpoint permet de lister les évaluations avec les **filtres optionnels** suivants :

- `skip` (int) : nombre d’éléments à ignorer (pagination)
- `limit` (int) : nombre maximum d’évaluations à retourner
- `movie_id` (int) : filtre par identifiant de film
- `user_id` (int) : filtre par identifiant d'utilisateur
- `min_rating` (float) : filtre pour ne retourner que les notes ≥ min_rating

**URL de base (local)**

```
http://localhost:8000/ratings
```

```python
# Endpoint pour obtenir une liste d’évaluations avec filtres
@app.get(
    "/ratings",
    summary="Lister les évaluations",
    description="Retourne une liste d’évaluations avec pagination et filtres optionnels (film, utilisateur, note min).",
    response_description="Liste des évaluations",
    response_model=List[schemas.RatingSimple],
    tags=["évaluations"],
)
def list_ratings(
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"),
    movie_id: Optional[int] = Query(None, description="Filtrer par ID de film"),
    user_id: Optional[int] = Query(None, description="Filtrer par ID d'utilisateur"),
    min_rating: Optional[float] = Query(None, ge=0.0, le=5.0, description="Filtrer les notes supérieures ou égales à cette valeur"),
    db: Session = Depends(get_db)
):
    ratings = helpers.get_ratings(db, skip=skip, limit=limit, movie_id=movie_id, user_id=user_id, min_rating=min_rating)
    return ratings
```

Voici **tous les cas possibles** pour tester le endpoint **`GET /ratings`** directement dans le navigateur ou via l'interface Swagger de FastAPI.

---

##### **Cas 1 : Liste des 100 premières évaluations**

```http
http://localhost:8000/ratings
```

 **Comportement attendu :** retourne 100 évaluations (par défaut).

---

##### **Cas 2 : Pagination — 10 évaluations à partir de la 50e**

```http
http://localhost:8000/ratings?skip=50&limit=10
```

 Retourne les évaluations 51 à 60.

---

##### **Cas 3 : Filtrer par `movie_id` (ex : film 1)**

```http
http://localhost:8000/ratings?movie_id=1
```

 Retourne les évaluations pour le **film 1** uniquement.

---

##### **Cas 4 : Filtrer par `user_id` (ex : utilisateur 2)**

```http
http://localhost:8000/ratings?user_id=2
```

 Retourne toutes les évaluations faites par l'utilisateur 2.

---

##### **Cas 5 : Filtrer par `min_rating` (ex : note ≥ 4.5)**

```http
http://localhost:8000/ratings?min_rating=4.5
```

 Retourne toutes les évaluations ayant une note **≥ 4.5**.

---

##### **Cas 6 : Filtre combiné — utilisateur 1, film 1, note ≥ 3**

```http
http://localhost:8000/ratings?user_id=1&movie_id=1&min_rating=3
```

 Retourne l'évaluation de l'utilisateur 1 pour le film 1 si elle est ≥ 3.

---

##### **Cas 7 : Aucun résultat (valeurs valides mais sans correspondance)**

```http
http://localhost:8000/ratings?user_id=123456&movie_id=654321
```

➡️ Réponse :
```json
[]
```
Statut HTTP : `200 OK` (liste vide)

---

##### **Cas 8 : Valeurs invalides**

```http
http://localhost:8000/ratings?user_id=abc
```

➡️ FastAPI retourne une erreur de validation :
```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "query",
        "user_id"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```
Statut HTTP : `422 Unprocessable Entity`

---

Rajouter un autre point de terminaison dans le fichier main.py

#### Endpoint pour retourner un tag pour un utilisateur et un film donnés, avec le texte du tag

```python
#  Endpoint pour retourner un tag pour un utilisateur et un film donnés, avec le texte du tag
@app.get(
    "/tags/{user_id}/{movie_id}/{tag_text}",
    summary="Obtenir un tag spécifique",
    description="Retourne un tag pour un utilisateur et un film donnés, avec le texte du tag.",
    response_model=schemas.TagSimple,
    tags=["tags"],
)
def read_tag(
    user_id: int = Path(..., description="ID de l'utilisateur"),
    movie_id: int = Path(..., description="ID du film"),
    tag_text: str = Path(..., description="Contenu exact du tag"),
    db: Session = Depends(get_db)
):
    result = helpers.get_tag(db, user_id=user_id, movie_id=movie_id, tag_text=tag_text)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Tag non trouvé pour l'utilisateur {user_id}, le film {movie_id} et le tag '{tag_text}'"
        )
    return result
```

Voici un exemple de test : http://localhost:8000/tags/2/60756/funny et voici le résultat :

```json
{
  "userId": 2,
  "movieId": 60756,
  "tag": "funny",
  "timestamp": 1445714994
}
```

Rajouter un autre point de terminaison dans le fichier main.py

---

#### Endpoint pour retourner une liste de tags avec pagination et filtres facultatifs par utilisateur ou film

```python
# Endpoint pour retourner une liste de tags avec pagination et filtres facultatifs par utilisateur ou film
@app.get(
    "/tags",
    summary="Lister les tags",
    description="Retourne une liste de tags avec pagination et filtres facultatifs par utilisateur ou film.",
    response_model=List[schemas.TagSimple],
    tags=["tags"],
)
def list_tags(
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"),
    movie_id: Optional[int] = Query(None, description="Filtrer par ID de film"),
    user_id: Optional[int] = Query(None, description="Filtrer par ID d'utilisateur"),
    db: Session = Depends(get_db)
):
    return helpers.get_tags(db, skip=skip, limit=limit, movie_id=movie_id, user_id=user_id)
```


Voici des Exemple de requêtes pour tester ce endpoint :

- **Tous les tags (limités à 100 par défaut)**  
  ```bash
  GET /tags
  ```

- **Pagination : page 2 (100 premiers ignorés)**  
  ```bash
  GET /tags?skip=100&limit=100
  ```

- **Filtrage par utilisateur `user_id=2`**  
  ```bash
  GET /tags?user_id=2
  ```

- **Filtrage par film `movie_id=60756`**  
  ```bash
  GET /tags?movie_id=60756
  ```

- **Filtrage combiné**  
  ```bash
  GET /tags?user_id=2&movie_id=60756
  ```

---

Rajouter un autre point de terminaison dans le fichier main.py

#### Endpoint pour retourner les identifiants IMDB et TMDB pour un film donné

```python
# Endpoint pour retourner les identifiants IMDB et TMDB pour un film donné
@app.get(
    "/links/{movie_id}",
    summary="Obtenir le lien d'un film",
    description="Retourne les identifiants IMDB et TMDB pour un film donné.",
    response_model=schemas.LinkSimple,
    tags=["links"],
)
def read_link(
    movie_id: int = Path(..., description="ID du film"),
    db: Session = Depends(get_db)
):
    result = helpers.get_link(db, movie_id=movie_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Aucun lien trouvé pour le film avec l'ID {movie_id}"
        )
    return result
```

Voici un exemple de test de ce endpoint `/links/{movie_id}` dans le **navigateur** :

```
http://localhost:8000/links/1
```

Voici le résultat :

```json
{
  "movieId": 1,
  "imdbId": "0114709",
  "tmdbId": 862
}
```

---

Rajouter un autre point de terminaison dans le fichier main.py

#### Endpoint pour retourner une liste paginée des identifiants IMDB et TMDB de tous les films

```python
# Endpoint pour retourner une liste paginée des identifiants IMDB et TMDB de tous les films
@app.get(
    "/links",
    summary="Lister les liens des films",
    description="Retourne une liste paginée des identifiants IMDB et TMDB de tous les films.",
    response_model=List[schemas.LinkSimple],
    tags=["links"],
)
def list_links(
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"),
    db: Session = Depends(get_db)
):
    return helpers.get_links(db, skip=skip, limit=limit)
```

Exemple d’URL pour tester :

```
http://localhost:8000/links?skip=10&limit=20
```

---

Rajouter un autre point de terminaison dans le fichier main.py

#### Endpoint pour obtenir des statistiques sur la base de données

```python
# Endpoint pour obtenir des statistiques sur la base de données
@app.get(
    "/analytics",
    summary="Obtenir les statistiques analytiques",
    description="Retourne le nombre total de films, évaluations, tags et liens.",
    response_model=schemas.AnalyticsResponse,
    tags=["analytics"]
)
def get_analytics(db: Session = Depends(get_db)):
    movie_count = helpers.get_movie_count(db)
    rating_count = helpers.get_rating_count(db)
    tag_count = helpers.get_tag_count(db)
    link_count = helpers.get_link_count(db)

    return schemas.AnalyticsResponse(
        movie_count=movie_count,
        rating_count=rating_count,
        tag_count=tag_count,
        link_count=link_count
    )
```

Pour tester : http://127.0.0.1:8000/analytics

Résultat : {"movie_count":9742,"rating_count":100836,"tag_count":3683,"link_count":9742}


## Documentation de l'API 

La **documentation** est une étape essentielle pour rendre l'API facile à comprendre et à utiliser. 

FastAPI propose **deux interfaces de documentation intégrées** (ou *built-in*) qu'on peut utiliser sans rien configurer : **Swagger UI** et **ReDoc**. Ces interfaces sont générées automatiquement à partir du code Python (FastAPI) de l'API.

### 1. Swagger UI (interface par défaut)

**Accès** : `http://127.0.0.1:8000/docs`

Avec la documentation Swagger, on peut :

- Voir la **liste des endpoints** (`/movies`, `/movies/{movie_id}`, etc.)
- Lire les **descriptions** et les **paramètres** attendus
- Envoyer des requêtes **GET**, **POST**, etc. directement depuis l’interface
- Visualiser les **réponses JSON**

### 2. ReDoc (documentation plus lisible)

**Accès** : `http://127.0.0.1:8000/redoc`

- Affichage plus **structuré et professionnel**
- Pratique pour une **lecture approfondie** de l’API
- Très apprécié dans les projets en entreprise

---

**À retenir**

| Interface     | URL                         | Usage principal                      |
|---------------|-----------------------------|--------------------------------------|
| Swagger UI    | `/docs`                     | Tester les endpoints facilement      |
| ReDoc         | `/redoc`                    | Lire la doc proprement               |

---

### Amélioration de documentation dans le code de main.py

```python
api_description = """
Bienvenue dans l'API **MovieLens** 

Cette API permet d'interagir avec une base de données inspirée du célèbre jeu de données [MovieLens](https://grouplens.org/datasets/movielens/).  
Elle est idéale pour découvrir comment consommer une API REST avec des données de films, d'utilisateurs, d'évaluations, de tags et de liens externes (IMDB, TMDB).

### Fonctionnalités disponibles :

- Rechercher un film par ID, ou lister tous les films
- Consulter les évaluations (ratings) par utilisateur et/ou film
- Accéder aux tags appliqués par les utilisateurs sur les films
- Obtenir les liens IMDB / TMDB pour un film
- Voir des statistiques globales sur la base

Tous les endpoints supportent la pagination (`skip`, `limit`) et des filtres optionnels selon les cas.

### Bon à savoir
- Vous pouvez tester tous les endpoints directement via l'interface Swagger ci-dessous.
- Pour toute erreur (ex : ID inexistant), une réponse claire est retournée avec le bon code HTTP.
"""

# Initialisation de l'application FastAPI
app = FastAPI(
    title="MovieLens API", 
    description=api_description, 
    version="0.1"
)


# Endpoint pour obtenir des statistiques sur la base de données
@app.get(
    "/analytics",
    summary="Obtenir des statistiques",
    description="""
    Retourne un résumé analytique de la base de données :

    - Nombre total de films
    - Nombre total d’évaluations
    - Nombre total de tags
    - Nombre de liens vers IMDB/TMDB
    """,
    response_model=schemas.AnalyticsResponse,
    tags=["analytics"]
)
def get_analytics(db: Session = Depends(get_db)):
    movie_count = helpers.get_movie_count(db)
    rating_count = helpers.get_rating_count(db)
    tag_count = helpers.get_tag_count(db)
    link_count = helpers.get_link_count(db)

    return schemas.AnalyticsResponse(
        movie_count=movie_count,
        rating_count=rating_count,
        tag_count=tag_count,
        link_count=link_count
    )
```

### 3. README

Grâce aux mises à jour apportées à la documentation Swagger intégrée, nous sommes sur la bonne voie pour offrir une expérience de développement optimale. Cependant, certaines fonctionnalités de la documentation de l'API restent à fournir, notamment la prise en main, les conditions d'utilisation et les exemples de code. 

Pour cela, on créera un superbe README.md (voir api/README.md) dans lequel particulièrement on inclut des exemples de code Python (avec httpx) pour montrer comment utiliser l'API.

**N.B** : On veuille à tester tous les codes Python d'exemples d'utilisation de l'API mises dans le README.

```bash
bello@Bello_Sbre_PC:~/Documents/essai$ source .venv/bin/activate

(.venv) bello@Bello_Sbre_PC:~/Documents/essai$ python
Python 3.13.5 (main, July  3 2025, 09:08:35)
Type "help", "copyright", "credits" or "license" for more information.

>>> # Lister les films

>>> import httpx

>>> response = httpx.get("http://localhost:8000/movies", params={"limit": 5})

>>> print(response.json())

[{'movieId': 1, 'title': 'Toy Story (1995)', 'genres': 'Adventure|Animation|Children|Comedy|Fantasy'}, {'movieId': 2, 'title': 'Jumanji (1995)', 'genres': 'Adventure|Children|Fantasy'}, {'movieId': 3, 'title': 'Grumpier Old Men (1995)', 'genres': 'Comedy|Romance'}, {'movieId': 4, 'title': 'Waiting to Exhale (1995)', 'genres': 'Comedy|Drama|Romance'}, {'movieId': 5, 'title': 'Father of the Bride Part II (1995)', 'genres': 'Comedy'}]

>>> exit()
```

Je rappelle que l'API doit être lancée en local et opérationnelle avant d'exécuter ces codes Python.

## Déploiement de notre API sur le Cloud

### Qu’est-ce que **le Cloud** ?

Le **Cloud** (ou "informatique en nuage") désigne l'ensemble des services informatiques (stockage, bases de données, serveurs, applications...) accessibles via **Internet**, plutôt que d'être hébergés localement sur un ordinateur ou un serveur personnel.

Autrement dit, au lieu de faire tourner l'application sur **l'ordinateur**, on la fait tourner sur un **ordinateur à distance**, accessible en ligne via un **serveur Cloud**.

---

### Pourquoi déployer l'API sur le Cloud ?

Lorsqu'on développez une API (comme celle qu'on a construite dans ce projet), elle est initialement **accessible uniquement en local** (c'est-à-dire uniquement sur la machine). Cela limite son utilité.

> **Déployer sur le Cloud**, c’est la rendre **accessible à tout le monde, partout dans le monde**, via une URL publique !

Cela permet de :
- Tester l'API dans un environnement réel,
- Partager le travail avec d’autres personnes (clients, collègues, recruteurs...),
- Préparer une future mise en production pour un usage professionnel.

---

### ☁️ Les 3 géants du Cloud : AWS, Azure et GCP

Il existe plusieurs grands fournisseurs de services Cloud dans le monde :

| Fournisseur | Nom complet                | Particularités |
|-------------|-----------------------------|----------------|
| **AWS**     | Amazon Web Services         | Le plus ancien et le plus populaire |
| **Azure**   | Microsoft Azure             | Très utilisé dans les grandes entreprises |
| **GCP**     | Google Cloud Platform       | Très bien intégré avec les outils Google |

Ces plateformes proposent toutes des **offres gratuites (Free Tier)**, mais :

 **L'inscription nécessite presque toujours une carte bancaire (carte de crédit)**, même si on ne paye rien immédiatement.


---

### Render : la solution simple et gratuite

Dans ce projet, on a utilisé **[Render](https://render.com/)**, une plateforme **cloud moderne et accessible**, idéale pour les développeurs indépendants, les étudiants et les projets de formation.

> **Render ne demande pas de carte bancaire pour l'inscription** .

Avec Render, on peux :
- Déployer l'API FastAPI en quelques clics,
- Obtenir une URL publique gratuite,
- Gérer les redémarrages automatiques, la scalabilité de base, et plus encore.

---

### Une remarque importante sur les “géants du Cloud”

Il est courant de penser qu’on ne peut **rien faire sans AWS, Azure ou GCP**, comme si ces plateformes étaient **indispensables** pour tout projet sérieux.

 En réalité, **de nombreuses entreprises dans le monde fonctionnent parfaitement sans Cloud**, en hébergeant elles-mêmes leurs serveurs (**on-premise**), c’est-à-dire **sur leurs propres machines**. C’est souvent le cas pour des raisons de sécurité, de confidentialité, ou de réduction des coûts à grande échelle.

---

### En résumé

| Ce qu'on retient |
|---------------------------|
| Le Cloud permet de rendre l'API accessible sur Internet |
| AWS, Azure et GCP sont puissants, mais souvent inaccessibles aux débutants à cause de la demande de carte bancaire |
| Render est une excellente alternative gratuite et sans carte bancaire, parfaite pour ce projet |
| Le Cloud n’est pas une obligation : on peut aussi héberger soi-même ses applications |

---

Voici une section claire et progressive, qui explique étape par étape comment déployer l'API FastAPI sur **Render**.

---

### Étapes détaillées du déploiement sur Render

Maintenant que l'API fonctionne en local, on va la **mettre en ligne gratuitement** grâce à la plateforme **[Render](https://render.com/)**.

---

#### Étape 1 – Préparer les fichiers pour le Cloud

Avant d’envoyer le code sur Render, on s'est rassuré d'avoir vérifier deux choses :

##### 1.1 – Créer un fichier `requirements.txt` dans le dossier `api/`

Ce fichier liste les bibliothèques nécessaires pour faire tourner l'application sur Render. Voici les **lignes minimales** qu'on a dù y mettre :

```
fastapi>=0.115.12
SQLAlchemy>=2.0.40
```

>  On rajoute aussi d'autres dépendances car l'API en utilise (par exemple `uvicorn`, `pydantic`, etc.).

##### 1.2 – Pousser les modifications sur GitHub

 Tout le code est bien **poussé (push)** sur GitHub, au préalabre . Render va se connecter au dépôt GitHub pour récupérer le projet.

---

#### Étape 2 – S'inscrire sur Render

1. [https://render.com](https://render.com)
2. **"Sign up"**
3. inscription avec un **compte GitHub** ou **Google** (très simple et rapide)

---

#### Étape 3 – Créer un nouveau service Web

1. Cliquer sur le bouton **"New"** dans le dashboard puis sélectionner **"Web Service"**

---

#### Étape 4 – Connecter au dépôt GitHub

1. Sélectionner **"Public Git Repository"**
2. Coller l’**URL du dépôt GitHub** (celui contenant l'API)
3. Cliquer sur **"Connect"**

---

#### Étape 5 – Configurer le déploiement

Sur la page suivante (où il est écrit "You are deploying a Web Service"), les champs sont remplis comme ceci :

| Champ              | Valeur attendue                                         |
|--------------------|----------------------------------------------------------|
| **Name**           | Choix d'un nom unique (ex : `movielens-api`)         |
| **Project**        | Ne rien sélectionner / ne pas créer de projet           |
| **Language**       | `Python 3`                                               |
| **Branch**         | `main` (la branche où se trouve le code)          |
| **Region**         | Choix de la région la plus proche         |
| **Root Directory** | `api` (le dossier racine contenant `main.py`)        |
| **Build Command**  | `pip install -r requirements.txt`                       |
| **Start Command**  | `uvicorn main:app --host 0.0.0.0 --port $PORT`          |
| **Instance Type**  | `Free`                                                  |

> Le **Start Command** utilise `uvicorn` directement, sans `fastapi run`. C’est normal pour Render.

---

#### Étape 6 – Lancer le déploiement

1. Descendre tout en bas de la page et Cliquer sur **"Deploy Web Service"**

Render commence à installer les dépendances, à démarrer votre API, et affiche les logs de déploiement.

---

#### Étape 7 – Accéder à votre API en ligne

Quand le message **"Your service is live"** apparaît :
1. on Copie l’URL affichée en haut de la page ( `https://movie-backend-x8iq.onrender.com`)
2. Coller dans un navigateur

On voit ainsi le **message de santé** de l'API (qui est bien défini), ou bien la page de Swagger si on va sur `/docs` :

 Comme ceci :  
 `https://movie-backend-x8iq.onrender.com/docs`  
 Cela ouvre l’interface **Swagger UI** pour tester les endpoints.

---

#### Étape 8 – Tester les endpoints de l’API via Swagger ou navigateur

Une fois l’API déployée, on peut **tester tous les endpoints** comme on l’avais fait en local. Il suffit de se rendre à l’adresse suivante :

**Swagger UI :**  
 `https://movie-backend-x8iq.onrender.com/docs`  
On a une interface interactive qui permet de tester facilement chaque route de l’API.

---

##### Exemple 1 – Endpoint `/movies`

**Lister tous les films :**  
 `https://movie-backend-x8iq.onrender.com/movies`

**Rechercher un film spécifique (ex: `movieId=1`) :**  
 `https://movie-backend-x8iq.onrender.com/movies/1`

---

##### Exemple 2 – Endpoint `/ratings`

**Lister toutes les évaluations :**  
 `https://movie-backend-x8iq.onrender.com/ratings`

**Lister les évaluations pour un film donné (ex: `movieId=1`) :**  
 `https://movie-backend-x8iq.onrender.com/ratings?movie_id=1`

---

##### Exemple 3 – Endpoint `/tags`

**Lister tous les tags :**  
 `https://movie-backend-x8iq.onrender.com/tags`

**Lister les tags pour un film donné (ex: `movieId=1`) :**  
 `https://movie-backend-x8iq.onrender.com/tags?movie_id=1`

---

##### Exemple 4 – Endpoint `/links`

 **Lister tous les liens :**  
 `https://movie-backend-x8iq.onrender.com/links`

**Afficher le lien pour un film donné (ex: `movieId=1`) :**  
 `https://movie-backend-x8iq.onrender.com/links/1`

---

##### Exemple 5 – Endpoint `/analytics`

 **Afficher les statistiques globales de la base de données :**  
 `https://movie-backend-x8iq.onrender.com/analytics`

Ce endpoint retourne un résumé contenant :
- le nombre total de films
- le nombre total d’évaluations
- le nombre total de tags
- le nombre total de liens

---

#### Étape 9 – Tester l’API en Python avec `httpx`

On peut aussi tester l'API **directement depuis un script Python**, en utilisant la librairie `httpx`.  
Cela permet d’intégrer l'API dans un pipeline de données ou une application.

> **N’oublie pas de remplacer** l’URL locale (`http://localhost:8000`) par l’URL publique de l'API déployée:  
`https://movie-backend-x8iq.onrender.com`

Voici quelques exemples mis à jour :

---

##### Lister les films

```python
import httpx

response = httpx.get("https://movie-backend-x8iq.onrender.com/movies", params={"limit": 5})
print(response.json())
```

---

##### Obtenir un film spécifique

```python
movie_id = 1
response = httpx.get(f"https://movie-backend-x8iq.onrender.com/movies/{movie_id}")
print(response.json())
```

---

##### Rechercher les évaluations pour un film donné

```python
response = httpx.get("https://movie-backend-x8iq.onrender.com/ratings", params={"movie_id": 1})
print(response.json())
```

---

##### Récupérer un tag spécifique

```python
response = httpx.get("https://movie-backend-x8iq.onrender.com/tags/5/1/superbe")
print(response.json())
```

---

##### Obtenir des statistiques globales

```python
response = httpx.get("https://movie-backend-x8iq.onrender.com/analytics")
print(response.json())
```

---

#### C’est terminé !

On a déployé une API FastAPI gratuitement en ligne accessible depuis n’importe quel appareil connecté à Internet.

---

## Déploiement de l'API dans un conteneur Docker

### Qu’est-ce que Docker ?

Docker est un outil **puissant et très populaire** dans l’écosystème tech moderne. Il permet d’**emballer une application et toutes ses dépendances** dans un environnement léger, appelé **conteneur** (*container*), qui peut ensuite être exécuté **partout de la même façon** : sur l'ordinateur, sur un serveur cloud, ou sur une machine distante.

> En résumé : Docker permet de dire **"ça marche chez moi" et que ça marche aussi chez tout le monde**.

---

### Pourquoi Docker est-il si important ?

- **Standardisation** : On évite les problèmes de compatibilité entre différents environnements.
- **Portabilité** : Le même conteneur peut être exécuté localement, sur AWS, Azure, GCP, etc.
- **Isolation** : Chaque conteneur fonctionne de manière indépendante, sans conflit avec les autres applications.
- **Gain de temps** : Fini les longues installations manuelles de dépendances.

---

### Installer Docker

On peut installer Docker en suivant les instructions officielles en fonction du système d’exploitation (Windows, macOS ou Linux) : https://docs.docker.com/get-docker/


---

### Vérifier que Docker est bien installé

Une fois l’installation terminée, dans le terminal, on tape la commande suivante :

```bash
docker --version
```

Si Docker est bien installé, on voit s’afficher la version actuelle.

---

### Étapes du déploiement avec Docker

Voici les **3 grandes étapes** suivi pour créer une version Dockerisée de l'API :

---

#### 1️- Créer un fichier `Dockerfile`

Ce fichier décrit **comment construire l’image Docker** à partir du code de l'API :  
- Quelle image de base utiliser (Python)
- Comment installer les dépendances
- Quelle commande lancer pour démarrer l’API

On crée un fichier `Dockerfile` dans le dossier api/ et écrit ceci dedans :

```dockerfile
# Utilise une image légère de Python 3.13 comme base
FROM python:3.13-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier des dépendances dans le conteneur
COPY requirements.txt .

# Installe les dépendances Python sans mise en cache
RUN pip install --no-cache-dir --upgrade -r requirements.txt 

# Copie tous les fichiers .py et le fichier .db dans le conteneur
COPY . .

# Lance le serveur Uvicorn pour exécuter l'API FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

```

Un **Dockerfile** est un fichier texte qui explique à Docker **comment construire une image** contenant l'application (ici, l'API FastAPI).

C’est comme **une recette de cuisine** : chaque ligne du fichier indique une étape pour préparer l’environnement nécessaire à l'application.

---

```Dockerfile
FROM python:3.13-slim
```
- Cette ligne dit à Docker de **partir d’une image Python légère** (basée sur Python 3.13). C’est comme une base toute prête qui contient Python mais très peu de choses en plus (d’où le mot *slim*).

---

```Dockerfile
WORKDIR /app
```
- On dit à Docker de **travailler dans le dossier `/app`** dans le conteneur. Tous les fichiers qu’on ajoutera et toutes les commandes qu’on exécutera après se feront dans ce dossier.

---

```Dockerfile
COPY requirements.txt .
```
- On **copie le fichier `requirements.txt`** du projet local vers le dossier `/app` dans le conteneur. Ce fichier contient la liste des bibliothèques Python nécessaires (comme `fastapi` et `sqlalchemy`).

---

```Dockerfile
RUN pip install --no-cache-dir --upgrade -r requirements.txt 
```
- On **installe toutes les bibliothèques Python** listées dans `requirements.txt`.  
L’option `--no-cache-dir` évite de stocker les fichiers d’installation (pour que le conteneur soit plus léger).

---

```Dockerfile
COPY . .
```
- On **copie tous les fichiers de ton dossier `api/`** vers le dossier `/app` du conteneur. Cela inclut tes fichiers `.py` (comme `main.py`, `crud.py`, etc.) et la base de données `.db`.

---

```Dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```
- C’est la **commande de démarrage de l’API**.  
On utilise `uvicorn`, le serveur qui exécute FastAPI. Il va chercher l’application dans `main.py`, dans la variable `app`, et la rend accessible depuis l’extérieur (grâce à `--host 0.0.0.0`).

---

Avec ce Dockerfile, on peut créer une **image Docker contenant l'API** prête à être exécutée.

Mais avant de construire une image Docker, il est **essentiel** de créer un fichier `.dockerignore`.

---

Voici un exemple **simple et efficace** de `.dockerignore` pour le projet FastAPI :

```dockerignore
# Fichiers Python compilés
__pycache__/
*.pyc
*.pyo

# Fichiers de logs
*.log

# Fichiers de configuration d’environnement local
.env

# Répertoire Git
.git
.gitignore

# Fichiers système
.DS_Store

# Cache pip ou venv
.venv/
venv/
pip-wheel-metadata/
```

---

**Pourquoi un `.dockerignore` est important ?**

Le fichier `.dockerignore` fonctionne **exactement comme un `.gitignore`**, mais pour **Docker**. Il indique quels fichiers **ne doivent pas être copiés** dans l’image Docker au moment de la construction.

**Sans `.dockerignore`** :
Docker copierait **tout le dossier** (y compris `.git`, `.venv`, fichiers inutiles, etc.), ce qui rend l’image :
- plus **lourde** 
- plus **lente à construire** 
- plus **vulnérable** (ex. : si on oublie un `.env` avec une clé secrète)

---

**En résumé**

Le fichier `.dockerignore` :
- **Réduit la taille** de l’image Docker
- **Accélère le build**
- **Protège les données sensibles**
- Évite de copier du bazar inutile

---

#### 2️- Construire une image Docker

On utilise la commande :

```bash
docker build -t img_api_films .
```

Cette commande sert à **construire une image Docker** à partir du `Dockerfile`. Voyons cette commande en détail :

---

| Élément | Explication |
|--------|-------------|
| `docker` | Lance l’outil Docker depuis ton terminal |
| `build` | Indique qu'on veut **construire une image** Docker |
| `-t img_api_films` | Donner un **nom (tag)** à l'image, ici `img_api_films` |
| `.` | Spécifie le **contexte de construction**, ici le dossier courant (`.`) où se trouve le `Dockerfile` |

---

**Concrètement, que fait Docker ici ?**
1. Il lit le `Dockerfile`
2. Il suit **chaque instruction** (`FROM`, `COPY`, `RUN`, `CMD`, etc.)
3. Il crée une **image Docker complète**, prête à être lancée
4. Il la nomme `img_api_films` pour qu'on puisse la réutiliser ensuite

---

**On peut voir l’image créée avec** :
```bash
docker images
```
Exemple de résultat :

```bash
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
img_api_films                 latest    fb50d410d93f   4 days ago      263MB
```

---

En résumé, cette commande permet de transformer le code et les dépendances en **une image Docker réutilisable**. C’est comme faire une boîte scellée qui contient l'API, prête à être envoyée ou exécutée **n’importe où** !

---

#### 3️- Lancer un conteneur

Une fois l’image créée, on peut **démarrer l’API dans un conteneur** avec :

```bash
docker run -d -p 80:80 --name container_api_films img_api_films
```

**Décomposons la commande** :

- `docker run` : Lance un conteneur basé sur une image existante.

- `-d` : Le mode **détaché**, qui permet d'exécuter le conteneur en arrière-plan.

- `-p 80:80` : Fait correspondre le port **80 du conteneur** au port **80 de la machine locale**. Cela signifie que l'API sera accessible via `http://localhost:80`.

- `--name container_api_films` : Cette option permet de donner un nom personnalisé au conteneur. Dans cet exemple, le conteneur est nommé `container_api_films`. Cela peut être utile pour identifier facilement le conteneur dans une liste ou pour l'arrêter et le gérer plus facilement.

- `img_api_films` : Le nom de l'image Docker construit.

**Vérification** :

On peut maintenant vérifier que le conteneur fonctionne en accédant à `http://localhost:80` et refaire des tests des endpoins à travers l'interface Swagger : `http://localhost/docs`

Pour vérifier les conteneurs en cours d'exécution, on peut aussi utiliser la commande :

```bash
docker ps
```
Voici un exemple de résultat de cette commande :

```bash
CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS             NAMES
5ca9b17d9b05   img_api_films   "uvicorn main:app --…"   6 minutes ago   Up 6 minutes  0.0.0.0:80->80/tcp container_api_films
```

Cela permet de voir le nom du conteneur dans la liste.

### Quelques commandes utiles pour nettoyer l'environnement Docker

Voici quelques commandes utiles pour nettoyer l'environnement Docker après avoir testé l'application :

1. **Arrêter un conteneur en cours d'exécution**
   Pour arrêter un conteneur qui fonctionne actuellement, on utilise la commande suivante (remplace `container_api_films` par le nom du conteneur) :

   ```bash
   docker stop container_api_films
   ```

2. **Supprimer un conteneur**
   Après avoir arrêté le conteneur, on peut le supprimer avec la commande suivante :

   ```bash
   docker rm container_api_films
   ```

   Cela supprimera le conteneur spécifique.

3. **Supprimer une image Docker**
   Pour supprimer une image Docker, on utilise cette commande en remplaçant `img_api_films` par le nom de l'image :

   ```bash
   docker rmi img_api_films
   ```

   Etre rassurer d'abord que tous les conteneurs basés sur l'image sont arrêtés et supprimés avant de la supprimer.

4. **Supprimer toutes les images**
   Pour supprimer toutes les images Docker présentes sur le système (attention, cela supprimera toutes les images et doivent etre reconstruire plus tard si nécessaire) :

   ```bash
   docker rmi $(docker images -q)
   ```

   Cette commande supprimera toutes les images présentes sur le système.

5. **Supprimer tous les conteneurs (arrêtés et en cours d'exécution)**
   Pour supprimer tous les conteneurs (en cours d'exécution ou arrêtés), on utilise la commande suivante :

   ```bash
   docker rm $(docker ps -a -q)
   ```

   Cela supprimera tous les conteneurs, qu'ils soient actifs ou non.

6. **Supprimer tous les conteneurs et images**
   Si on souhaite tout supprimer en une seule commande (tous les conteneurs et toutes les images), on peut combiner les deux commandes comme suit :

   ```bash
   docker system prune -a
   ```

   Cela supprimera tous les conteneurs, images et volumes inutilisés. C'est une commande puissante à utiliser avec précaution, car elle supprimera toutes les ressources non utilisées par Docker.

**En résumé** :
Après avoir terminé les tests ou le déploiement, il est important de nettoyer l'environnement Docker (au cas où on ne comptes plus utiliser les images/conteneurs créés) pour libérer de l'espace et éviter l'accumulation de ressources inutiles. Les commandes ci-dessus  permettent de stopper et supprimer les conteneurs et les images Docker.


## Création d'un kit de développement logiciel (*Software development kit* ou SDK) pour l'API


### Qu'est-ce qu'un SDK et pourquoi est-il important ?

Un **Software Development Kit** (SDK) est un ensemble d'outils, de bibliothèques, de documentation et d'exemples de code qui permettent aux développeurs de facilement intégrer, étendre ou interagir avec une application, un service ou une API. Dans le contexte de ce projet, le SDK sera un package Python qui fournira une interface simple et intuitive pour interagir avec l'API MovieLens.

Les bénéfices de la création d'un SDK pour l'API sont nombreux :
- **Faciliter l'intégration** : Les utilisateurs n'ont pas besoin de comprendre les détails techniques de l'API, comme l'envoi de requêtes HTTP ou la gestion des réponses. Le SDK simplifie ces étapes.
- **Accélérer le développement** : En fournissant des fonctions prédéfinies pour effectuer des actions courantes, le SDK permet aux utilisateurs de gagner du temps.
- **Assurer la cohérence** : Un SDK bien conçu garantit que tous les utilisateurs interagiront avec l'API de manière uniforme et cohérente.
- **Support de la communauté** : En partageant un SDK via PyPI, il devient accessible à d'autres développeurs et analystes de données qui pourraient l'utiliser dans leurs projets.

### Pourquoi Python pour le SDK ?

Le choix de **Python** pour développer le SDK est particulièrement adapté au contexte de ce projet, car la plupart des utilisateurs finaux de l'API seront des **data analysts** et **data scientists**, des professionnels qui utilisent principalement Python dans leur travail quotidien. Python est largement adopté dans le domaine de l'analyse de données, grâce à sa simplicité et à l'écosystème riche de bibliothèques pour le traitement des données, telles que **pandas**, **NumPy**, **scikit-learn**, etc.

En publiant ce SDK sous forme de package Python sur **PyPI** (Python Package Index), on permet aux utilisateurs de facilement l'installer avec une simple commande `pip install`. Cela rend l'intégration de l'API dans leurs projets Python rapide et transparente, tout en maximisant la compatibilité avec leurs outils existants.

En résumé, un SDK bien conçu permet de rendre l'API accessible et facile à utiliser pour les professionnels de l'analyse de données, tout en utilisant un langage et des outils avec lesquels ils sont déjà familiers.

### Etapes de création du Package

#### Structure du dossier du package

Pour commencer, à partir de la racine du répertoire de travail, on exécute successivement les commandes suivantes pour structurer le répertoire du package :

```bash
mkdir sdk
cd sdk
touch pyproject.toml
mkdir src
mkdir src/films_sdk_sbre
touch __init__.py
touch film_client.py
touch film_config.py
mkdir schemas
touch schemas/__init__.py
touch schemas/schemas.py
```

Exécuter la commande ci-dessous pour visualiser la structure du dossier sdk/ :

```bash
tree --prune -I 'build|*.egg-info|__pycache__'
```

On obtient cette structure pour le dossier sdk/ :

```
.
├── pyproject.toml
├── src
│   └── films_sdk_sbre
│       ├── __init__.py
│       ├── film_client.py
│       ├── film_config.py
│       └── schemas
│           ├── __init__.py
│           └── schemas.py
└── test_sdk.py
```

#### Fichier `sdk/pyproject.toml`

Le fichier `pyproject.toml` est un fichier de configuration pour les projets Python modernes. Il est utilisé pour décrire les métadonnées du projet, ses dépendances, et les outils nécessaires à sa construction et à son packaging. Ce fichier remplace progressivement des fichiers comme `setup.py` et `requirements.txt` pour la configuration des projets Python.

```toml
[build-system]
requires = ["setuptools>=80.9.0"]
build-backend = "setuptools.build_meta"

[project]
name = "films_sdk_sbre"
version = "0.0.1"
authors = [
  { name="[BELLO Soboure]" },
]
description = "Software Development Kit (SDK) for MovieLens API"
requires-python = ">=3.12"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
       'httpx>=0.28.1',
       'pydantic>=2.11.2',
       'backoff>=2.2.1',
       'python-dotenv',
]
```

***Explication de ce fichier `pyproject.toml`***

- **[build-system]** : Cette section décrit comment le projet doit être construit. Il est nécessaire d'indiquer `setuptools` comme backend de construction et la version minimale requise de `setuptools`.
- **[project]** : C'est ici que se trouvent les métadonnées du projet :
  - `name` : Le nom du projet, dans ce cas "films_sdk_sbre".
  - `version` : La version actuelle du SDK.
  - `authors` : Les informations sur les auteurs du projet, incluant potentiellement un email.
  - `description` : Une brève description du SDK.
  - `requires-python` : La version minimale de Python requise pour utiliser le SDK.
  - `classifiers` : Des informations sur le statut du projet (par exemple, si c'est un projet alpha) et des détails techniques sur la compatibilité.
  - `dependencies` : La liste des dépendances Python nécessaires à l'exécution du SDK.

Le fichier `pyproject.toml` est essentiel pour gérer le projet Python de manière moderne et cohérente, et il est requis pour publier SDK sur **PyPI**.

---

#### Fichier `sdk/src/films_sdk_sbre/film_config.py`

```python
import os
from dotenv import load_dotenv

load_dotenv()

class MovieConfig:
    """Classe de configuration contenant des arguments pour le client SDK.

    Contient la configuration de l'URL de base et du backoff progressif.
    """

    movie_base_url: str
    movie_backoff: bool
    movie_backoff_max_time: int

    def __init__(
        self,
        movie_base_url: str = None,
        backoff: bool = True,
        backoff_max_time: int = 30,
    ):
        """Constructeur pour la classe de configuration.

        Contient des valeurs d'initialisation pour écraser les valeurs par défaut.

        Args:
        movie_base_url (optional):
            L'URL de base à utiliser pour tous les appels d'API. Transmettez-la ou définissez-la dans une variable d'environnement.
        movie_backoff:
            Un booléen qui détermine si le SDK doit réessayer l'appel en utilisant un backoff lorsque des erreurs se produisent.
        movie_backoff_max_time:
            Le nombre maximal de secondes pendant lesquelles le SDK doit continuer à essayer un appel API avant de s'arrêter.
        """

        self.movie_base_url = movie_base_url or os.getenv("MOVIE_API_BASE_URL")
        print(f"MOVIE_API_BASE_URL in MovieConfig init: {self.movie_base_url}")  

        if not self.movie_base_url:
            raise ValueError("L'URL de base est requise. Définissez la variable d'environnement MOVIE_API_BASE_URL.")

        self.movie_backoff = backoff
        self.movie_backoff_max_time = backoff_max_time

    def __str__(self):
        """Fonction Stringify pour renvoyer le contenu de l'objet de configuration pour la journalisation"""
        return f"{self.movie_base_url} {self.movie_backoff} {self.movie_backoff_max_time}"
```

Le fichier `film_config.py` joue un rôle fondamental dans le SDK en centralisant la **configuration de base** nécessaire pour que le client puisse fonctionner correctement. Voici une **revue complète et une explication simplifiée** de ce fichier :

---

##### **Objectif du fichier `film_config.py`**

Ce fichier définit une classe `MovieConfig` utilisée pour **configurer le SDK** avant de faire des appels à l’API.  
Il permet de définir :

- l’URL de base de l’API,
- si on souhaite appliquer un mécanisme de **backoff** (réessais automatiques en cas d’échec),
- et combien de temps maximum on doit réessayer.

Il permet aussi de charger la configuration à partir d’un **fichier `.env`**, ce qui est une très bonne pratique pour éviter de stocker des données sensibles ou spécifiques à un environnement directement dans le code.

---

##### **Détail du contenu**

```python
from dotenv import load_dotenv
import os

load_dotenv()
```
Charge les variables d’environnement depuis un fichier `.env` (utile pour ne pas écrire les secrets ou URL directement dans le code).  
Par exemple, tu peux définir ceci dans un fichier `.env` :
```env
MOVIE_API_BASE_URL=http://localhost:8000
```

---

###### Classe `MovieConfig`

```python
class MovieConfig:
    ...
```

Cette classe sert à **centraliser la configuration du SDK**.

---

###### Le constructeur `__init__`

Il permet d’instancier l'objet de configuration avec :
- une `movie_base_url` : si elle n’est pas passée, on la récupère depuis une variable d’environnement.
- un `backoff` : booléen qui permet de dire si on veut réessayer automatiquement en cas d’erreur.
- `backoff_max_time` : durée maximale (en secondes) pendant laquelle on veut réessayer.

```python
self.movie_base_url = movie_base_url or os.getenv("MOVIE_API_BASE_URL")
```
Cette ligne dit : « Si `movie_base_url` est fourni, je l’utilise. Sinon, je vais chercher dans les variables d’environnement. »

Et si `movie_base_url` est toujours vide, on déclenche une erreur claire :

```python
if not self.movie_base_url:
    raise ValueError("L'URL de base est requise...")
```

Le `print()` temporaire peut aider au débogage (mais on pourra le supprimer ou le logger proprement plus tard).

---

###### Fonction `__str__`

```python
def __str__(self):
    return f"{self.movie_base_url} {self.movie_backoff} {self.movie_backoff_max_time}"
```

Permet d’afficher la config facilement, par exemple dans un `print(MovieConfig())`.

---

##### En résumé

| Élément               | Rôle                                                                 |
|----------------------|----------------------------------------------------------------------|
| `load_dotenv()`       | Charge les variables d’environnement depuis un fichier `.env`        |
| `movie_base_url`      | URL de base de l’API (obligatoire)                                   |
| `movie_backoff`       | Active/désactive les tentatives automatiques en cas d’erreur réseau  |
| `movie_backoff_max_time` | Définit la durée maximale du backoff en secondes                 |
| `__str__`              | Sert à afficher le contenu de la config de manière lisible           |

Ce fichier est donc la **brique de configuration principale du SDK**.

#### Fichier `sdk/src/films_sdk_sbre/schemas/schemas.py`

**Code** : C'est le mème code que celui du fichier `api/schemas.py`.

Ce fichier contient les **schémas de données Pydantic** utilisés dans l'API FastAPI.

Ce sont **des classes Python qui définissent la forme et le type des objets JSON échangés avec l’API** : films, notes, tags, etc.

Le fait de les utilise encore dans le SDK ?** **garantit la cohérence entre ce que l’API renvoie et ce que le SDK attend**.

Dans le SDK, ces classes Pydantic servent à :

1. **Valider les réponses JSON de l’API**

Exemple :

```python
response = httpx.get(url)
return MovieDetailed(**response.json())
```

➡️ Cette ligne transforme le JSON de l’API en un **objet Python fort typé** (`MovieDetailed`)  
➡️ Si les données ne correspondent pas, Pydantic lève une erreur immédiatement : sécurité.

---

2. **Offrir une expérience Pythonic**

On peut faire :

```python
movie = client.get_movie(123)
print(movie.title)
print(movie.genres.split("|"))
```

Plutôt que :

```python
data = response.json()
print(data["title"])
```

C’est plus sûr, plus lisible, plus robuste.

---

3. **Mutualiser le code (DRY)**

Tu **réutilises les mêmes classes Pydantic que pour l’API**, donc :
- Pas besoin de redéfinir les modèles deux fois.
- Moins de risques d’incohérences.
- Maintenance simplifiée.

---

#### Fichier `sdk/src/films_sdk_sbre/__init__.py`

Dans un package Python (comme `films_sdk_sbre` ici), le fichier `__init__.py` permet de **définir ce qui est exposé lorsque quelqu’un importe le package**.

Concrètement, avec ce contenu :

```python
from .film_client import MovieClient
from .film_config import MovieConfig
```

Qui permet à l’utilisateur final de faire :

```python
from films_sdk_sbre import MovieClient, MovieConfig
```

Au lieu de :

```python
from films_sdk_sbre.film_client import MovieClient
from films_sdk_sbre.film_config import MovieConfig
```

---

**Pourquoi c’est utile ?**

1. **Simplifie l'import pour l'utilisateur final**

Un SDK bien conçu doit être **facile à importer et à utiliser**.

On veut que les gens fassent :

```python
from films_sdk_sbre import MovieClient
```

Pas :

```python
from films_sdk_sbre.film_client import MovieClient
```

C’est plus lisible, plus direct.

---

2. **Masque la structure interne**

Avec l’import centralisé dans `__init__.py`, on **masque les sous-modules internes** à l’utilisateur.  
Cela permet de :
- Garder une API publique propre.
- Pouvoir modifier la structure interne du package **sans casser les imports** pour l’utilisateur.

---



**En résumé**

| Élément                            | Rôle                                                                 |
|-----------------------------------|----------------------------------------------------------------------|
| `__init__.py`                     | Déclare les composants "publics" du package                         |
| `from .film_client import ...`   | Rends directement accessibles ces classes depuis `films_sdk_sbre`         |
| Avantage pour l'utilisateur       | Importation simple et intuitive (`from films_sdk_sbre import MovieClient`)|

---

#### Fichier `sdk/src/films_sdk_sbre/schemas/__init__.py`

Le fichier `schemas/__init__.py` avec :

```python
from .schemas import *
```

a un objectif **simple mais important** : rendre toutes les classes définies dans `schemas.py` **accessibles directement** depuis le sous-module `schemas`.

---

#### Fichier `film_client.py` 

```python
import httpx
from typing import Optional, List

from .schemas import MovieSimple, MovieDetailed, RatingSimple, TagSimple, LinkSimple, AnalyticsResponse
from .film_config import MovieConfig


class MovieClient:
    def __init__(self, config: Optional[MovieConfig] = None):
        self.config = config or MovieConfig()
        self.movie_base_url = self.config.movie_base_url

    def health_check(self) -> dict:
        url = f"{self.movie_base_url}/"
        response = httpx.get(url)
        response.raise_for_status()
        return response.json()

    def get_movie(self, movie_id: int) -> MovieDetailed:
        url = f"{self.movie_base_url}/movies/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return MovieDetailed(**response.json())

    def list_movies(self, skip: int = 0, limit: int = 100, title: Optional[str] = None, genre: Optional[str] = None) -> List[MovieSimple]:
        url = f"{self.movie_base_url}/movies"
        params = {"skip": skip, "limit": limit}
        if title:
            params["title"] = title
        if genre:
            params["genre"] = genre
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return [MovieSimple(**movie) for movie in response.json()]

    def get_rating(self, user_id: int, movie_id: int) -> RatingSimple:
        url = f"{self.movie_base_url}/ratings/{user_id}/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return RatingSimple(**response.json())

    def list_ratings(self, skip: int = 0, limit: int = 100, movie_id: Optional[int] = None, user_id: Optional[int] = None, min_rating: Optional[float] = None) -> List[RatingSimple]:
        url = f"{self.movie_base_url}/ratings"
        params = {"skip": skip, "limit": limit}
        if movie_id:
            params["movie_id"] = movie_id
        if user_id:
            params["user_id"] = user_id
        if min_rating:
            params["min_rating"] = min_rating
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return [RatingSimple(**rating) for rating in response.json()]

    def get_tag(self, user_id: int, movie_id: int, tag_text: str) -> TagSimple:
        url = f"{self.movie_base_url}/tags/{user_id}/{movie_id}/{tag_text}"
        response = httpx.get(url)
        response.raise_for_status()
        return TagSimple(**response.json())

    def list_tags(self, skip: int = 0, limit: int = 100, movie_id: Optional[int] = None, user_id: Optional[int] = None) -> List[TagSimple]:
        url = f"{self.movie_base_url}/tags"
        params = {"skip": skip, "limit": limit}
        if movie_id:
            params["movie_id"] = movie_id
        if user_id:
            params["user_id"] = user_id
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return [TagSimple(**tag) for tag in response.json()]

    def get_link(self, movie_id: int) -> LinkSimple:
        url = f"{self.movie_base_url}/links/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return LinkSimple(**response.json())

    def list_links(self, skip: int = 0, limit: int = 100) -> List[LinkSimple]:
        url = f"{self.movie_base_url}/links"
        params = {"skip": skip, "limit": limit}
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return [LinkSimple(**link) for link in response.json()]

    def get_analytics(self) -> AnalyticsResponse:
        url = f"{self.movie_base_url}/analytics"
        response = httpx.get(url)
        response.raise_for_status()
        return AnalyticsResponse(**response.json())
```

Le fichier `film_client.py` est **le cœur du SDK**. Il encapsule toutes les **fonctions de communication avec l'API MovieLens** et fournit une interface Python simple, propre et typée pour les utilisateurs (data analysts, data scientists, développeurs, etc.).

Ce fichier définit la **classe `MovieClient`**, qui agit comme **le client principal pour interagir avec l’API MovieLens**. Elle permet à l'utilisateur final de :

- récupérer des films, des notes, des tags, des liens,
- faire des recherches (filtrées par titre, genre, etc.),
- accéder à des données analytiques,
- vérifier que l’API est opérationnelle (`health_check`).

Le but est d’avoir une **expérience Python “clé en main”** pour appeler l’API sans écrire de requêtes HTTP brutes.

---

Voici la Structure et fonctionnement de `film_client.py` :

1. **Initialisation du client**

```python
def __init__(self, config: Optional[MovieConfig] = None):
    self.config = config or MovieConfig()
    self.movie_base_url = self.config.movie_base_url
```

Si l’utilisateur fournit une configuration (`MovieConfig`), on l’utilise.  
Sinon, on en crée une par défaut (avec lecture `.env` automatique).  
Puis on récupère l’URL de base de l’API.

---

2. **Méthode `health_check()`**

Vérifie que l’API est accessible (utile avant d’enchaîner les requêtes).

---

3. **Méthodes pour les films**

- `get_movie(movie_id)` : récupère un film avec tous ses détails (`MovieDetailed`)
- `list_movies(...)` : permet de récupérer une **liste paginée** de films, avec filtres `title` et `genre`

Très utile dans un notebook pour faire une recherche rapide :

```python
client.list_movies(title="Matrix", genre="Action")
```

---

4. **Méthodes pour les notes (ratings)**

- `get_rating(user_id, movie_id)` : récupère la note d’un utilisateur pour un film.
- `list_ratings(...)` : liste paginée des notes, avec filtres `movie_id`, `user_id`, ou `min_rating`.

---

5. **Méthodes pour les tags**

- `get_tag(...)` : un tag spécifique pour un film par un utilisateur.
- `list_tags(...)` : liste paginée des tags avec possibilité de filtrer.

---

6. **Méthodes pour les liens (vers IMDb, TMDb)**

- `get_link(movie_id)` : récupère les IDs externes du film.
- `list_links()` : récupère tous les liens disponibles.

---

7. **Méthode d’analytics**

```python
def get_analytics(self) -> AnalyticsResponse:
```

Récupère un rapport agrégé (statistiques globales comme nombre de films, de notes, etc.).

---

#### Installation du package dans l'environnement de développement


Au niveau du terminal, s'assure d'être dans sdk/ et taper cette commande :

```bash
pip install -e .
```

Cette commande est très utilisée pendant le **développement d’un package Python** (comme le SDK `films_sdk_sbre`). Voici une explication simple et claire pour bien comprendre :

---

**Que fait cette commande ?**

##### `pip install`  
Installe un package Python dans l'environnement (comme on le fait avec `pip install requests`).

##### `-e` = `--editable`  
Le flag `-e` signifie **"editable mode"** (mode modifiable). Cela veut dire que **le package n’est pas copié** dans le dossier `site-packages`, mais un **lien symbolique** est créé vers le dossier local (`.`).

##### `.`  
C’est le chemin vers le **répertoire courant**, donc ici le dossier `sdk/`, qui contient le`pyproject.toml`.

---

**Pourquoi c’est utile pour le SDK ?**

Quand on développe le SDK, il est encore en évolution. Grâce à l’installation en mode *editable* :

- On peut modifier les fichiers source (ex : `film_client.py`, `schemas.py`, etc.)
- Et **voir les changements immédiatement** sans devoir réinstaller le package à chaque fois.

---

Pour résumer, en exécutant :

```bash
pip install -e .
```

On rends le package `films_sdk_sbre` utilisable **partout dans le projet** (ou dans des notebooks, scripts, etc.) comme s’il était installé normalement, **mais on peut continuer à modifier le code source** en temps réel.


| Élément                 | Description                                                         |
|-------------------------|---------------------------------------------------------------------|
| `pip install`           | Installe un package                                                 |
| `-e` ou `--editable`    | Crée un lien vers le code source, permet de le modifier en direct  |
| `.`                     | Répertoire courant contenant `pyproject.toml`                      |
| Avantage                | Pas besoin de réinstaller après chaque changement                   |

---

#### Fichier `sdk/test_sdk.py`

```python
from films_sdk_sbre import MovieClient, MovieConfig

# Initialisation du client avec l'URL de l'API
config = MovieConfig(movie_base_url="https://movie-backend-x8iq.onrender.com")
client = MovieClient(config=config)

# 1. Health check
print("Health check:")
print(client.health_check())

# 2. Récupérer un film par ID
print("\n Movie ID 1:")
movie = client.get_movie(1)
print(movie)
print(type(movie))

# 3. Lister les films (premiers 5)
print("\n List of movies:")
movies = client.list_movies(limit=5)
print(type(movies))
for m in movies:
    print(m)
    print(type(m))

# 4. Récupérer un rating spécifique
print("\n Rating for user 1 and movie 1:")
rating = client.get_rating(user_id=1, movie_id=1)
print(rating)
print(type(rating))

# 5. Lien du film
print("\n Link for movie ID 1:")
link = client.get_link(movie_id=1)
print(link)
print(type(link))


# 6. Analytics
print("\n Analytics:")
analytics = client.get_analytics()
print(analytics)
print(type(analytics))
```

Ce fichier joue le rôle de **script de test manuel** pour le SDK. Il sert à **valider que le SDK fonctionne correctement** en appelant les différentes méthodes fournies par la classe `MovieClient`.

#### Mise à jour du fichier `sdk/src/films_sdk_sbre/movie_client.py`

```python
import httpx
from typing import Optional, List, Literal, Union

from .schemas import MovieSimple, MovieDetailed, RatingSimple, TagSimple, LinkSimple, AnalyticsResponse
from .film_config import MovieConfig

import pandas as pd


class MovieClient:
    def __init__(self, config: Optional[MovieConfig] = None):
        self.config = config or MovieConfig()
        self.movie_base_url = self.config.movie_base_url

    def _format_output(self, data, model, output_format: Literal["pydantic", "dict", "pandas"]):
        if output_format == "pydantic":
            return [model(**item) for item in data]
        elif output_format == "dict":
            return data
        elif output_format == "pandas":
            import pandas as pd
            return pd.DataFrame(data)
        else:
            raise ValueError("Invalid output_format. Choose from 'pydantic', 'dict', or 'pandas'.")

    def health_check(self) -> dict:
        url = f"{self.movie_base_url}/"
        response = httpx.get(url)
        response.raise_for_status()
        return response.json()

    def get_movie(self, movie_id: int) -> MovieDetailed:
        url = f"{self.movie_base_url}/movies/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return MovieDetailed(**response.json())

    def list_movies(
        self,
        skip: int = 0,
        limit: int = 100,
        title: Optional[str] = None,
        genre: Optional[str] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[MovieSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.movie_base_url}/movies"
        params = {"skip": skip, "limit": limit}
        if title:
            params["title"] = title
        if genre:
            params["genre"] = genre
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), MovieSimple, output_format)

    def get_rating(self, user_id: int, movie_id: int) -> RatingSimple:
        url = f"{self.movie_base_url}/ratings/{user_id}/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return RatingSimple(**response.json())

    def list_ratings(
        self,
        skip: int = 0,
        limit: int = 100,
        movie_id: Optional[int] = None,
        user_id: Optional[int] = None,
        min_rating: Optional[float] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[RatingSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.movie_base_url}/ratings"
        params = {"skip": skip, "limit": limit}
        if movie_id:
            params["movie_id"] = movie_id
        if user_id:
            params["user_id"] = user_id
        if min_rating:
            params["min_rating"] = min_rating
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), RatingSimple, output_format)

    def get_tag(self, user_id: int, movie_id: int, tag_text: str) -> TagSimple:
        url = f"{self.movie_base_url}/tags/{user_id}/{movie_id}/{tag_text}"
        response = httpx.get(url)
        response.raise_for_status()
        return TagSimple(**response.json())

    def list_tags(
        self,
        skip: int = 0,
        limit: int = 100,
        movie_id: Optional[int] = None,
        user_id: Optional[int] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[TagSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.movie_base_url}/tags"
        params = {"skip": skip, "limit": limit}
        if movie_id:
            params["movie_id"] = movie_id
        if user_id:
            params["user_id"] = user_id
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), TagSimple, output_format)

    def get_link(self, movie_id: int) -> LinkSimple:
        url = f"{self.movie_base_url}/links/{movie_id}"
        response = httpx.get(url)
        response.raise_for_status()
        return LinkSimple(**response.json())

    def list_links(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[LinkSimple], List[dict], "pd.DataFrame"]:
        url = f"{self.movie_base_url}/links"
        params = {"skip": skip, "limit": limit}
        response = httpx.get(url, params=params)
        response.raise_for_status()
        return self._format_output(response.json(), LinkSimple, output_format)

    def get_analytics(self) -> AnalyticsResponse:
        url = f"{self.movie_base_url}/analytics"
        response = httpx.get(url)
        response.raise_for_status()
        return AnalyticsResponse(**response.json())

```

Voici une explication détaillée des changements apportés au fichier `film_client.py` pour offrir deux modes de sortie :

L'objectif principal de ces changements est de rendre l'API plus flexible pour les différents types d'utilisateurs. En particulier, on souhaite faciliter l'interaction avec l'API pour les **Data Analysts** et **Data Scientists**, qui sont habitués à utiliser des structures comme des **pandas DataFrame** ou des **dictionnaires** pour leurs analyses.

##### 1. Retour par défaut des objets Pydantic

Dans le code, on continue de retourner des objets basés sur **Pydantic**, comme `MovieDetailed`, `RatingSimple`, etc., dans la plupart des cas. C'est un choix courant pour plusieurs raisons :
- **Clarté** et **Typage** : Pydantic garantit que les données respectent bien les modèles, ce qui améliore la lisibilité et l'autocomplétion dans les IDE.
- **Validation** : Les objets Pydantic offrent une validation automatique des données en fonction du modèle, ce qui aide à garantir que les données reçues sont bien structurées.
- **Pratique pour le backend** : Les objets Pydantic sont particulièrement utiles pour les systèmes qui nécessitent des objets structurés, comme pour les intégrations avec d'autres APIs ou services backend.

##### 2. Retour de dictionnaires ou pandas DataFrame selon un format spécifié

Pour rendre l'API plus accessible aux utilisateurs de **pandas** et des **Data Analysts/Data Scientists**, nous avons ajouté un paramètre `output_format` optionnel aux méthodes de notre client API. Ce paramètre permet de choisir le format de sortie des données en fonction des préférences de l'utilisateur. Les options sont :
- **"pydantic"** (par défaut) : Retourne les objets Pydantic (modèles structurés).
- **"dict"** : Retourne les données sous forme de dictionnaires Python natifs. Cela peut être plus pratique pour ceux qui souhaitent manipuler des données sans avoir à traiter les objets Pydantic.
- **"pandas"** : Retourne un **DataFrame pandas**, ce qui est très pratique pour les Data Scientists et Analystes qui travaillent directement avec des tableaux de données.

##### 3. La méthode `_format_output`

Cette méthode est utilisée pour formater la sortie en fonction de l'option `output_format` choisie. Elle prend en entrée les données brutes reçues de l'API (`data`), le modèle Pydantic (`model`) et le format de sortie demandé (`output_format`). Elle décide ensuite quel type d'objet retourner en fonction de la valeur de `output_format` :
- Si le format est `"pydantic"`, il retourne des objets basés sur le modèle Pydantic.
- Si le format est `"dict"`, il retourne directement les données sous forme de dictionnaires.
- Si le format est `"pandas"`, il utilise pandas pour convertir les données en un DataFrame.

##### Exemple d'utilisation de `output_format` dans une méthode comme `list_movies`

Voici un rajout de code dans le fichier `sdk/test_sdk.py` :

```python
# 7. Tests avec option du choix de format de sortie
    # Par défaut : objets Pydantic
new_movies = client.list_movies(limit=5)
print(new_movies)
print(type(new_movies))

    # Format dictionnaire
new_movies_dicts = client.list_movies(limit=5, output_format="dict")
print(new_movies_dicts)
print(type(new_movies_dicts))

    # Format DataFrame
new_movies_df = client.list_movies(limit=5, output_format="pandas")
print(new_movies_df)
print(type(new_movies_df))
```

En conclusion, les principaux changements apportés au fichier `film_client.py` permettent de rendre l'API plus flexible et mieux adaptée aux **Data Analysts** et **Data Scientists**, tout en maintenant les avantages de Pydantic pour la validation et le typage. En offrant les trois options (`pydantic`, `dict`, `pandas`), nous pouvons facilement répondre aux besoins de différents types d'utilisateurs. Ces améliorations rendent l'API plus conviviale et plus facile à intégrer dans des pipelines de données Python typiques.

### Publication du SDK sur PyPI 

Publier un SDK sur [PyPI](https://pypi.org/) permet à n’importe quel utilisateur Python d’installer ton package avec un simple `pip install`. Voici comment faire, étape par étape.

---

#### 1- Créer un compte sur PyPI

Rendez-vous sur [https://pypi.org/account/register/](https://pypi.org/account/register/) et créer un compte gratuit. Ce compte te permettra de publier le SDK sur le Python Package Index (PyPI).

---

#### 2- Générer un token d’authentification

Une fois connecté au compte PyPI :

- Aller dans [Paramètres de compte PyPI](https://pypi.org/manage/account/)
- Cliquer sur **"Ajouter un jeton d’API"**
- Donner un nom (ex. : `token-sdk-movies`)
- Laisser les paramètres par défaut (accès global)
- Cliquer sur **"Créer"**
- **Copier immédiatement le token affiché** (il commence par `pypi-...`) : on ne pourra plus le revoir plus tard.

---

#### 3- Enregistrer le token dans un fichier de config

Dans un **nouveau terminal**, configurer le token pour que l’outil `twine` puisse l’utiliser automatiquement.

##### Sous Linux/macOS :

```bash
nano ~/.pypirc
```

Puis coller les lignes suivantes dans le fichier :

```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-le_token_ici
```

> Remplace `pypi-le_token_ici` par le vrai token copié.

✔️ Enregistrer avec `CTRL + O`, puis `Entrée`, et quitte avec `CTRL + X`.

---

##### Sous Windows :

1. Ouvrir **PowerShell** ou l’invite de commandes (cmd).

2. Créer un fichier de configuration `.pypirc` dans le répertoire utilisateur :

```powershell
notepad $env:USERPROFILE\.pypirc
```

3. Colle-y les lignes suivantes :

```ini
[distutils]
index-servers =
    pypi

[pypi]
username = __token__
password = pypi-le_token_ici
```

> Remplace `pypi-le_token_ici` par le token copié depuis PyPI.

4. Enregistrer et fermer le fichier.

---

Une fois ce fichier `.pypirc` en place, on pourra exécuter la commande `twine upload dist/*` sans avoir à saisir manuellement le token à chaque fois.

---

#### 4- Construire et publier le package

Retourne dans le terminal du projet (`sdk/`) et exécute les commandes suivantes :

```bash
pip install build twine
python3 -m build
twine upload dist/*
```

---

#### 5- Résultat attendu

- Après `python -m build`, on devrais voir quelque chose comme :

```
Successfully built moviesdk-0.0.1.tar.gz and moviesdk-0.0.1-py3-none-any.whl
```

- Après `twine upload dist/*`, on devrait voir :

```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading moviesdk-0.0.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.0/7.0 kB • 00:00 • ?
Uploading moviesdk-0.0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 kB • 00:00 • ?

View at:
https://pypi.org/project/moviesdk/0.0.1/
```

---

#### SDK pret

Le SDK est maintenant **publié sur PyPI** ! Tout le monde peut l’installer avec :

```bash
pip install films_sdk_sbre
```

On peux maintenant partager le lien `https://pypi.org/project/films_sdk_sbre/` à des utilisateurs.

---


### Tester le nouveau SDK publié sur PyPI

Une fois le SDK publié sur [PyPI](https://pypi.org/project/films_sdk_sbre/), il est important de tester son bon fonctionnement comme un **utilisateur final** le ferait.

---

#### Étape 1 : Créer un nouveau projet Python

1. Créer un dossier pour tester le SDK :

```bash
mkdir test_films_sdk_sbre
cd test_films_sdk_sbre
```

2. Créer un nouvel environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate      # Sous macOS/Linux
# .venv\Scripts\activate       # Sous Windows
```

3. Installer le SDK publié sur PyPI :

```bash
pip install films_sdk_sbre
```

On peut aussi voir la version installée avec :

```bash
pip show films_sdk_sbre
```

---

#### Étape 2 : Tester dans un fichier ou dans un terminal Python

##### Option A - Utiliser un script de test

Crée un fichier `test_sdk_pypi.py` :

```python
from films_sdk_sbre import MovieClient, MovieConfig

# 1. Définir l'URL de l'API (en production ou en local)
config = MovieConfig(movie_base_url="https://movie-backend-x8iq.onrender.com")  # ou http://localhost:8000
client = MovieClient(config=config)

# 2. Health check
print("Health check:", client.health_check())

# 3. Récupérer un film par ID
movie = client.get_movie(1)
print("\n Movie ID 1:", movie.title)

# 4. Lister les 5 premiers films (au format pandas)
movies_df = client.list_movies(limit=5, output_format="pandas")
print("\n Liste de films (DataFrame):")
print(movies_df)

# 5. Récupérer un rating
rating = client.get_rating(user_id=1, movie_id=1)
print("\n Note utilisateur 1 pour le film 1:", rating.rating)
```

Exécute ensuiter :

```bash
python test_sdk_pypi.py
```

---

##### Option B - Tester en interactif (REPL Python)

On peut aussi tester en ouvrant un shell Python :

```bash
python
```

Puis taper :

```python
from films_sdk_sbre import MovieClient, MovieConfig

config = MovieConfig(movie_base_url="https://movie-backend-x8iq.onrender.com")
client = MovieClient(config=config)

# Faire un health check
client.health_check()

# Récupérer un film
movie = client.get_movie(1)
print(movie.title)

# Afficher un tableau pandas des 3 premiers films
client.list_movies(limit=3, output_format="pandas")
```

---

**Astuce :** On peut aussi tester dans un Jupyter Notebook pour profiter pleinement de l’interactivité avec Pandas !

### Ajout de la documentation au package sur PyPI

Lorsqu'on publie un package Python sur PyPI, il est fortement recommandé de fournir un fichier `README.md`. Ce fichier sera utilisé comme **page de présentation** du projet sur https://pypi.org.

#### Étapes pour afficher la documentation du SDK `films_sdk_sbre` sur PyPI

---

##### 1. Créer un fichier `README.md`

Dans le dossier `sdk/`, on crée un fichier `README.md`. C’est lui qui sera affiché automatiquement sur la page du package.

```bash
touch README.md
```

Rédiger le README en Markdown avec les sections suivantes :
- Présentation du projet
- Installation du SDK depuis PyPI
- Utilisation de base avec exemples concrets
- Fonctionnalités clés
- Lien vers l’API (hébergée sur Render ou en local)

Voir exemple de documentation dans `sdk/README.md`.

---

##### 2. Modifier le fichier `pyproject.toml`

Ajouter ou modifie la section `[project]` pour inclure le `README.md` comme description du projet :

```toml
[project]
name = "films_sdk_sbre"
version = "0.0.2"
description = "SDK Python pour interagir avec l'API MovieLens"
readme = "README.md"
requires-python = ">=3.8"
authors = [{ name = "BELLO Soboure", email = "soboure.bello@gmail.com" }]
dependencies = [
    "httpx",
    "pandas",
    "pydantic"
]
```

---

##### 3. Supprimer les anciens fichiers de build

Avant de recompiler, supprimer les anciens fichiers s’ils existent :
```bash
rm -r dist/ *.egg-info
```

---

##### 4. Rebuilder le package

Générer une nouvelle version du package :

```bash
python -m build
```

---

##### 5. Uploader sur PyPI

Publier la nouvelle version contenant la documentation :

```bash
twine upload dist/*
```

---

#### Résultat

On peut maintenant visiter la page du package et voir la documentation s’afficher correctement :

[https://pypi.org/project/films_sdk_sbre/0.0.2/](https://pypi.org/project/films_sdk_sbre/0.0.2/)

---


## Conclusion – Phase 1 : Développeur Python & Architecte API

 Je viens d’achever avec succès la **Phase 1** du parcours vers la maîtrise du développement backend en Python, avec un focus sur l’architecture d’API modernes. Cette étape  m'a permis de poser des fondations solides en conception de bases de données, en programmation orientée objet avec SQLAlchemy, en création d’API avec FastAPI, et en publication de SDK sur PyPI.

---

### Conçu la base de l'application de A à Z

-  **Conception de la base de données relationnelle** : j'ai conçu des tables et des relations métier (films, évaluations, tags...) en utilisant SQLite.
-  **Importation de données réelles** depuis des fichiers CSV (MovieLens) pour alimenter les tables.
-  **Écriture de requêtes SQL** pour extraire, manipuler et explorer les données stockées.

---

### mise en place la couche Data & ORM en Python

-  **Création de modèles SQLAlchemy** pour représenter les tables de la base dans le monde Python.
-  **Connexion à la base de données avec SQLAlchemy** et configuration d’une session propre pour exécuter les requêtes.
-  **Fonctions utilitaires (helpers)** permettant d’interagir efficacement avec la base de données (récupérer des films, ajouter une évaluation...).

---

### On a développé une API robuste avec FastAPI

-  **Création des endpoints d’API REST** pour exposer les données via HTTP.
-  **Utilisation de Pydantic** pour définir des schémas de validation et des objets de transfert de données (DTO).
-  **Tests des routes API** avec Swagger UI et ReDoc, grâce à la documentation interactive auto-générée de FastAPI.
-  **Tests en local**, dans un conteneur **Docker**, ou **déploiement en ligne** sur **Render**.

---

### On a produit un SDK Python pour interagir avec l’API

-  **Construction d’un SDK Python (`films_sdk_sbre`)** avec une interface claire pour interagir avec les endpoints exposés par l’API.
-  **Publication du SDK sur PyPI**, avec un `README.md` bien rédigé, respectant les normes de documentation.
-  **Tests du SDK publié** dans un nouveau projet, avec des appels simples en Python pour valider les fonctionnalités.
-  Le SDK est désormais accessible à toute la communauté Python, comme tout package professionnel.

---

### Compétences clés acquises

-  Conception de bases de données relationnelles
-  ORM avec SQLAlchemy
-  Architecture API RESTful avec FastAPI
-  Validation et typage fort avec Pydantic
-  Utilisation de Docker pour contenairiser votre application
-  Déploiement cloud sur Render
-  Génération de documentation API automatique (Swagger / Redoc)
-  Packaging Python, publication sur PyPI, gestion de versions
-  Création d’un SDK professionnel

---

### Et maintenant ?

Dans la **Phase 2 (Data Analyst)**, on changera de perspective.

On va **consommer des APIs**, extraire et analyser des données à l’aide de pandas, créer des visualisations et des tableaux de bord pour répondre à des questions métiers concrètes. Découvrir comment utiliser les données publiées par une API pour générer des **insights puissants**.

---

  
Jusque-là, je suis maintenant capable de **construire une API professionnelle de bout en bout et de créer un SDK réutilisable**.  
C’est exactement ce que font les développeurs dans des équipes tech modernes !

Passons à la Phase 2 : **Data Analyst – From API to Insight**.

--- 


