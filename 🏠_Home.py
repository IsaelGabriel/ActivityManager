import streamlit as st
from classes.goal import Goal


st.set_page_config(
    page_title = "Activity Manager",
    page_icon = None,
    layout = "centered",
    initial_sidebar_state = "auto"
    menu_items = None
)

st.title("Activity Manager")
st.header("Suas metas")

solo_goal = Goal("test_01")
solo_goal.get_card(st=st)

st.header("Metas coletivas")