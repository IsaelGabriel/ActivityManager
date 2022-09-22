import streamlit as st
import json
from scripts.classes import Task

user = "jorge"

tasks = json.load(open("scripts/tasks.json", "r"))
open_tasks,user_tasks = [],[]

for k in tasks.keys():
    t = tasks[k]["assigned_to"] 
    if  t == user:
        user_tasks.append(Task(k,user,st))
    elif t == None:
        open_tasks.append(Task(k,user,st))

st.header("User Tasks")

if len(user_tasks) > 0:
    for task in user_tasks:
        task.get_card(st=st)
else:
    st.markdown('_You have claimed no tasks._')

st.header("Available Tasks")

if len(open_tasks) > 0:
    for task in open_tasks:
        task.get_card(st=st)
else:
    st.markdown("_No tasks available at the moment._")

if st.button("rerun"):
    st.experimental_rerun()
    st.session_state['tasks']['test_02'] = {
        "label" : "Limpar chão 23/09 (sexta)",
        "completion_date" : "23/09/2022",
        "description" : "",
        "assigned_to" : None,
        "reward" : "3 dias de férias pagas"
    }