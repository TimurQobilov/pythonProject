


def student():

    num_student = (int(input("Ведите количество студентов: ")))

    student=[]

    for i in range(num_student):
        name = (input("Ведите имя студента: "))
        ball = (input("Ведите оценку студента: "))
        student.append([name,ball])


    sorted_student = sorted(student,key=lambda student: student[1],reverse=True)

    print("\nСписок учеников отсортированных: ")
    for i in sorted_student:
        print(f"{student[0]}:"
              f" {student[1]}")


student()

