import streamlit as st
import json
user = "jorge"

rewards = []
if 'rewards' not  in st.session_state:
    st.session_state = json.load(open("scripts/rewards.json","r"))
rewards = st.session_state['rewards']


st.header("Rewards")

if len(rewards) > 0:
    for reward in rewards:
        st.markdown(f"**Reward:{reward['label']}**")
        st.markdown(f"_From task:{reward['task']}._")

if st.button("rerun"):
    st.experimental_rerun()