Movie Fanatic Recommender (Deployment not finished yet)

Project Overview
This project is a Content-Based Movie Recommendation System that suggests movies similar to a given movie based on its plot description. It leverages the CountVectorizer from the scikit-learn library to convert movie descriptions into a matrix of token counts and generate recommendations.

Features
- Recommends movies based on similarities between cast, director, genre, movie plot, etc
- Uses CountVectorizer for feature extraction (token counts) from the movie descriptions
- Computes cosine similarity between movie vectors to find the closest matches.
- Provides a list of similar movies when a user inputs a movie title.

Prerequisites
- scikit-learn
- pandas
- numpy

Dataset
- A dataset containing 5,000 movies from themoviedb.org

Future Improvements
- Implement a hybrid recommendation system by combining content-based filtering with collaborative filtering.
- Integrate user ratings and other metadata (genres, actors, etc.) for more personalized recommendations.
- Deploy the system as a web application using frameworks like Flask or Django.

