class car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведён')

    def unlock(self):
        print('Автомобиль заглушен')

    def Color(self, new_color):
        self.color = new_color

    def Type(self, new_type):
        self.type = new_type

    def Year(self, new_year):
        self.year = new_year

Car = car('Black', 'BMW', 2024)
print(vars(Car))
Car.start()
Car.unlock()
Car.Color('Red')
print(vars(Car))
Car.Type('Mercedes')
print(vars(Car))
Car.Year(2023)
print(vars(Car))
