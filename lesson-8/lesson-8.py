
classes = {"1А": [],"1Б": [],"1В": [],"1Г": []}



def add_student(class_name, student_name):
    if class_name in classes:
        classes[class_name].append(student_name)
        print(f"Ученик {student_name} добавлен в класс {class_name}.")
    else:
        print(f"Класс {class_name} не существует.")



def remove_student(class_name, student_name):
    if class_name in classes:
        if student_name in classes[class_name]:
            classes[class_name].remove(student_name)
            print(f"Ученик {student_name} удален из класса {class_name}.")
        else:
            print(f"Ученик {student_name} не найден в классе {class_name}.")
    else:
        print(f"Класс {class_name} не существует.")



def move_student(from_class, to_class, student_name):
    if from_class in classes and to_class in classes:
        if student_name in classes[from_class]:
            classes[from_class].remove(student_name)
            classes[to_class].append(student_name)
            print(f"Ученик {student_name} перемещен из {from_class} в {to_class}.")
        else:
            print(f"Ученик {student_name} не найден в классе {from_class}.")
    else:
        print("Один из классов не существует.")



def show_classes():
    for class_name, students in classes.items():
        print(f"Класс {class_name}: {', '.join(students) if students else 'Пустой'}")



def main():
    while True:
        print("\nМеню управления классами:")
        print("1. Добавить ученика")
        print("2. Удалить ученика")
        print("3. Переместить ученика в другой класс")
        print("4. Показать список учеников по классам")
        print("5. Выйти")
        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            class_name = input("Введите класс (например, 1А): ")
            student_name = input("Введите имя ученика: ")
            add_student(class_name, student_name)
        elif choice == "2":
            class_name = input("Введите класс (например, 1А): ")
            student_name = input("Введите имя ученика: ")
            remove_student(class_name, student_name)
        elif choice == "3":
            from_class = input("Введите класс, из которого переводится ученик (например, 1А): ")
            to_class = input("Введите класс, в который переводится ученик (например, 1Б): ")
            student_name = input("Введите имя ученика: ")
            move_student(from_class, to_class, student_name)
        elif choice == "4":
            show_classes()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

#
# if __name__ == "__main__":
#     main()
