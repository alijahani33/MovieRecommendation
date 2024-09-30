import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List
from .models import Movie
import difflib
from .constants import SELECTED_FEATURES

class MovieRecommender:
    """Movie recommendation system"""

    def __init__(self, movie_data_file_path: str) -> None:
        """
        Initializes the movie recommender system.

        Args:
            movie_data_file_path (str): Path to the movie data file.
        """
        self.movie_data_file_path = movie_data_file_path
        self.movies_data = pd.read_csv(movie_data_file_path)
        self._prepare()

    def _prepare(self) -> None:
        """Prepares the movie data for recommendation."""
        for feature in SELECTED_FEATURES:
            self.movies_data[feature] = self.movies_data[feature].fillna('')

        combined_features = self.movies_data[SELECTED_FEATURES].agg(' '.join, axis=1)
        vectorizer = TfidfVectorizer()
        feature_vectors = vectorizer.fit_transform(combined_features)
        self.similarity = cosine_similarity(feature_vectors)
        self.list_of_all_titles = self.movies_data['title'].tolist()
        self.movies_data.reset_index(inplace=True)

    def get_similar_movies(self, movie_name: str, limit: int) -> List[Movie]:
        """
        Returns a list of similar movies based on the input movie name.

        Args:
            movie_name (str): Title of the movie for which to find similar movies.
            limit (int): Maximum number of similar movies to return.

        Returns:
            List[Movie]: List of similar movies.
        """
        try:
            find_close_match = difflib.get_close_matches(movie_name, self.list_of_all_titles)
            if not find_close_match:
                return []

            close_match = find_close_match[0]
            index_of_the_movie = self.movies_data[self.movies_data.title == close_match]['index'].values[0]
            similarity_score = list(enumerate(self.similarity[index_of_the_movie]))
            sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)[:limit]

            similar_movies: List[Movie] = []
            for movie in sorted_similar_movies:
                index = movie[0]
                movie_obj = Movie(
                    title=self.movies_data.loc[index, "title"],
                    release_date=self.movies_data.loc[index, "release_date"],
                    genres=self.movies_data.loc[index, "genres"].split(),
                    overview=self.movies_data.loc[index, "overview"],
                    vote_average=float(self.movies_data.loc[index, "vote_average"])
                )
                similar_movies.append(movie_obj)

            return similar_movies

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []
