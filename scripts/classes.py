import json

class Goal:
    def __init__(self,g_id):
        v = json.load(open("scripts/goals.json", "r"))
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
    
    def update_goal(self,quantity):
        v = json.load(open("scripts/goals.json", "r"))
        self.values["current"] += quantity
        #v[self.g_id] = self.values
        v.update(self.values)
        with open("goals.json", "w") as outfile:
            json.dumsp(v,outfile)

class Task:
    def __init__(self,t_id):
        v = json.load(open("scripts/tasks.json", "r"))
        self.t_id = t_id
        if t_id in v.keys():
            self.valid = True
            self.values = v[t_id]
        else:
            self.valid = False

    def get_card(self,st):
        if not self.valid: return
        st.subheader(self.values["label"])
        st.write(f'**End date:** {self.values["completion_date"]}')
        st.write(self.values["description"])
        st.write(f'**Reward**: {self.values["reward"]}.')
    
    def update_goal(self,quantity):
        v = json.load(open("scripts/tasks.json", "r"))
        self.values["current"] += quantity
        #v[self.g_id] = self.values
        v.update(self.values)
        with open("goals.json", "w") as outfile:
            json.dumsp(v,outfile)