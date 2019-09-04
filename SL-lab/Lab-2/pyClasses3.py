
class Student:
	def __init__(self,name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks

s1 = Student("Ayush",20,[91,95,100])
s2 = Student("Ujjwal",20,[90,95,96])

def display(s):
	print("Name is ",s.name)
	print("Age is ",s.age)
	for i in s.marks:
		print("Marks ",i)
def accept(s):
	s.name = input("Enter name")
	s.age = input("Enter the age")
	s.marks = input("Enter marks")
	
	

display(s1)
print("\n")
display(s2)
