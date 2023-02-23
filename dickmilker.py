import time
import math

validated = False

while validated == False:
    try:
        number1 = int(input("First number of equation "))
        number2 = int(input("Second number or base of equation "))
        validated = True
    
    except:
        pass

validated = False

while validated == False:
    sign = input("The sign of the equation ")
    if(sign == '+'):
        print(number1+number2)
        validated = True

    elif(sign == '-'):
        print(number1-number2)
        validated = True

    elif(sign == '*'):
        print(number1*number2)
        validated = True

    elif(sign == '/'):
        print(number1/number2)
        validated = True

    elif(sign == '^'):
        print(number1**number2)
        validated = True

    elif(sign == 'log'):
        print(math.log(number1,number2))
        validated = True
