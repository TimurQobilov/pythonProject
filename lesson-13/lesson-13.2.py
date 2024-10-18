### Установка базы данных и создание таблицы клиентов
import sqlite3
# Подключение к базе данных
conn = sqlite3.connect('bank.db')

cur = conn.cursor()

# Создание таблицы клиентов
cur.execute('''CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,phone TEXT NOT NULL UNIQUE,balance REAL DEFAULT 0)''')

conn.commit()


### Шаг 2: Регистрация клиента
def register_client(name, phone):
    try:
        cur.execute("INSERT INTO clients (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print(f"Клиент {name} успешно зарегистрирован.")
    except sqlite3.IntegrityError:
        print("Клиент с таким номером телефона уже существует.")


### Шаг 3: Поиск клиента по ФИО и номеру телефона
def search_client(name=None, phone=None):
    if name:
        cur.execute("SELECT * FROM clients WHERE name = ?", (name,))
    elif phone:
        cur.execute("SELECT * FROM clients WHERE phone = ?", (phone,))

    result = cur.fetchone()
    if result:
        print("Клиент найден:", result)
    else:
        print("Клиент не найден.")


### Шаг 4: Пополнение баланса
def deposit(phone, amount):
    cur.execute("SELECT balance FROM clients WHERE phone = ?", (phone,))
    current_balance = cur.fetchone()

    if current_balance:
        new_balance = current_balance[0] + amount
        cur.execute("UPDATE clients SET balance = ? WHERE phone = ?", (new_balance, phone))
        conn.commit()
        print(f"Баланс пополнен. Новый баланс: {new_balance}")
    else:
        print("Клиент не найден.")


### Шаг 5: Снятие денег с баланса
def withdraw(phone, amount):
    cur.execute("SELECT balance FROM clients WHERE phone = ?", (phone,))
    current_balance = cur.fetchone()

    if current_balance and current_balance[0] >= amount:
        new_balance = current_balance[0] - amount
        cur.execute("UPDATE clients SET balance = ? WHERE phone = ?", (new_balance, phone))
        conn.commit()
        print(f"Снято {amount}. Новый баланс: {new_balance}")
    else:
        print("Недостаточно средств или клиент не найден.")



### Шаг 6: Просмотр баланса клиента
def check_balance(phone):
    cur.execute("SELECT balance FROM clients WHERE phone = ?", (phone,))
    balance = cur.fetchone()

    if balance:
        print(f"Текущий баланс: {balance[0]}")
    else:
        print("Клиент не найден.")




### Шаг 7: Подсчет вклада на 12-24-36 месяцев
def calculate_deposit(phone, months):
    cur.execute("SELECT balance FROM clients WHERE phone = ?", (phone,))
    balance = cur.fetchone()

    if balance:
        rate = 0.05  # Допустим, процентная ставка 5%
        final_amount = balance[0] * (1 + rate) ** (months / 12)
        print(f"Сумма вклада через {months} месяцев: {final_amount:.2f}")
    else:
        print("Клиент не найден.")




### Шаг 8: Личный кабинет клиента
def client_dashboard(phone):
    print("\n--- Личный кабинет клиента ---")
    search_client(phone=phone)

    while True:
        print("\n1. Пополнить баланс\n2. Снять деньги\n3. Проверить баланс\n4. Подсчитать вклад\n5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            amount = float(input("Введите сумму для пополнения: "))
            deposit(phone, amount)
        elif choice == '2':
            amount = float(input("Введите сумму для снятия: "))
            withdraw(phone, amount)
        elif choice == '3':
            check_balance(phone)
        elif choice == '4':
            months = int(input("Введите количество месяцев (12/24/36): "))
            calculate_deposit(phone, months)
        elif choice == '5':
            print("Выход из личного кабинета.")
            break
        else:
            print("Неверный ввод.")




### Пример использования Регистрация нового клиента
register_client("Иван Иванов", "+71234567890")

# Поиск клиента
search_client(phone="+71234567890")

# Личный кабинет клиента
client_dashboard("+71234567890")

