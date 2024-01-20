import streamlit as st
import pandas as pd
import pickle
import requests


# Streamlit ko GitHub Pages ke liye configure karein
# st.set_option('deprecation.showPyplotGlobalUse', False)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = (movies[movies['title'] == movie]).index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movie = []
    recommend_movie_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommend_movie_poster.append(fetch_poster(movie_id))
    return recommend_movie,recommend_movie_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie-Recommend-System')

selected_movie_name = st.selectbox(
    'How would be like to be contracted?',
    (movies['title'])
)

if st.button('Recommend'):
    names,poster = recommend(selected_movie_name)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col1:
        st.text(names[1])
        st.image(poster[1])
    with col1:
        st.text(names[2])
        st.image(poster[2])
    with col1:
        st.text(names[3])
        st.image(poster[3])
    with col1:
        st.text(names[4])
        st.image(poster[4])
    
    
   