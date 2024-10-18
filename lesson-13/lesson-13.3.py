### Шаг 1: Создание базы данных и таблицы "students"
import sqlite3

# Подключение к базе данных SQLite (если файл не существует, он будет создан)
conn = sqlite3.connect('mydatabase.db')

cur = conn.cursor()

# Создание таблицы students
cur.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER,grade TEXT)''')

conn.commit()


### Шаг 2: Вставка записей в таблицу
students_data = [
    ('Алексей', 20, 'A'),
    ('Мария', 22, 'B'),
    ('Иван', 19, 'A'),
    ('Ольга', 21, 'C')
]

cur.executemany('INSERT INTO students (name, age, grade) VALUES (?, ?, ?)', students_data)
conn.commit()


### Шаг 3: Функция для получения информации о студенте по имени
def get_student_by_name(name):
    cur.execute('SELECT name, age, grade FROM students WHERE name = ?', (name,))
    student = cur.fetchone()
    if student:
        print(f"Имя: {student[0]}, Возраст: {student[1]}, Оценка: {student[2]}")
    else:
        print("Студент не найден.")


### Шаг 4: Функция для обновления оценки студента
def update_student_grade(name, new_grade):
    cur.execute('UPDATE students SET grade = ? WHERE name = ?', (new_grade, name))
    conn.commit()
    if cur.rowcount > 0:
        print(f"Оценка для {name} обновлена до {new_grade}.")
    else:
        print("Студент не найден.")


### Шаг 5: Функция для удаления студента
def delete_student(name):
    cur.execute('DELETE FROM students WHERE name = ?', (name,))
    conn.commit()
    if cur.rowcount > 0:
        print(f"Студент {name} удален.")
    else:
        print("Студент не найден.")


### Пример использования: Получение информации о студенте
get_student_by_name('Мария')

# Обновление оценки студента
update_student_grade('Иван', 'B')

# Удаление студента
delete_student('Ольга')


### Закрытие соединения с базой данных
conn.close()


