students ={
    1 : "Kaneki",
    2 : "Midoriya",
    3 : "Toka",
    4 : "Bakugo"
}

for i in students.keys():
    if i%2 == 0 :
        print(students[i])
        
        
# If u are using register number as USN
def anotherWay():
    dict={
    "1MS17IS001":"AMAN",
    "1MS17IS002":"Ayush",
    "1MS17IS003":"Aditya",
    "1MS17IS004":"Pranjal",
    "1MS17IS006":"Himanshu"
    }

    # if u are taking the usn
    # Extract each and every usn and then take out the last value if it is a single digit [1-9] and then change it to integer
    for i in dict.keys():
        if int(i[len(i)-1])%2==0:
            print("USN : ",i," Name is : ",dict[i])

# anotherWay()
# Uncomment the above line to see the output using the other way
