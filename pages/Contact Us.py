import streamlit as st

st.header("Contact Me")

with st.form("уьфшд_form"):
    user_mail = st.text_input("Your email")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        print('I was pressed')
        print(button)