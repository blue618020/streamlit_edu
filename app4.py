import streamlit as st
import pandas as pd

def main():
    st.title('앱 대시보드')
    
    df = pd.read_csv('data/iris.csv')

    # 버튼을 누르면 데이터 프레임이 보이게 만들기
    if st.button('데이터 보기') : # 버튼을 누르면 True가 된다
        st.dataframe(df)

    # 대문자 버튼을 누르면 대문자로 표시하고
    # 소문자 버튼을 누르면 소문자가 표시되게 하기
    name = 'Mike'
    if st.button('대문자'):
        st.text(name.lower())

    if st.button('소문자'):
        st.text(name.upper())


    st.dataframe(df)
    # petal_length 컬럼을 정렬하기
    # 오름차순 정렬, 내림차순 정렬 두가지 옵션 중 하나 선택하기
    
    status = st.radio('정렬을 선택하세요', ['오름차순','내림차순']) 
    # 2가지 이상이니 리스트 사용  
    # print(status) 
    # 앱에서 누른 값을 status에 오름차순 또는 내림차순을 메모리에 저장한걸 확인함

    if status == '오름차순':
        st.dataframe(df.sort_values('petal_length'))
    
    if status == '내림차순':
        st.dataframe(df.sort_values('petal_length', ascending=False))
    # if문으로 버튼을 눌렀을때의 실행할 것을 알려주기


    # 체크박스
    if st.checkbox('데이터프레임 보이기'):
        st.dataframe(df.head(3))
    else:
        st.write('데이터가 없습니다.')
        # 체크가 해제 상태일 때 보여주고 싶은 문장이 있다면 이렇게

    
    # 여러개 중에 1개를 선택
    language = ['Python', 'Java', 'C', 'Go', 'PHP']
    selected_lang = st.selectbox('선호하는 언어를 선택', language)

    if selected_lang == 'Python':
        st.text('파이썬이 최고지')
    elif selected_lang == 'Java':
        st.text('클래스가 좀 어렵지')
    elif selected_lang == 'C':
        st.text('C언어는 보통이지')
    elif selected_lang == 'Go':
        st.text('고우')
    elif selected_lang == 'PHP':
        st.text('php')


    # 데이터 프레임의 컬럼이름을 보여주고
    # 유저가 컬럼을 선택하면 해당컬럼만 가져와서 데이터프레임을 보여주기
    
    columns_list = st.multiselect('컬럼을 선택하세요', df.columns)
    # print(columns_list) # 터미널에서 메모리 실행 확인

    # 선택한 컬럼으로 데이터프레임을 보여주기
    st.dataframe(df[columns_list])


    # 슬라이더
    age = st.slider('나이', min_value=30, step=10, value=50)
    st.text('나이는 ' + str(age) + '입니다.')
    # min_value : 시작 값
    # step : n칸씩 조절
    # value : 디폴트 값
    # text로 출력할 때 문자열만 사용할 수 없다고 에러떠서 str(age)로 입력


    with st.expander('hello'):
        st.text('안녕하세요')

if __name__ == '__main__':
    main()