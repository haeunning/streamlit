# 라이브러리 불러오기 

import pandas as pd
import streamlit as st
import numpy as np
from datetime import date

import time

st.title('🤏 popup store in Seoul ✨')
st.markdown("""---""")


# 공간크기
with st.sidebar:
    st.title('🤏 POPUP concept .ᐟ')
    st.markdown(" ")
    
    user_word = st.sidebar.text_input("진행하는 브랜드명을 입력해주세요.", "SM C&C 계열사 ㅁㅁㅁ") 
    st.markdown("""---""")
    #########################################################################
    st.markdown("**Step 1. 공간 규모를 선택해주세요.**")
    
    option1 = st.sidebar.checkbox('대규모 (300평 이상)')
    option2 = st.sidebar.checkbox('중규모 (100~300평)')
    option3 = st.sidebar.checkbox('소규모 (100평 이하)')
    
    st.markdown(" ")
    #########################################################################
    st.markdown("**Step 2. 팝업스토어 컨셉을 선택해주세요.**")
    
    option1 = st.sidebar.checkbox('일상')
    option2 = st.sidebar.checkbox('자연친화')
    option3 = st.sidebar.checkbox('키덜트')
    option4 = st.sidebar.checkbox('레트로')
    option5 = st.sidebar.checkbox('SNS')
    
    st.markdown(" ")
    #########################################################################
    st.markdown("**Step 3. 희망 가격대 선택해주세요. (24시간 기준)**")
    
    number_of_tweets = st.slider('최대 예산 한도 (단위:만원)', 0, 5000)
    
    st.markdown(" ")
    #########################################################################
    st.markdown("**Step 4. 팝업스토어 운영 기간 선택해주세요.**")
    
    start_date = st.date_input("운영 시작 날짜", date.today())
    end_date = st.date_input("운영 종료 날짜", start_date)
    if start_date <= end_date:
        st.success(f'선택한 운영 기간: {start_date}부터 {end_date}까지')
    else:
        st.error('종료 날짜는 시작 날짜 이후여야 합니다.')
    
    st.markdown(" ")

    
##############################################################################

st.markdown('**👍 이런 곳을 추천해요.**')

data = pd.read_csv('Desktop/bigpro/샘플_대관료데이터.csv', encoding = 'utf-8-sig')
st.dataframe(data)

st.markdown('**📍 추천 지역 위치**')

myData = {'lat':[37.56668], 'lon':[126.9784]}
for _ in range(100):
    myData['lat'].append(myData['lat'][0] + np.random.randn()/50.0)
    myData['lon'].append(myData['lon'][0] + np.random.randn()/50.0)
    
st.map(data=myData,zoom=10)    


with st.container():
    container = st.container(border=True)
    container.write("생활인구 변화 (0:남자/1:여자)")
    st.bar_chart(np.random.randn(12, 2))

