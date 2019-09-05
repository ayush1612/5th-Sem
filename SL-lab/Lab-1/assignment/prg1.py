#list 
ls = [1,'2',"Three"]

# print the length of the list
print(len(ls))

# new list as an element of the existing list
ls.append([4,'5',"Six"])
print("New List after adding a new list as an element of the existing list:\n",ls)

# Using the slice operator
print("From second to the third element of the list ",ls[1:3])

# replace the second element of the list with a fruit name
ls[1] = "Orange"
print("After replacing the name of the second element with a fruit name ",ls)

# Conacatenate the lists
ls2 = [7,'8',"Nine"]
ls = ls + ls2
print("After concatenating the lists ",ls)

# Copy and clone the list
# Way 1
ls3 = []

for i in ls:
    ls3.append(i)


print("List after copying by first way : \n",ls3)

ls4 = ls3
print("List after copying by second way : \n",ls4)

ls = [0,1,2,3,4,5,6,7,8,9]

for i in range(0,len(ls),2):
    print(ls[i:i+2])
