class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    # функция пополнения баланса
    def deposit(self, amount):
        self.balance += amount
        print(f"Баланс пополнен. Текущий баланс "
              f"{self.balance}")
    # функция снятия денег
    def cash(self, amount):
        # есть ли на балансе столько денег
        if self.balance >= amount:
            self.balance -= amount
            print(f"Вы сняли со счета {amount}$")
        else:
            print("Недостаточно денег на счету")
    # функция просмотра баланса
    def show_balance(self):
        print(f"Ваш баланс: {self.balance}$")

user1 = BankAccount("Timur")
while True:
    menu = input("Выберите дейсвтие:\n"
                 "1- Пополнить баланс\n"
                 "2- Снять деньги\n"
                 "3- Посмотреть баланс\n"
                 "4- Выход из аккаунта\n"
                 "Выберите действия: ")
    if menu == "1":
        user1.deposit(amount=int(input("введите купюры: ")))
    elif menu == "2":
        user1.cash(amount=int(input("введите сумму для снятия: ")))
    elif menu == "3":
        user1.show_balance()
    elif menu == "4":
        break





