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
acc_options = ['Administrador','Funcionário']
acc_current = 0
if 'acc' in st.session_state: acc_current = acc_options.index(st.session_state['acc'])
st.session_state['acc'] = st.sidebar.selectbox(label='Account',options=['Administrador','Funcionário'],index=acc_current)

# check jsons
json_list = ['goals','tasks','rewards']
for json_name in json_list:
    if json_name not in st.session_state:
        st.session_state[json_name] = json.load(open(f"scripts/{json_name}.json", "r"))

goals = st.session_state['goals']
solo_goals, team_goals = [],[]

for k in goals.keys():
    t = goals[k]["type"] 
    if  t == "solo":
        solo_goals.append(Goal(k,st))
    elif t == "team":
        team_goals.append(Goal(k,st))

st.header("Your goals")

for goal in solo_goals:
    goal.get_card(st=st)

st.header("Collective goals")

for goal in team_goals:
    goal.get_card(st=st)

if st.session_state['acc'] == "Administrador":
    if st.button("reset session"):
        for json_name in json_list:
            st.session_state[json_name] = json.load(open(f"scripts/{json_name}.json", "r"))
        st.session_state['acc'] = "Funcionário"
        st.experimental_rerun()
if st.button("rerun"): st.experimental_rerun()
