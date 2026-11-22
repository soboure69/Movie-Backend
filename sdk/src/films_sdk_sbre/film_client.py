import backoff
import httpx
from typing import Optional, List, Literal, Union

from .schemas import MovieSimple, MovieDetailed, RatingSimple, TagSimple, LinkSimple, AnalyticsResponse
from .film_config import MovieConfig

import pandas as pd


def _abandonner(exc: Exception) -> bool:
    """Ne pas réessayer les erreurs du client (404, 422...), sauf 429 (trop de requêtes)."""
    if isinstance(exc, httpx.HTTPStatusError):
        code = exc.response.status_code
        return code < 500 and code != 429
    return False


class MovieClient:
    def __init__(self, config: Optional[MovieConfig] = None):
        self.config = config or MovieConfig()
        self.movie_base_url = self.config.movie_base_url
        if self.config.movie_backoff:
            # Nouvelles tentatives à délai croissant sur les erreurs réseau, les erreurs 5xx
            # (par exemple pendant le réveil de l'API hébergée) et les 429.
            self._get = backoff.on_exception(
                backoff.expo,
                (httpx.RequestError, httpx.HTTPStatusError),
                max_time=self.config.movie_backoff_max_time,
                giveup=_abandonner,
            )(self._get_une_fois)
        else:
            self._get = self._get_une_fois

    def _get_une_fois(self, path: str, params: Optional[dict] = None):
        response = httpx.get(f"{self.movie_base_url}{path}", params=params)
        response.raise_for_status()
        return response.json()

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
        path = "/"
        data = self._get(path)
        return data

    def get_movie(self, movie_id: int) -> MovieDetailed:
        path = f"/movies/{movie_id}"
        data = self._get(path)
        return MovieDetailed(**data)

    def list_movies(
        self,
        skip: int = 0,
        limit: int = 100,
        title: Optional[str] = None,
        genre: Optional[str] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[MovieSimple], List[dict], "pd.DataFrame"]:
        path = "/movies"
        params = {"skip": skip, "limit": limit}
        if title:
            params["title"] = title
        if genre:
            params["genre"] = genre
        data = self._get(path, params)
        return self._format_output(data, MovieSimple, output_format)

    def get_rating(self, user_id: int, movie_id: int) -> RatingSimple:
        path = f"/ratings/{user_id}/{movie_id}"
        data = self._get(path)
        return RatingSimple(**data)

    def list_ratings(
        self,
        skip: int = 0,
        limit: int = 100,
        movie_id: Optional[int] = None,
        user_id: Optional[int] = None,
        min_rating: Optional[float] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[RatingSimple], List[dict], "pd.DataFrame"]:
        path = "/ratings"
        params = {"skip": skip, "limit": limit}
        if movie_id:
            params["movie_id"] = movie_id
        if user_id:
            params["user_id"] = user_id
        if min_rating:
            params["min_rating"] = min_rating
        data = self._get(path, params)
        return self._format_output(data, RatingSimple, output_format)

    def get_tag(self, user_id: int, movie_id: int, tag_text: str) -> TagSimple:
        path = f"/tags/{user_id}/{movie_id}/{tag_text}"
        data = self._get(path)
        return TagSimple(**data)

    def list_tags(
        self,
        skip: int = 0,
        limit: int = 100,
        movie_id: Optional[int] = None,
        user_id: Optional[int] = None,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[TagSimple], List[dict], "pd.DataFrame"]:
        path = "/tags"
        params = {"skip": skip, "limit": limit}
        if movie_id:
            params["movie_id"] = movie_id
        if user_id:
            params["user_id"] = user_id
        data = self._get(path, params)
        return self._format_output(data, TagSimple, output_format)

    def get_link(self, movie_id: int) -> LinkSimple:
        path = f"/links/{movie_id}"
        data = self._get(path)
        return LinkSimple(**data)

    def list_links(
        self,
        skip: int = 0,
        limit: int = 100,
        output_format: Literal["pydantic", "dict", "pandas"] = "pydantic"
    ) -> Union[List[LinkSimple], List[dict], "pd.DataFrame"]:
        path = "/links"
        params = {"skip": skip, "limit": limit}
        data = self._get(path, params)
        return self._format_output(data, LinkSimple, output_format)

    def get_analytics(self) -> AnalyticsResponse:
        path = "/analytics"
        data = self._get(path)
        return AnalyticsResponse(**data)