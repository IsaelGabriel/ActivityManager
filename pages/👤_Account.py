import streamlit as st
import json
import scripts.firebase_handler as fb

choice = st.selectbox('login/signup',['Login','Sign up'])

email = st.text_input('Email address: ')
password = st.text_input('Password: ')