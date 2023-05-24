# app8.py 와 연결되어있음

import streamlit as st
from datetime import datetime
import pandas as pd
from app_utils import save_uploaded_file # 분리해둔 함수 파일 불러오기

def run_app_csv():
    st.subheader('csv 파일 업로드')

    csv_file = st.file_uploader('csv 파일 업로드', type=['csv'])

    if csv_file is not None:
        current_time = datetime.now()
        filename = current_time.isoformat().replace(':',"_") + '.csv'
        
        csv_file.name = filename
        save_uploaded_file('csv', csv_file)

        # 대시보드에 파일 데이터프레임 출력하기
        df = pd.read_csv('csv/'+filename)
        st.dataframe(df)