atom = {
    'Na' : "Sodium",
    'Li' : "Lithium",
    'K' : 'Potassium'
}

#adding a unique element
atom['He'] = "helium"
print(atom,"\n\n")

# adding a duplicate element
atom['He'] = 'Helium'
print(atom,"\n\n")

print("Number of atoms :",len(atom))

search = input("Enter an element to search : ")

if search in atom:
    print("Found",search,"\n\nDetails:\n"+search,":",atom[search])
else:
    print("not found")