###Вот основные команды для работы с SQLite в Python:

### 1. **Подключение к базе данных**


import sqlite3

# Создание или подключение к базе данных
conn = sqlite3.connect('example.db')  # 'example.db' — это файл базы данных


##Если базы данных не существует, она будет создана автоматически.



### 2. **Создание курсора**

##Курсор нужен для выполнения SQL-запросов.


cur = conn.cursor()




### 3. **Создание таблицы**

##Для создания таблицы используется SQL-запрос `CREATE TABLE`.


cur.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY,name TEXT,age INTEGER)''')




### 4. **Вставка данных в таблицу**

##Для вставки данных используется запрос `INSERT INTO`.

cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Alice', 21))


##Чтобы вставить несколько строк:


students = [('Bob', 22), ('Charlie', 23)]
cur.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students)




### 5. **Чтение данных из таблицы**

##Для получения данных из таблицы используется запрос `SELECT`.


cur.execute("SELECT * FROM students")
rows = cur.fetchall()  # Получить все строки
for row in rows:
    print(row)




### 6. **Обновление данных**

##Чтобы изменить данные, используется запрос `UPDATE`.


cur.execute("UPDATE students SET age = ? WHERE name = ?", (24, 'Alice'))



### 7. **Удаление данных**

##Для удаления данных используется запрос `DELETE FROM`.


cur.execute("DELETE FROM students WHERE name = ?", ('Bob',))




### 8. **Сохранение изменений**

##После изменения данных необходимо сохранить их в базе с помощью `commit()`.


conn.commit()




### 9. **Закрытие соединения**

##После завершения работы всегда закрывайте соединение с базой данных.


conn.close()




### 10. **Обработка ошибок**

##Для обработки ошибок используйте блоки `try-except`.


try:
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('David', 25))
    conn.commit()
except sqlite3.Error as e:
    print(f"Ошибка: {e}")
finally:
    conn.close()


##Таким образом, программа гарантированно закрывает соединение даже при возникновении ошибки.