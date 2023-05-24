import streamlit as st

# 이미지를 처리하는 라이브러리
from PIL import Image

def main():
    st.title('내 앱 대시보드')

    # 사진과 영상을 보여주는 방법
    img = Image.open('data/image_03.jpg')
    print(img)

    st.image(img)

    st.image(img, use_column_width=True)
    # use_column_width : 화면에 꽉차게 사진을 띄움

    # 이미지 URL로 불러와서 보여주기
    st.image('https://cdn.epnc.co.kr/news/photo/201907/91021_81259_3048.jpg')


    # 비디오 파일 보여주기
    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)

if __name__ == '__main__':
    main()