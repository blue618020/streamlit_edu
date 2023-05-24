# app7.py를 토대로 파일을 나눈거임

import streamlit as st
from app_image import run_app_image # 분리해둔 이미지 파일 불러오기
from app_csv import run_app_csv # 분리해둔 csv 파일 불러오기
from app_about import run_app_about # 분리해둔 about 파일 불러오기


# 파일 업로드 하기
def main():
    st.title('내 앱 대시보드')

    # 메뉴화면 만들기
    menu = ['이미지 업로드', 'csv 업로드', 'About']
    choice = st.sidebar.selectbox("메뉴", menu)

    # 이미지파일    
    if choice == menu[0] :
        run_app_image()

    # csv 파일
    elif choice == menu[1] :
        run_app_csv()

    # about 파일
    else :
        run_app_about()
         
if __name__ == '__main__':
    main()