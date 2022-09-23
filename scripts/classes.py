import json

def add_reward(label,task,st):
    info = {
        "label" : label,
        "task" : task
    }
    if "rewards" not in st.session_state:
        st.session_state['rewards'] = [info]
    else: st.session_state['rewards'].append(info)

class Goal:
    def __init__(self,g_id,st):
        v = st.session_state['goals']
        self.g_id = g_id
        if g_id in v.keys():
            self.valid = True
            self.values = v[g_id]
        else:
            self.valid = False

    def get_card(self,st):
        if not self.valid: return
        st.subheader(self.values["label"])
        col1, col2 = st.columns(2)
        prog = int(float(float(self.values["current"])/float(self.values["max"])) * 100.0)
        col1.progress(prog)
        quant  = f'{self.values["current"]}/{self.values["max"]} {self.values["currency"]} ({prog}%)'
        col2.write(quant)
        st.write(self.values["description"])
    
    def update_goal(self,quantity,st):
        st.session_state['goals'][self.g_id]["current"] += quantity
    

class Task:
    def __init__(self,t_id,user,st):
        self.user = user
        v = st.session_state['tasks']
        self.t_id = t_id
        if t_id in v.keys():
            self.valid = True
            self.values = v[t_id]
        else:
            self.valid = False

    def get_card(self,st):
        if not self.valid: return
        with st.container():
            #st.subheader(self.values["label"])
            with st.expander(self.values["label"]):
                st.write(f'**End date:** {self.values["completion_date"]}')
                st.write(self.values["description"])
                st.write(f'**Reward**: {self.values["reward"]}.')
                if self.values['assigned_to'] == None:
                    if st.button("Claim"): self.claim_task(self.user,st)
                else:
                    if st.button("Done"): self.finish_task(self.user,st)

    def claim_task(self,user,st):
        if not self.valid: return
        self.values['assigned_to'] = user
        self.update_task(st)

    def update_task(self,st):
        v = st.session_state['tasks']
        v[self.t_id] = self.values
        st.session_state['tasks'] = v
        st.experimental_rerun()
    
    def finish_task(self,user,st):
        if "reward" in self.values.keys():
            add_reward(self.values['reward'],self.values['label'],st)
        if "reward_goals_id" in self.values.keys():
            if "goals" in st.session_state:
                for i in range(0,len(self.values['reward_goals_id'])):
                    goal_k = self.values['reward_goals_id'][i]
                    score_add = self.values['reward_points'][i]
                    if goal_k in st.session_state['goals']:
                        st.session_state['goals'][goal_k]["current"] += score_add
        del st.session_state["tasks"][self.t_id]
        st.experimental_rerun()