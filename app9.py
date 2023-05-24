import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('내 앱 대시보드')
    
    df = pd.read_csv('data/iris.csv')
    st.dataframe(df)

    # 꽃받침의 길이와 높이 구하기
    # sepal_length, sepal_width의 관계를 차트로 나타내기
    fig = plt.figure()  # 차트의 영역 정함

    plt.scatter(data=df, x='sepal_length', y='sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal_length')
    plt.ylabel('sepal_width')

    st.pyplot(fig)  
    # plt.show() 를 사용하지 않음. st를 써야 앱에 보일테니깐

    fig2 = plt.figure()
    sns.regplot(data=df, x='sepal_length', y='sepal_width')
    st.pyplot(fig2)



    # 상관 분석하기
    correlation = df[['sepal_length', 'sepal_width']].corr()
    st.dataframe(correlation)



    # sepal_length로 히스토그램 그리기
    # bin의 개수는 20개와 10개로
    fig3 = plt.figure(figsize=(10,4)) 
    plt.subplot(1, 2, 1)
    plt.hist(data=df, x='sepal_length', rwidth=0.8, bins=20)

    plt.subplot(1, 2, 2)
    plt.hist(data=df, x='sepal_length', rwidth=0.8, bins=10)

    st.pyplot(fig3)


    # species 컬럼에는 종에 대한 정보가 들어있는데,
    # 각 종별로 몇개씩의 데이터가 있는지 차트로 나타내기
    st.dataframe(df['species'].value_counts())
    fig4 = plt.figure()
    sns.countplot(data=df, x='species')
    st.pyplot(fig4)


    # 데이터프레임의 차트 그리는 코드도 실행 가능
    fig5 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig5)

    
    # 데이터프레임 자체 plot 함수는 스트림릿에선 안됨
    # fig6 = plt.figure()
    # df.plot()
    # st.pyplot(fig6)

    fig7 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)


if __name__ == '__main__':
    main()