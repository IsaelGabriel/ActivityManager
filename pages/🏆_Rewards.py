import streamlit as st
import json

choice = st.sidebar.selectbox('Account',['Administrador','Funcionário'])
user = "jorge"

rewards = []
if 'rewards' not  in st.session_state:
    st.session_state['rewards'] = json.load(open("scripts/rewards.json","r"))
rewards = st.session_state['rewards']


st.header("Rewards")

if len(rewards) > 0:
    for reward in rewards:
        st.markdown(f'**Reward: {reward["label"]}**')
        st.write(f'From task: {reward["task"]}')
        st.write("")
else:
    st.markdown("_You have no rewards at the moment._")

if st.button("rerun"):
    st.experimental_rerun()