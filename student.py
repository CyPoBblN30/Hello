class student:
    def __init__(self, name='Ivan', group='10A', age=18):
        self.name = name
        self.group = group
        self.age = age

    def getname(self, name):
        print(self.name)

    def getage(self, name):
        print(self.age)

    def getgroup(self, name):
        print(self.group)

    def setnameage(self,new_name , new_age):
        self.name = new_name
        self.age = new_age

    def setgroup(self,new_group):
        self.group = new_group

Vladimir = student('Vladimir', '10B', 17)
Anna = student('Anna', '10B', 16)
Veronika = student('Veronika', '10C', 15)
Dasha = student('Dasha', '9A', 14)
Daniil = student('Daniil', '8A', 13)
print(Vladimir.getname('Vladimir'))
print(Anna.getage('Anna'))
print(Veronika.getgroup('Veronika'))
print(vars(Dasha))
Dasha.setnameage('Elena', 10)
print(vars(Dasha))
print(vars(Daniil))
Daniil.setgroup('9A')
print(vars(Daniil))
