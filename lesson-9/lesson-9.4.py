class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def start(self):
        print("Автомобиль заведён")

    def stop(self):
        print("Автомобиль заглушен")

    def year(self, year):
        self.year = year
        print(f"Год выпуска: {self.year}")

    def type(self, type):
        self.type = type
        print(f"Марка автомобиля: {self.type}")

    def color(self, color):
        self.color = color
        print(f"Цвет автомобиля: {self.color}")

car1 = Car("Белый", "Седан", 2024)

car1.start()

print(car1.color)
print(car1.type)
print(car1.year)

car1.stop()

