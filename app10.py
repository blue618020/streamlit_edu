import streamlit as st
import plotly.express as px
import altair as alt
import pandas as pd

def main():
    st.title('내 앱 대시보드')

    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)
    st.write(df1.shape)

    print(df1.columns[1:]) # Week 제외하고 이름 다 갖고온거 확인

    lang_list = df1.columns[1:]
    choice_list = st.multiselect('언어를 선택하세요.', lang_list)
    print(choice_list) # 다중선택 되는지 확인

    # 유저가 아무것도 선택하지 않았을 때 아무것도 안보이게 하기
    print(choice_list)
    if len (choice_list) > 0: #유저가 선택한 컬럼이 하나라도 있으면 
        choice_df = df1[choice_list]
        st.dataframe(choice_df) # 데이터프레임 출력
        st.line_chart(choice_df)  # 라인차트
        st.area_chart(choice_df)  # 영역차트  


    df2 = pd.read_csv('data/iris.csv') 
    st.dataframe(df2)   
    
    # 스트림릿이 제공하는 바 차트
    df3 = df2[['sepal_length', 'sepal_width']]
    st.bar_chart(df3)

    # Altair 이용
    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length', 
        y = 'petal_width',
        color = 'species'
    )
    st.altair_chart(chart)


    # 스트림릿의 map 차트
    df4 = pd.read_csv('data/location.csv', index_col=0)
    print(df4)

    st.map(df4)  # 지도가 뜬다

    # plotly의 pie 차트 (파이차트는 비율을 보고싶을 때 사용)
    df5 = pd.read_csv('data/prog_languages_data.csv', index_col=0)
    st.dataframe(df5)
    
    fig1 = px.pie(df5, 'lang', 'Sum', title='각 언어별 비율')
    st.plotly_chart(fig1)
   
    # plotly의 bar 차트 
    df6 = df5.sort_values('Sum', ascending=False)
    
    fig2 = px.bar(df6, x='lang', y='Sum')
    st.plotly_chart(fig2)
    # 차트 안에서 정렬을 시키는게 아닌 데이터를 가공할때부터 정렬을 하기


if __name__ == '__main__':
    main()