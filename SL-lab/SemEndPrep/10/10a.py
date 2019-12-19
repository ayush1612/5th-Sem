from functools import reduce

numbers = [1,2,3,4,5,6]

newnumbers = [x*3 for x in numbers]

print("New List:",newnumbers)

sumOfNumbers = reduce((lambda x,y:x+y),numbers)
sumOfNewNumbers = reduce((lambda x,y:x+y),newnumbers)

print("Sum of numbers in the original list :",sumOfNumbers)

print("\nSum of new numbers :",sumOfNewNumbers)