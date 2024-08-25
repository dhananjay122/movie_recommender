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
    number_of_movies=int(st.selectbox("Enter the number of movies to be recommended"))
    movies_list=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:number_of_movies+1]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters,number_of_movies
        
    

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
    for i in range(number_of_movies):
        col1,col2,col3,col4,col5=st.columns(5)
        rows=number_of_movies*[1]
        Rows=st.rows(number_of_movies//5)
        for j in rows:
            if i<=(number_of_movies-5):
                with col1,Rows[j]:
                    st.text(names[i])
                    st.image(posters[i])
                with col2,Rows[j]:
                    st.text(names[i+1])
                    st.image(posters[i+1])
                with col3,Rows[j]:
                    st.text(names[i+2])
                    st.image(posters[i+2])
                with col4,Rows[j]:
                    st.text(names[i+3])
                    st.image(posters[i+3])
                with col5,Rows[j]:
                    st.text(names[i+4])
                    st.image(posters[i+4])
            else:
                pass
