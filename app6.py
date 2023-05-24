import streamlit as st

def main():
    st.title('내 앱 대시보드')
    
    # 유저에게 입력받기
    name = st.text_input('이름을 입력하세요. ', max_chars=10)
    st.text('입력하신 이름은 ' + name)
    # max_chars : 입력 길이 정하기


    # 여러줄 입력받기
    message = st.text_area('메시지를 입력하세요. ', height=3)
    st.text(message)
    # height : ?


    # 숫자 입력받기(정수)
    number = st.number_input('숫자를 입력하세요.', 1, 10)
    st.text(number * 3) # 연산 가능

    # 숫자 입력받기(실수)
    number2 = st.number_input('숫자를 입력하세요.', 1.0, 100.0)
    st.text(number2 * 3)


    # 날짜
    my_data = st.date_input('약속 날짜 입력')
    print(my_data)
    print(type(my_data))
    st.text(my_data)


    # 시간
    my_time = st.time_input('시간 선택') # 기본값은 15분단위
    print(my_time)
    print(type(my_time))
    st.text(my_time)


    # 비밀번호
    password = st.text_input('비밀번호 입력', type='password')
    st.text(password)


    # 색 입력
    color = st.color_picker('색을 선택하세요.')
    st.text(color)

if __name__ == '__main__':
    main()