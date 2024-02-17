import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form("email_form"):
    user_mail = st.text_input("Your email")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(user_mail, message)
        st.info("Your email was sent successfully")