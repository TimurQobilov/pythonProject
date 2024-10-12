class Animal:
    def __init__(self, skin, lapi):
        self.skin = skin
        self.lapi = lapi
    def make_sound(self, sound):
        print(sound)
class Horse(Animal):
    def __init__(self, skin, fur, lapi):
        super().__init__(skin, lapi)
        self.fur = fur
    def skachka(self):
        print("лошадь скачет")
class Cat(Animal):
    def __init__(self, skin, fur, lapi):
        super().__init__(skin, lapi)
        self.fur = fur
    def murchat(self):
        print("кошка мурчит")
class Fish(Animal):
    def __init__(self, skin, cheshuya):
        # super().__init__(skin=skin, lapi=None)
        self.cheshuya = cheshuya


    def make_sound(self, sound):
        pass
bucefal = Horse(skin="черная", fur="коричневый", lapi=4)
tom = Cat(skin="черная", fur="коричневый", lapi=4)
sushestvo = Animal(skin="прозрачная", lapi=1000)
nemo = Fish(skin="chernaya", cheshuya="острая")
















