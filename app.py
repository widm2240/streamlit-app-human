# -*- coding: utf-8 -*-

# core pkg
import streamlit as st

import pandas as pd

def main():
    """코드작성"""
    iris_df = pd.read_csv(data/iris.csv)
    st.dataframe(iris_df)
    st.dataframe(iris_df, width=1000, height=200)

    # 색상 추가
    st.title('데이터 프레임에 색상')
    st.dataframe(iris_df.style.highlight_max)

if __name__ == "__main__":
    main()
