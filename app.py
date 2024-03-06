import streamlit as st

email = st.text_input('Enter email')
password = st.text_input('Enter password')


btn = st.button('Login Karo')

# if the button is clicked
if btn:
    if email == 'amangupta73402@gmail.com' and password == '12345':
        st.balloons()

    else:
        st.error('Login Failed')