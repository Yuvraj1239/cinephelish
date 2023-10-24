import streamlit as st
import pandas as pd
import pickle
import requests
import pyttsx3
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))



def speak(text):
    # Initialize the text-to-speech engine

    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Convert and speak the text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
    return
    exit(0)


# Example usage


st.image('hollywood.jpg')
st.title('cinephilish')
st.text('over 5000 movies handpicked for you')
selected_movie_name = st.selectbox(
    'enter your movie name',movies['title'].values
)
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        speak(names[0])
        st.text(names[0])
        st.image(posters[0])
    with col2:
        speak(names[1])
        st.text(names[1])
        st.image(posters[1])
    with col3:
        speak(names[2])
        st.text(names[2])
        st.image(posters[2])
    with col4:
        speak(names[3])
        st.text(names[3])
        st.image(posters[3])
    with col5:
        speak(names[4])
        st.text(names[4])
        st.image(posters[4])