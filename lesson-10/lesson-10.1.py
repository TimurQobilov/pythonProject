class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def info_player(self):
        print(f"Игрок: {self.name} Номер: {self.number}")

class Napadayushiy(Player):
    def __init__(self,name, number, speed):
        super().__init__(name, number)
        self.speed = speed

    def plaeyr_speed(self):
        print(f" его скорость: {self.speed}")


class Zashitnik(Player):
    def __init__(self,name, number, power,):
        super().__init__(name, number)
        self.power = power


    def plaeyr_power(self):
        print(f"его сила: {self.power}")


class Poluzashita(Player):
    def __init__(self,name, number, weight, ):
        super().__init__(name, number)
        self.weight = weight

    def plaeyr_weight(self):
        print(f"его вес: {self.weight}")


class Vratar(Player):
    def __init__(self, name, number, height, ):
        super().__init__(name, number)
        self.height = height

    def plaeyr_height(self):
        print(f" его рост: {self.height}")



player1 = Napadayushiy("Олег", 11 ,"10km/ч")
player2 = Zashitnik("Иван", 17, "100кл" )
player3 = Poluzashita("Саша", 22 ,"75кл")
player4 = Vratar("Юра", 33 ,"85см")


player1.info_player()
player1.plaeyr_speed()

player2.info_player()
player2.plaeyr_power()

player3.info_player()
player3.plaeyr_weight()

player4.info_player()
player4.plaeyr_height()