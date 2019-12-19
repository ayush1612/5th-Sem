class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def display(self):
        print("Name of the student :",self.name)
        print("Age of the Student  :",self.age)

    def accept(self):
        self.name = input("Enter the name of the student")
        self.age = input("Enter the age of the student")

s1 = Student("Kaneki Thomson",21)
print("Student 1 details\n")
s1.display()

s2 = Student('',0)
print("\nStudent 2 details before using the accept() function\n")
s2.display()

s2.accept()
print("\nStudent 2 details after using the accept() function\n")
s2.display()
