import sys

def display(conversions):
    for i in conversions:
        print(i[0],'to',i[1])
        print("----------------------------")

def C2F(C):
    return 1.8*C + 32

def F2C(F):
    return (F-32)*(5/9.0)

def K2C(K):
    return K-273.15

def C2K(C):
    return C+273.15

def F2K(F):
    return C2K(F2C(F))

def K2F(K):
    return C2F(K2C(K))

if __name__ == '__main__':
    choice = 1

    conversions = []

    while choice != 0:
        choice = int(input("Press 1 for converting Celsius to Farenheit\nPress 2 for converting farenheit to celsius\nPress 3 for converting Kelvin to Celsius\nPress 4 for converting Celsius to Kelvin\nPress 5 for converting Farenheit to Kelvin\nPress 6 for converting Kelvin to Farenheit\nPress 7 to display\nPress 0 to exit\n"))
        if choice != 7 and choice != 0:
            temp1 = int(input("Enter temperature 1"))
    
        if choice == 1:
            temp2 = C2F(temp1)
            deg1 = 'C'
            deg2 = 'F'        
        
        elif choice == 2:
            temp2 = F2C(temp1)
            deg1 = 'F'
            deg2 = 'C'
        
        elif choice == 3:
            temp2 = K2C(temp1)
            deg1 = 'K'
            deg2 = 'C'

        elif choice == 4:
            temp2 = C2K(temp1)
            deg1 = 'C'
            deg2 = 'K'

        elif choice == 5:
            temp2 = K2F(temp1)
            deg1 = 'K'
            deg2 = 'F'

        elif choice == 6:
            temp2 = F2K(temp1)
            deg1 = 'F'
            deg2 = 'K'

        elif choice == 7:
            display(conversions)
        else:
            break
        conversions.append((str(temp1) + deg1,str(temp2) + deg2))