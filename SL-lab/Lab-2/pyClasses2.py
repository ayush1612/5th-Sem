class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

p1 = Person("Suppandi",14)

print("\n Name of person is ",p1.name)
print("\n Age of person is ",p1.age)

print("\n*** Printing after deleting age attribute for p1***")
del p1.age
print("\n Name of the person #1 is ",p1.name)

print("\n*** Printing after deleting p1***")
#del p1
print("\n Name of the person #1 is ",p1.name)

