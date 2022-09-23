import streamlit as st
import json

choice = st.sidebar.selectbox('Account',['Administrador','Funcionário'])

email = st.text_input('Email address: ')
password = st.text_input('Password: ')