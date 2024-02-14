import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st. columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Elena Daurtseva")
    content1 = """
    Hi, my name is Elena!
    """
    st.info(content1)

col3 = st.columns(1)


content2 = """
This is additional string for exceptional information. It should be stretched to the full width of the screen.
"""
st.write(content2)