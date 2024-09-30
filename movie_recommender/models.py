from dataclasses import dataclass
from typing import List
from pydantic import BaseModel, Field

@dataclass
class Movie:
    """Data class for a movie."""
    title: str
    release_date: str
    genres: List[str]
    overview: str
    vote_average: float

class RecommendationResponse(BaseModel):
    """Response model for movie recommendations."""
    title: str = Field(title="Recommended Movie Title")
    release_date: str = Field(title="Release Date of the Recommended Movie")
    genres: List[str] = Field(title="Genres of the Recommended Movie")
    overview: str = Field(title="Summary of the Recommended Movie")
    vote_average: float = Field(title="Average Rating of the Recommended Movie")
