import streamlit as st
import json
from scripts.classes import Goal

st.set_page_config(
    page_title = "Activity Manager",
    page_icon = None,
    layout = "centered",
    initial_sidebar_state = "auto",
    menu_items = None
)

# check jsons
json_list = ['goals,tasks']
for json_name in json_list:
    if json_name not in st.session_state:
        st.session_state[json_name] = json.load(open(f"scripts/{json_name}.json", "r"))

goals = st.session_state['goals']
solo_goals, team_goals = [],[]

for k in goals.keys():
    t = goals[k]["type"] 
    if  t == "solo":
        solo_goals.append(Goal(k))
    elif t == "team":
        team_goals.append(Goal(k))

st.header("Suas metas")

for goal in solo_goals:
    goal.get_card(st=st)

st.header("Metas coletivas")

for goal in team_goals:
    goal.get_card(st=st)

if st.button("reset session"):
    for json_name in json_list:
        st.session_state[json_name] = json.load(open(f"scripts/{json_name}.json", "r"))