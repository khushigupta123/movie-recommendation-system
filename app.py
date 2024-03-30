import streamlit as st
import pandas as pd
import pickle
import requests

st.title('Movie Recommender System')


# fetching movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjODcxZWFlZTk4MmNmNWIyZjA4Y2Y2ZGUzODYxNGFjNiIsInN1YiI6IjY1NDQ5ZGI2Mjg2NmZhMDBlMWVkZWM5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B-5lFe41AwHv0AD3q-2vAVItrkfsUxgtGC85EwlyBGM"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']


# recommendation function
def recommend(selected_movie):
    movie_index = movie[movie['title'] == selected_movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    rec_movie = []
    # rec_movie_poster = []
    for i in movies_list:
        movie_id = movie.iloc[i[0]].id
        rec_movie.append(movie.iloc[i[0]].title)
        # rec_movie_poster.append(fetch_poster(movie_id))
    # return rec_movie, rec_movie_poster
    return rec_movie


# loading files from jupyter notebook

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movie = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    'Which movie is on your mind?',
    movie['title'].values
)

if st.button('Recommend'):
    # name, poster = recommend(selected_movie_name)
    name = recommend(selected_movie_name)
    for i in name:
        st.write(i)

    # col1, col2, col3, col4, col5 = st.columns(5)
    #
    # with col1:
    #     st.text(name[0])
    #     st.image(poster[0])
    # with col2:
    #     st.text(name[1])
    #     st.image(poster[1])
    # with col3:
    #     st.text(name[2])
    #     st.image(poster[2])
    # with col4:
    #     st.text(name[3])
    #     st.image(poster[3])
    # with col5:
    #     st.text(name[4])
    #     st.image(poster[4])