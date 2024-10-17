import sqlite3
# подключение к бд
connection2 = sqlite3.connect("cars.db")
# создание среды разработчика (переводчика на язык SQL)
sql2 = connection2.cursor()
# создание таблицы
sql2.execute("CREATE TABLE IF NOT EXISTS cars (name TEXT, color TEXT);")
# добавление информации в таблицу
sql2.execute("INSERT INTO cars (name, color) VALUES ('gentra', 'black');")
# сохранение изменений
connection2.commit()
# получение информации
users_name = sql2.execute("SELECT name FROM cars WHERE color='white';").fetchall()
print(users_name)














