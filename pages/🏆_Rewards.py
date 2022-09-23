import streamlit as st
import json

acc_options = ['Administrador','Funcionário']
acc_current = 1
if 'acc' in st.session_state: acc_current = acc_options.index(st.session_state['acc'])
st.session_state['acc'] = st.sidebar.selectbox(label='Account',options=['Administrador','Funcionário'],index=acc_current)

user = st.session_state['acc']

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