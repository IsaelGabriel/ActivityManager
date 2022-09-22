import streamlit as st

from classes.goal import Goal

st.title("Activity Manager")
st.header("Metas")
st.subheader("Suas metas")

solo_goal = Goal("test_goal", "Teste feito para atribuir valor", "g_1")
solo_goal.get_card(st=st)

st.subheader("Metas coletivas")
