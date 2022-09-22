import json

class Goal:
    def __init__(self,g_id):
        v = json.loads("../json/goals.json")
        self.g_id = g_id
        if g_id in v.keys():
            self.values = v[g_id]
        else:
            self.valid = False

    def get_card(self,st):
        st.subheader(self.values["label"])
        st.write(self.values["description"])
    
    def update_goal(self,quantity):
        v = json.loads("../json/goals.json")
        self.values["current"] += quantity
        #v[self.g_id] = self.values
        v.update(self.values)
        json.dumsp(v)