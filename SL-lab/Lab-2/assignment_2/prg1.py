# Class
class Student:
        def __init__(self,name, age,marks):
            self.name = name
            self.age = age
            self.marks = marks

        def display(s):
            print("Name of the Student : ",s.name)
            print("\nAge of the Student : ",s.age)
            print("\n Marks of the student : ",s.marks)
        
        def accept(s):
            
            s.name = input("Enter the name of the student\n")
            s.age = input("Enter the age of the student \n")
            for i in range(3):
                s.marks.append(input("Enter marks\n"))
            return s

# Constructors
s1 = Student("Kaneki",15,[95,95,100])
s2 = Student("Midoriya",16,[96,97,98])

print("First student:\n")
Student.display(s1)
print("Second Student:\n")
Student.display(s2)

print("Input now")
s = Student('',0,[])
s = Student.accept(s)

Student.display(s)
