import time

print("Hello, pls do this survey pls")
time.sleep(2)

Validated = False

while Validated == False:
    Gender = input ("Are you a woman \n").lower()
    if Gender == "yes" or Gender == "i'm non binary" or Gender == "im non binary" or Gender == "im non-binary":
        print ("kys")
        Validated = True
    elif Gender == "no":
        print ("based")
        Validated = True

time.sleep(2)

Validated = False

while Validated == False:
    Height = input ("How tall are you in cm \n").lower()
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
    Age = input("How old are you \n").lower()
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

    elif Age > 59:
        print("Go back to your 9-5 you msierable scum")

    elif Age > 59 and Gender == "yes":
        print("Old granny bouta play sum bingo")
    
    elif Age > 59 and Gender == "no":
        print("Badass grandpa fuck yeahhhhhhhh")

    time.sleep(2)

Validated = False

while Validated == False:
    Skin = input ("What is your siin colour \n").lower()
    if Skin == "yellow":
        print("Your phone linging")
        Validated = True
    
    elif Skin == "black":
        print("STOP RESISTING OR I'LL SHOOT")
        Validated = True
    
    elif Skin == "white"
        print("You have privilage stop denying it")
        Validated = True

    elif Skin == "brown"
        print("GO BACK TO INDIA AND SCAM CALL SOMEONE")
        Validated = True

time.sleep(2)
        



