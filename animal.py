class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class dog(animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def dog_sound(self):
        print('Аф-аф')

class cat(animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def cat_sound(self):
        print('Мяу-мяу')

class cow(animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def cow_sound(self):
        print('Муу-муу')

Dog = dog('Volt', 3)
Cat = cat('Snejok', 2)
Cow = cow('Dori', 4)
print(vars(Dog))
print(Dog.dog_sound())
print(vars(Cat))
print(Cat.cat_sound())
print(vars(Cow))
print(Cow.cow_sound())