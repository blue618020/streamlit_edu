# app8.py 와 연결되어있음

import streamlit as st
from datetime import datetime
from app_utils import save_uploaded_file # 분리해둔 함수 파일 불러오기

def run_app_image():
    st.subheader('이미지 파일 업로드')

    img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png','jpg','jpeg'])
    # type : 업로드하는 파일 형식 제한

    if img_file is not None :
        print(type(img_file))

        # 유저가 올린 파일을 서버에서 유니크하게 처리하기 위해
        # 파일명을 현재시간 조합으로 해서 만들기
        current_time = datetime.now()
        print(current_time)
        print(current_time.isoformat().replace(':','_') + '.jpg')
        # replace : 원하는 문자열 변경. 콜론을 언더바로 바꿨음

        filename = current_time.isoformat().replace(':','_') + '.jpg'

        # 함수 호출
        img_file.name = filename
        save_uploaded_file('image', img_file)

        # 대시보드에 파일 이미지 출력하기
        st.image('image/' + filename)