import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,col2=st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("TharunVijay")
    content="""
    Hello I am Tharun! I am a python programmer, as a student and my educational qualification is B.Tech Information Technology and I am a quick learner and an analytical thinker.
    I am from India.
    """
    st.info(content)

content2 = """
Below you can find some of the apps i have built in Python.Feel free to contact me!
 """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df=pandas.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")