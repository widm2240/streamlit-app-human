# -*- coding: utf-8 -*-

# core pkg
import streamlit as st

import pandas as pd

main():
    """코드작성"""
    iris_df = pd.read_csv(data/iris.csv)
    st.dataframe(iris_df)
if __name__ == "__main__":
    main()
