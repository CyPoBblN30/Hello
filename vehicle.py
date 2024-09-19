class vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(vars())

class car(vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

class motorcycle(vehicle):
    def __init__(self, brand, year, speed):
        super().__init__(brand, year)
        self.speed = speed

BMW = car('BMW', 2024, 'Red')
Suzuki = motorcycle('GSX', 2020, 200)
print(BMW.display_info())