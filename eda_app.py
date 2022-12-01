import streamlit as st
import utils
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(path):
    df = pd.read_csv(path)
    return df

def run_eda_app():
    
    DATA_PATH = 'data/iris.csv'
    iris_df = load_data(DATA_PATH)
    
    submenu = st.sidebar.selectbox("서브메뉴", ['기술통계량', '그래프'])
    if submenu == '기술통계량':  
        st.subheader('기술통계량')
        st.dataframe(iris_df)

        tab1, tab2, tab3 = st.tabs(['데이터타입', '기술타입', '타겟분포'])
        with tab1:

            df2=pd.DataFrame(iris_df.dtypes).transpose()
            df2.index = ['구분']
            st.dataframe(df2)

        with tab2:
            st.dataframe(pd.DataFrame(iris_df.describe()).transpose())

        with tab3: 
            st.dataframe(iris_df['species'].value_counts())

    elif submenu == '그래프':
        st.subheader('그래프')
        with st.subheader('산점도'):
            fig1 = px.scatter(iris_df,
                              x = 'sepal_width',
                              y = 'sepal_length',
                              color = 'species',
                              size = 'petal_width',
                              hover_data = ['petal_length'],
                              title = 'IRIS 산점도')
            st.plotly_chart(fig1)
        tab1, tab2 = st.tabs(['Seaborn 그래프','Histogram 그래프'])
        with tab1:
            st.write('Seaborn 그래프')
            fig, ax = plt.subplots()
            sns.boxplot(iris_df, x = 'species', y = 'sepal_length', ax = ax)
            st.pyplot(fig)


        with tab2:
            st.write('Histogram 그래프')
            fig, ax = plt.subplots()
            ax.hist(iris_df['sepal_length'], color = 'green')
            st.pyplot(fig)
            
        st.subheader('종을 선택하여 확인하기')
        col1, col2 = st.columns(2)
        with col1:
            val_species = st.selectbox('', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'))
            result = iris_df[iris_df['species'] == val_species]
            st.dataframe(result)
            
        with col2:
            fig1 = px.scatter(result, 
                              x = 'sepal_width', 
                              y = 'sepal_length', 
                              size = 'petal_width',
                              hover_data = ['petal_length']
                              )
            st.plotly_chart(fig1)
            st.write('선택한 종 -', val_species)
    else:
        pass