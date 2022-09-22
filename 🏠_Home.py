import streamlit as st

from classes.goal import Goal

st.header("Metas")
st.subheader("Suas metas")

solo_goal = Goal()
solo_goal.get_card(st=st)

st.subheader("Metas coletivas")
