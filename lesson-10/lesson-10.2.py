class Vehicle:
    def __init__(self, year, brand):
        self.year = year
        self.brand = brand

    def display_info(self):
        print(f"Название авто: {self.brand} год выпуска: {self.year}")


class Car(Vehicle):
    def __init__(self, year, brand, wheels):
        super().__init__(year, brand)
        self.wheels = wheels

    def Car_wheels(self):
        print(f"у автомобиля есть {self.wheels} шт колёс ")




class Motorcycle(Vehicle):
    def __init__(self, year, brand, speed):
        super().__init__(year, brand)
        self.speed = speed

    def Motorcycle(self):
        print(f"мотоцыкл может набррать скорость {self.speed}")

avto = Car("2024год", "BMW", 4)
moto = Motorcycle("2023год", "Suzuki", "300км/ч" )

avto.display_info()
avto.Car_wheels()

moto.display_info()
moto.Motorcycle()



############################################################
# class Vehicle:
#     def init(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         return self.brand, self.model, self.year
#
#
# class Car(Vehicle):
#     def init(self, brand, model, year, hybrid):
#         super().init(brand, model, year)
#         self.hybrid = hybrid
#
#     def display_info(self):
#         return self.brand, self.model, self.year, self.hybrid
#
#
# class Motorcycle(Vehicle):
#     def init(self, brand, model, year, electricity):
#         super().init(brand, model, year)
#         self.electricity = electricity
#
#     def display_info(self):
#         return self.brand, self.model, self.year, self.electricity

