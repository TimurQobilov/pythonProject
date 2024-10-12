class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

student1 = Student()
student2 = Student(name="Oleg", age=22, groupNumber="20B")

print(student1.getName(), student1.getAge(), student1.getGroupNumber())
print(student2.getName(), student2.getAge(), student2.getGroupNumber())

student1.setNameAge("Timur", 33)
student1.setGroupNumber(57)

print(student1.getName(), student1.getAge(), student1.getGroupNumber())