import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

chart_data=pd.DataFrame(np.random.randn(20,3),columns=["Line-1","Line-2","Line-3"])
#chart_data1=DataFrame(random.randn(20,2),columns=["Line-1","Line-2"])
#chart_data2=DataFrame(random.randn(20,1),columns=["Line-1"])
#chart_data3=DataFrame(random.randn(20))

st.header("1.Charts with Random Number")
st.subheader("1.1 Line Chart")
st.line_chart(chart_data)
#st.line_chart(chart_data1)
#st.line_chart(chart_data2)
#st.line_chart(chart_data3)


st.subheader("1.2 Area Chart")
st.area_chart(chart_data)
#st.area_chart(chart_data1)
#st.area_chart(chart_data2)
#st.area_chart(chart_data3)


st.subheader("1.3 Bar Chart")
st.bar_chart(chart_data)
#st.bar_chart(chart_data1)
#st.bar_chart(chart_data2)
#st.bar_chart(chart_data3)


st.header("2.Data Visualization with Matplotlib and Seaborn")
st.subheader("2.1 Loading the DataFrame : ")
df=pd.read_csv("C:/Streamlit/annual3.csv")
st.dataframe(df)

st.subheader("2.2 Bar Graph with Matplotlib : ")
fig=plt.figure(figsize=(15,8))
df["sector"].value_counts().plot(kind="bar")
st.pyplot(fig)


st.subheader("2.3 Distribution Plot with Seaborn : ")
fig=plt.figure(figsize=(15,8))
sns.distplot(df["year"])
st.pyplot(fig)


st.header("3. Multiple Graphs in one Columns : ")
#st.subheader("3.1 Distribution Plot with Seaborn : ")
col1,col2=st.columns(2)
with col1:
    col1.header="KDE=False"
    #col1.write("KDE=False")
    df=pd.read_csv("C:/Streamlit/annual3.csv")
    fig1=plt.figure()
    sns.distplot(df["year"],kde=False)
    st.pyplot(fig1)
with col2:
    col2.header="Hist=False"
    #col2.write("Hist=False")
    df=pd.read_csv("C:/Streamlit/annual3.csv")
    fig2=plt.figure()
    sns.distplot(df["year"],hist=False)
    st.pyplot(fig2)


st.header("4. Changing Style : ")
col1,col2=st.columns(2)
with col1:
    df=pd.read_csv("C:/Streamlit/annual3.csv")
    fig=plt.figure()
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df["data_value"],hist=False)
    st.pyplot(fig)
with col2:
    df=pd.read_csv("C:/Streamlit/annual3.csv")
    fig=plt.figure()
    sns.set_theme(context="poster",style="darkgrid")
    sns.distplot(df["data_value"],hist=False)
    st.pyplot(fig)


st.header("5. Exploring Different Graphs : ")

st.subheader("5.1 Scatter Plot")
fig,ax=plt.subplots(figsize=(15,8))
#fig,ax=subplots()
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("5.2 Count-Plot")
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x="year")
st.pyplot(fig)

st.subheader("5.3 Box-Plot")
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df, x="year",y="data_value" )
st.pyplot(fig)

st.subheader("5.4 Violin-Plot")
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x="year",y="data_value")
st.pyplot(fig)
