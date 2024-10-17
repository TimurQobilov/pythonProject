def get_choice(player):
    print(f"{player}, выберите: камень, ножницы или бумага.")
    return input().lower()


def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Ничья!"
    elif (choice1 == "камень" and choice2 == "ножницы") or \
            (choice1 == "ножницы" and choice2 == "бумага") or \
            (choice1 == "бумага" and choice2 == "камень"):
        return "Игрок 1 победил!"
    else:
        return "Игрок 2 победил!"


def play_game():
    print("Игра: Камень, Ножницы, Бумага")
    player1_choice = get_choice("Игрок 1")
    player2_choice = get_choice("Игрок 2")

    result = determine_winner(player1_choice, player2_choice)
    print(result)


play_game()



# class Calculator:
#     def __init__(self, a, b):
#         self.a = int(input("Введите число: "))
#         self.b = int(input("Введите число: "))
#
#     def slojenie(self):
#         return self.a + self.b
#
#     def vichitanie(self):
#         return self.a - self.b
#
#     def umnojenie(self):
#         return self.a * self.b
#
#     def delenie(self):
#         if self.b != 0:
#             return self.a / self.b
#         else:
#             return "Деление на ноль невозможно"
#
#
# calc = Calculator(0, 0)
#
#
# print(f"Сложение: {calc.slojenie()}")
# print(f"Вычитание: {calc.vichitanie()}")
# print(f"Умножение: {calc.umnojenie()}")
# print(f"Деление: {calc.delenie()}")