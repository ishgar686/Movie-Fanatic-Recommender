import pickle as p
import streamlit as stl
import requests as rq
import os

def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7673d980193b4864fa3631609c71ef72".format(movie_id)
    data = rq.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "http://image.tmdb.org/t/p/w500/" + poster_path

    return full_path


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(list(enumerate(similarity_score[index])), reverse = True, key= lambda x: x[1])
    recommended_movies_titles = []
    recommended_movies_posters = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_posters.append(get_poster(movie_id))
        recommended_movies_titles.append(movies.iloc[i[0]].title)
    return recommended_movies_titles, recommended_movies_posters



stl.header("Movie Fanatic Recommendations")
movies = p.load(open("/Users/Ishaan/Desktop/Movie_Recommender/pickle/movie_list.pkl", "rb"))
similarity_score = p.load(open("/Users/Ishaan/Desktop/Movie_Recommender/pickle/similarity.pkl", "rb"))

movie_list = movies["title"].values
movie_chosen = stl.selectbox(
    "Type a movie to get your recommendation",
    movie_list
)

if stl.button ("Show recommendation"):
    recommended_movies_titles, recommended_movies_posters = recommend(movie_chosen)
    col1, col2, col3, col4, col5 = stl.columns(5)
    with col1:
        stl.text(recommended_movies_titles[0])
        stl.image(recommended_movies_posters[0])
    with col2:
        stl.text(recommended_movies_titles[1])
        stl.image(recommended_movies_posters[1])
    with col3:
        stl.text(recommended_movies_titles[2])
        stl.image(recommended_movies_posters[2])
    with col4:
        stl.text(recommended_movies_titles[3])
        stl.image(recommended_movies_posters[3])
    with col5:
        stl.text(recommended_movies_titles[4])
        stl.image(recommended_movies_posters[4])