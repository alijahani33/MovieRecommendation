import unittest

from movie_recommender.models import Movie
from movie_recommender.recommender import MovieRecommender
from movie_recommender.constants import MOVIE_DATA_FILE_PATH

class TestMovieRecommender(unittest.TestCase):
    def setUp(self):
        self.recommender = MovieRecommender(MOVIE_DATA_FILE_PATH)

    def test_get_similar_movies(self):
        result = self.recommender.get_similar_movies("interstellar", 5)
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(movie, Movie) for movie in result))

if __name__ == '__main__':
    unittest.main()
