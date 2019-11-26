def AtomicDictionary():          # this line is not necessary in this program (it depicts the main function)
# i) Create a dictionary 
    atomDict = {
        'Na' : 'Sodium',
        'K' : 'Potassium',
        'Mn' : 'Manganese',
        'Mg' : 'Magnesium',
        'Li' : 'Lithium'
    }

# ii) Adding unique and duplicate elements in the dictionary
    print('Dictinary before :',atomDict)

    atomDict['He'] = 'Helium'
    print('Dictionary after adding a unique element :',atomDict)
    # a new key value pair will be added as 'He' : 'Helium'

    atomDict['Na'] = 'SODIUM'
    print('Dictionary after adding a duplicate value :',atomDict)
    # 'Na' value will change from 'Sodium' to 'SODIUM'

# iii) Number of elements in the dictionary

    print('Number of Atomic Elements in the dictionary are : ',len(atomDict.items()))

# iv) Ask user to enter an element and search in the dictionary

    searchElement = input('Enter an element to search in the dictionary:\n')

    if searchElement not in atomDict.keys():        #dict.keys() returns the list of keys in the doctionary
        print('Element not in the dictionary')
    else:
        print('Name of the element ',searchElement,' is ',atomDict[searchElement])  