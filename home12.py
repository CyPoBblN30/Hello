class ruchka:
    def __init__(self, color, money, ves):
        self.color = color
        self.money = money
        self.ves = ves
    def vzat(self):
        return "Взял ручку!"

class carandash(ruchka):
    def __init__(self, color, money, ves, dl_chego):
        super().__init__(color, money, ves)
        self.dl_chego = dl_chego

    def Dl_etogo(self):
        return 'Взяла карандаш для рисования!'

Vladimir = ruchka('Blue', 2000, 10)
print(vars(Vladimir))
print(Vladimir.vzat())
Anna = carandash('Red', 3000, 15, 'Для рисования')
print(vars(Anna))
print(Anna.Dl_etogo())



penal = {'ruchka':'Blue', 'karandash':'Red', 'tochilka':'Yellow'}

def tut(n):
    print(penal[n])

tut('ruchka')
tut('karandash')
tut('tochilka')



uchiniki = []

while True:
    surname = input('Введите фамилию ученика: ')
    if surname in uchiniki:
        print('Ученик уже добавлен, введите следующего')
    else:
        uchiniki.append(surname)
        print(uchiniki)
    if len(uchiniki) == 10:
        break
