import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=eb7fa588942d6964a375fa96be2ed688&language=en-US')
    data=response.json()

    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
def recommend(movie):
    movie_idx=movies[movies['title']==movie].index[0]
    dist=similarity[movie_idx]
    movies_list=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:10]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
        
    

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')
selection_of_movie=st.selectbox(
"Type movie name to be recommended",
movies['title'].values
)
if st.button('Recommend'):
    names,posters=recommend(selection_of_movie)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
