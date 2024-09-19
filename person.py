class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Anna = person('Anna', 20)
Vladimir = person('Vladimir', 23)
Veronika = person('Veronika', 48)
Daniil = person('Daniil', 17)
Dasha = person('Dasha', 27)
print(vars(Anna))
print(vars(Vladimir))
print(vars(Veronika))
print(vars(Daniil))
print(vars(Dasha))