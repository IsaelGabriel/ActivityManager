import streamlit as st
from classes.goal import Goal

st.title("Activity Manager")
st.header("Suas metas")

solo_goal = Goal("test_01")
solo_goal.get_card(st=st)

st.header("Metas coletivas")
