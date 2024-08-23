import streamlit as st
import pickle
from tmdbv3api import Movie, TMDb

def get_recommendations(title):
    # 영화 제목을 통해 영화의 index 값을 얻기
    idx = movies[movies['title']==title].index[0]
    # cosine 유사도 매트릭스에서 idx에 해당하는 데이터를 [idx, 유사도] 형태로 얻기
    sim_score = list(enumerate(cosine_sim[idx]))
    # cosine 유사도 기준으로 내림차순 정렬
    sim_score = sorted(sim_score, key=lambda x: x[1], reverse=True)
    # 자기 자신을 제외한 10개의 추천 영화를 Slicing
    sim_score = sim_score[1: 21]
    # 추천 영화 목록 10개의 index 정보 추출
    movie_indices = [i[0] for i in sim_score]
    images = []
    titles = []
    for i in movie_indices:
        id = movies['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path: image_path = 'https://image.tmdb.org/t/p/w500' + details['poster_path']
        else:
            image_path = 'no_image.jpg'
        images.append(image_path)
        #details title은 TMDB 한글 설정 시 한글제목을 가져올 수 있다.
        titles.append(details['title'])
    return images, titles


    

#프로그램 시작
movie = Movie()
tmdb = TMDb()
tmdb.api_key = 'c668cda4cf75bf267ef2aeffa2da0341'
tmdb.language ='ko-KR'



movies = pickle.load(open('data/movies.pickle', 'rb'))
cosine_sim = pickle.load(open('data/cosine_sim.pickle', 'rb'))



st.set_page_config(layout='wide')
st.header('영화추천')
movie_list = movies['title'].values
title = st.selectbox('영화선택', movie_list)

if st.button('개추'):
    with st.spinner('기다려'):
        images, titles = get_recommendations(title)
        idx = 0
        for i in range(0, 4):
            cols = st.columns(5)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1


