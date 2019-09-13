# Write a python program to read in a list of elements
# Create a new list that holds all the elements minus the duplicates(Use functions)

def remove_duplicates(numbers):
	newlist = []
	for number in numbers:
		if number not in newlist:
			newlist.append(number)
		
	
	print(newlist)
	return newlist

remove_duplicates([1,2,3,4,4,4,5,5,6,7,8,8,8,8,9])
