import streamlit as st

st.set_page_config(layout="wide")

col1,col2=st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("TharunVijay")
    column="""
    Hello I am Tharun! I am a python programmer, as a student and my educational qualification is B.Tech Information Technology and I am a quick learner and an analytical thinker.
    I am from India.
    """
    st.info(column)
