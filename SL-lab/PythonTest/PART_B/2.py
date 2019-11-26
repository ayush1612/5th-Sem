def CelsiusToFahrenheit(tempC):
    return 1.8*tempC + 32

def FahrenheitToCelsius(tempF):
    return (tempF - 32)*(5/9)

def KelvinToCelsius(tempK):
    return tempK - 273.15


def KelvinToFahrenheit(tempK):
    return CelsiusToFahrenheit(KelvinToCelsius(tempK))

def convertTemp():
    temp = int(input('Enter the temp:\n'))

    choice = input('Press 1 for Kelvin to Celsius.\nPress 2 for conversion from Celsius to Fahrenheit.\nPress 3 for conversion from Fahrenheit to Celsius.\nPress 4 for conversion from Kelvin to Fahrenheit.\n')

    functionChoice = {
        '1':KelvinToCelsius(temp),
        '2':CelsiusToFahrenheit(temp),
        '3':FahrenheitToCelsius(temp),
        '4':KelvinToFahrenheit(temp)
    }

    modTemp = functionChoice[choice]
    print('Converted Temperature = ',modTemp)

    return (temp,modTemp)

if __name__ == "__main__":

    tempList = []
    while(True):
        option = input('1. Make conversion\n2. See the logs\n3. Exit\n')

        if option == '1':
            tempData = convertTemp()
            tempList.append(tempData)
        
        elif option == '2':
            for item in tempList:
                print('\nOld Value :',item[0],'\nNew Value :',item[1])
        else:
            exit()
    