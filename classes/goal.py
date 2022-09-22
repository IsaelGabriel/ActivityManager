import json

class Goal:
    def __init__(self,g_id):
        v = json.load(open("classes/goals.json", "r"))
        self.g_id = g_id
        if g_id in v.keys():
            self.valid = True
            self.values = v[g_id]
        else:
            self.valid = False

    def get_card(self,st):
        if not self.valid: return
        #st.subheader(self.values["label"])
        #st.write(self.values["description"])
        st.write(self.values)
    
    def update_goal(self,quantity):
        v = json.load(open("classes/goals.json", "r"))
        self.values["current"] += quantity
        #v[self.g_id] = self.values
        v.update(self.values)
        with open("goals.json", "w") as outfile:
            json.dumsp(v,outfile)