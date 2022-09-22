import streamlit as st
import json

from classes.goal import Goal

st.title("Activity Manager")
st.header("Suas metas")

solo_goal = Goal("g_1")
solo_goal.get_card(st=st)

st.header("Metas coletivas")
