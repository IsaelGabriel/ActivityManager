class Goal:
    def __init__(self, label, description,id):
        self.label = label
        self.description = description
        self.id = id

    def get_card(self,st):
        st.latex(self.label)
        st.write(self.description)