
def conversion():
	
	print("1. Convert to farenheit\n2. Convert to Celsius\n");
	choice = int(input("Enter the choice"))
	
	temp = int(input("Enter the temperature"))
	value = 0
	if choice == 1:
		value = (1.8*temp + 32)
		print("Value in farenheit",value)
	elif choice == 2:
		value = ((5/9)*(temp - 32))
		print("Value in Celsius",value)
	tup = (temp,value)
	return tup,choice
	#print(type(choice))

def display(logs):
	for i in logs:
		print(i,"\n")

def WIP():
	logsF = []
	logsC = []
	
	while(True):
	
		ch,tup = conversion()
		
		if ch == 1:
			logsF.append(tup)
		elif ch == 2:
			logsC.append(tup)
			
		print("Press 1 to continue\nPress 2 for seeing the logs of Farenheit\nPress 3 for seeing the logs of Celsius\nPress other for exit\n")
		
		choice = int(input("Enter your choice"))
		
	    if choice == 2:
			display(logsF)
			
		elif choice == 3:
			display(logsC)
		
		else:
			break
			
		
WIP()
