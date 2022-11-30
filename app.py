# -*- coding: utf-8 -*-

# core pkg
import streamlit as st

import pandas as pd

def main():
    """코드작성"""
    iris_df = pd.read_csv(data/iris.csv)
    st.dataframe(iris_df)
    st.dataframe(iris_df, width=1000, height=200)
if __name__ == "__main__":
    main()
