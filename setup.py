from setuptools import setup, find_packages

setup(
    name='movie_recommender',
    version='0.1.0',
    description='A movie recommendation system using FastAPI and machine learning.',
    author='Ali jahani',
    author_email='codebrains33@gmail.com',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'pandas',
        'scikit-learn',
        'pydantic',
        'uvicorn',
        'setuptools',
        'unittest',
    ],
    include_package_data=True,
    package_data={
        'movie_recommender': ['data/*.csv'],
    },
    entry_points={
        'console_scripts': [
            'run-movie-recommender=movie_recommender.main:app',
        ],
    },
)
