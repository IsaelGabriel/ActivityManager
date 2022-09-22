import streamlit as st

user = "jorge"

rewards = []
if rewards in st.session_state:
    rewards = st.session_state['rewards']

st.header("Rewards")

if len(rewards) > 0:
    for reward in rewards:
        st.markdown(f"**Reward:{reward['label']}**")
        st.markdown(f"_From task:{reward['task']}._")

if st.button("rerun"):
    st.experimental_rerun()