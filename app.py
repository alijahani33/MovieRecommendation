# app.py

import streamlit as st
import pandas as pd

from movie_recommender.constants import MOVIE_DATA_FILE_PATH
from movie_recommender.recommender import MovieRecommender

# Initialize the movie recommender
recommender_m = MovieRecommender(MOVIE_DATA_FILE_PATH)

# Set the title of the app
st.title("Movie Recommendation System")

# Input for the movie name
movie_title = st.text_input("Enter the name of a movie:")

# Input for the number of recommendations
limit = st.number_input("Number of recommendations:", min_value=1, max_value=30, value=5)

# Button to get recommendations
if st.button("Get Recommendations"):
    if movie_title:
        recommended_movies = recommender_m.get_similar_movies(movie_title, limit)

        # Check if any movies were found
        if recommended_movies:
            # Create a DataFrame to display the results
            movies_data = {
                "Title": [movie.title for movie in recommended_movies],
                "Release Date": [movie.release_date for movie in recommended_movies],
                "Genres": [", ".join(movie.genres) for movie in recommended_movies],
                "Overview": [movie.overview for movie in recommended_movies],
                "Vote Average": [movie.vote_average for movie in recommended_movies],
            }
            movies_df = pd.DataFrame(movies_data)

            # Display the DataFrame as a table
            st.write("### Recommended Movies:")
            st.dataframe(movies_df)
        else:
            st.write("No recommendations found for the provided movie title.")
    else:
        st.write("Please enter a movie title.")