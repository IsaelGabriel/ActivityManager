import streamlit as st
import json
from scripts.classes import Task

acc_options = ['Administrador','Funcionário']
acc_current = 1
if 'acc' in st.session_state: acc_current = acc_options.index(st.session_state['acc'])
st.session_state['acc'] = st.sidebar.selectbox(label='Account',options=['Administrador','Funcionário'],index=acc_current)

user = st.session_state['acc']

if user == "Funcionário":

    tasks = None
    if 'tasks' in st.session_state:
        tasks = st.session_state['tasks']
    else:
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
# Add tasks

if user == "Administrador":
    st.header("Add Task")
    g_id = st.text_input("Task_id: ")
    g_label = st.text_input("Task name: ")
    g_date = st.text_input("Date: ")
    g_desc = st.text_input("Description: ")
    g_reward = st.text_input("Reward: ")
    if st.button("Publish task"):
        st.session_state['tasks'][g_id] = {
            "label" : g_label,
            "completion_date" : g_date,
            "description" : g_desc,
            "reward" : g_reward,
            'assigned_to' : None,
            "reward_points" : [2],
            "reward_goals_id" : ["test_02"]
        }

# # # # # #

if st.button("rerun"):
    st.experimental_rerun()