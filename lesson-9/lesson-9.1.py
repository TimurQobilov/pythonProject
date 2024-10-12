class User:
    def __init__(self, name, email, phone, age=0):
        self.name = name
        self.email = email
        self.age = age
        self.phone = phone
    def change_name(self, name):
        self.name = name
        print(f"Имя пользователя изменено на {self.name}")

    def change_email(self, email):
        self.email = email
        print(f"Почта пользователя изменено на {self.email}")

    def change_phone(self, phone):
        self.phone = phone
        print(f"Номер телефона изменён на {self.phone}")

user1 = User("Timur", "email@gmail.com", 33, +998979019191)


print(user1.name, user1.email, user1.phone, user1.age)

user1.change_name(input("Ведите новое имя: "))
user1.change_email(input("Ведите эл почту: "))
user1.change_phone(input("Ведите номер тел: "))

print(user1.name, user1.email, user1.phone, user1.age)