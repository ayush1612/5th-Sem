#Write a python program to read in a list of numbers 
#Use one-line comprehensions of create a new list of even numbers
#Create another list in recversing the elements

S = [x**2 for x in range(10)]# read elements to list
M = [x for x in S if x % 2 == 0 ]
M.reverse()
#print(M)

# ============================
# Explantion:
# In line 5 we are using an iterator 'x' which is going from 0 to 9
# S = [0,1,4,9,16,25,36,49,64,81]
# In line 6 we are storing the elements which are even in S into the new list M
# In line 7, we are reversing the list M
