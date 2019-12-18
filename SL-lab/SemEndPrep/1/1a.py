elements = input('Enter the elements').split()

print("Max element:",max(elements))
print('Minimum Element:',min(elements))

newEl = int(input('Enter a new element'))

elements.append(newEl)

print("New List:",elements)

delEl = int(input("Enter an element to delete"))

elements.remove(delEl)

print("List:",elements)

find = int(input("Enter the element to find in the list"))

if find in elements:
    print("yes")
else:
    print('no')