from collections import Counter  # for subpart b)

# a) Read the list of elements ....

def removeDuplicates(x):
    newlist = []

    for i in x:
        if i not in newlist:
            newlist.append(i)
    return newlist


def a():

    # reading the elements 
    elements = input('Enter the list').split();
    print('List of elements :',elements)

    # usinf function to create a list of unique elements
    newList = removeDuplicates(elements)
    print('List with unique elements :',newList)

    # using list comprehension to create a new list of even numbers
    n = int(input('Enter the number for making the list of even numbers'))
    evenNumbers = [x for x in range(0,n,2)]
    print('List of even numbers :',evenNumbers)

    #create another list reversing the elements 
    reverse = elements[::-1]
    print('Reverse :',reverse)


a()

# ----------------- END OF a) ---------------------




# b) Write a python program to count the frequency of words in a given file

def b(fname):
    with open(fname) as f:
        return Counter(f.read().split())      # a dictionary is returned carrying the frequency of each word



# print('Frequency of words :\n',b('test.txt'))

# TO EXECUTE b) uncomment the print statement above

# ------------------END OF b) ------------------------




# c) Read a list and find the max using a recursive function


def maxNumber(numbers,i):
# Recursive function to find the maximum
    if i==len(numbers):
        return -1
    
    return numbers[i] if numbers[i] > maxNumber(numbers,i+1) else maxNumber(numbers,i+1)


def c():
    numbers = [1,2,3,4,12,6]
    print('Maximun = ',maxNumber(numbers,0))

    
# c()

# TO EXECUTE 1a) uncomment the c) (the line above)
# --------------- END OF c) ------------------------------


