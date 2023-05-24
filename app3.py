import streamlit as st
import pandas as pd

def main():
    st.title('앱 대시보드')

    df = pd.read_csv('data/iris.csv')
    # print(df) 이건 터미널에 출력
    st.dataframe(df) # 앱 대시보드에 출력

    # 데이터 분석할때 사용하던걸 앱 대시보드에 출력할 수 있다.
    species = df['species'].unique()
    st.text('아이리스 꽃은 ' + species + '으로 되어있다.')

    st.write(df.head())

if __name__ == '__main__':
    main()