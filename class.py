class tut:
    def __init__(self, name, dom):
        self.name = name
        self.dom = dom

    def relocate(self, new_name, new_dom):
        self.name = new_name
        self.dom = new_dom

Vladimir = tut(name='Vladimir', dom=5)
print(vars(Vladimir))
Vladimir.relocate('Anna', 5)
print(vars(Vladimir))
