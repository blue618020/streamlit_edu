import streamlit as st

def main():
    st.title('내 앱 대시보드')
    
    # 유저에게 입력받기
    st.text_input('이름을 입력하세요. ')

if __name__ == '__main__':
    main()

# st. : 앱 브라우저 화면 관련 편집할 때 사용
# main()함수 안에서 편집하고 수정작업을 하면 됨