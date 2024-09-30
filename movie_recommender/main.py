# movie_recommender/main.py
from typing import List

from fastapi import FastAPI, Query, Body
from typing import List
from .recommender import MovieRecommender
from .models import RecommendationResponse
from .constants import MOVIE_DATA_FILE_PATH

app = FastAPI()
recommender = MovieRecommender(MOVIE_DATA_FILE_PATH)

@app.post("/api/v1/recommend", response_model=List[RecommendationResponse])
async def recommend(
    limit: int = Query(default=10, le=30, ge=1, title="Number of Recommended Movies"),
    movie_title: str = Body(..., title="Title of the Movie")
):
    """
    Returns a list of recommended movies based on the input movie title.

    Args:
        limit (int): Maximum number of recommended movies to return.
        movie_title (str): Title of the movie for which to find recommended movies.

    Returns:
        List[RecommendationResponse]: List of recommended movies.
    """
    recommended_movies = recommender.get_similar_movies(movie_title, limit)
    return recommended_movies
