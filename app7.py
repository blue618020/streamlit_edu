import streamlit as st
from datetime import datetime
import os  # 파일이름 작업해주는 라이브러리
import pandas as pd

# 디렉토리이름과 파일을 주면 
# 해당 디렉토리에 파일을 저장해주는 함수만들기

def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리가 있는지 확인
    # 없다면 디렉토리를 먼저 만들기
    if not os.path.exists(directory):
        os.makedirs(directory)

    # 2. 디렉토리가 있으면 파일 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('파일 저장 완료!')



# 파일 업로드 하기
def main():
    st.title('내 앱 대시보드')

    # 메뉴화면 만들기
    menu = ['이미지 업로드', 'csv 업로드', 'About']
    choice = st.sidebar.selectbox("메뉴", menu)


    # 이미지파일    
    if choice == menu[0] :
        st.subheader('이미지 파일 업로드')

        img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png','jpg','jpeg'])
        # type : 업로드하는 파일 형식 제한

        if img_file is not None :
            print(type(img_file))

            print(img_file.name) # 업로드한 파일 이름 확인
            print(img_file.size) # 파일 사이즈 확인(byte 단위)
            print(img_file.type) # 파일 타입 확인

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


    # csv 파일
    elif choice == menu[1] :
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



    else :
        st.subheader('About 파일 업로드')
    


if __name__ == '__main__':
    main()