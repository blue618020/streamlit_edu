# app_image.py / app_csv.py / app_about.py 와 연결되어있음

# 디렉토리이름과 파일을 주면 
# 해당 디렉토리에 파일을 저장해주는 함수만들기

import streamlit as st
import os  # 파일이름 작업해주는 라이브러리

def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리가 있는지 확인
    # 없다면 디렉토리를 먼저 만들기
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 2. 디렉토리가 있으면 파일 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('파일 저장 완료!')
