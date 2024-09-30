# Movie Recommendation System
![Movie Recommendation System](/Images/a.png)
## Overview

The **Movie Recommendation System** is a web-based application that utilizes machine learning techniques to provide personalized movie recommendations based on user input. Built using **FastAPI** for the backend and **Streamlit** for the frontend, this application offers an intuitive interface for users to discover movies similar to their favorites.

### Features

- **Movie Recommendations**: Input a movie title and receive a list of similar movies based on various features such as genres, keywords, and cast.
- **Interactive User Interface**: Built with Streamlit, allowing for a seamless user experience with real-time feedback.
- **Data-Driven Insights**: Utilizes a dataset of movies to generate recommendations, ensuring diverse and relevant suggestions.

## Technologies Used
 
- **Python**: Programming language used for backend development.
- **FastAPI**: Asynchronous web framework for building APIs quickly and efficiently.
- **Streamlit**: Framework for creating interactive web applications for machine learning and data science projects.
- **Pandas**: Library for data manipulation and analysis.
- **Scikit-learn**: Machine learning library for implementing the recommendation algorithm.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/movie_recommender.git
   cd movie_recommender
2. **Create a Virtual Environment (optional but recommended)**:
    ```bash
   python -m venv .venv
3. **Activate the Virtual Environment**:
   ```bash
   On Windows:
   .venv\Scripts\activate
   On macOS/Linux:
   source .venv/bin/activate
    
4. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt

5. **Download Movie Dataset: Ensure you have a movies.csv file in the data/ directory. You can use any movie dataset available online.**
6. **Run The App:**
   ```bash
   uvicorn movie_recommender.main:app --reload
   streamlit run app.py

### 7. Usage


1. Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the FastAPI documentation and test the API endpoints.
2. For the Streamlit application, open `http://localhost:8501` to interact with the movie recommendation system.
3. Enter a movie title in the input field and click the "Get Recommendations" button to view a list of similar movies.

## Example

Here’s an example of how to use the application:

1. Input: **"Inception"**
2. Output: A list of recommended movies such as **"Interstellar"**, **"The Matrix"**, etc., displayed in a user-friendly table format.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request.


## Contact

For any inquiries or feedback, please reach out to:
- **Ali jahani**: [alijahani1919@gmail.com](alijahani1919@gmail.com)
- **GitHub Profile**: [alijahani33](https://github.com/alijahani33)

