class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Marks :",self.marks)
    
    def accept(self):
        self.name = input("Enter the name of the student : ")
        self.age = input("Enter the age of the student :")
        self.marks = input("Enter the marks of the student :").split(' ')
    
s1 = Student('Ayush',21,[48,49,50])
print("Student 1 details\n")
s1.display()

print("\nStudent 2 details:\n")
s2 = Student('',0,[])
s2.display()

print("\nCalled accept() for Student 2\n")
s2.accept()
print("After accepting the details:")
s2.display()