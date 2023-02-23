import time

print("Hello, pls do this survey pls")
time.sleep(2)

Validated = False

while Validated == False:
    Gender = input ("Are you a woman \n")
    if Gender == "yes" or Gender == "i'm non binary" or Gender == "im non binary" or Gender == "im non-binary":
        print ("kys")
        Validated = True
    elif Gender == "no":
        print ("based")
        Validated = True

time.sleep(2)

Validated = False

while Validated == False:
    Height = input ("How tall are you in cm \n")
    try:
        Height = int(Height)
        Validated = True

    except:
        pass

if Height > 168:
    print("You get bitches")

elif Height < 152:
    print("you look like a sawed off shotgun + kys")

elif Height < 168:
    print("You got no game")

time.sleep(2)

Validated = False

while Validated == False:
    Age = input("How old are you \n")
    try:
        Age = int(Age)
        Validated = True

    except:
        pass

    if Age < 0:
        print("Fetus Deletus")

    elif Age < 8 and Gender == "yes":
        print("young girls, just the way i like them")
    
    elif Age < 8 and Gender == "no":
        print("Your uncle molested you last night")
    
    elif Age < 12 and Gender == "no":
        print("fortnite kid little shortie")

    elif Age < 12 and Gender == "yes":
        print("Stop gossiping about Brad raping his teacher")
    
    elif Age < 18:
        print("depressed ahh kid")

        



