
age = 0
active = True 
while age != -1 and active != False:
    age = int(input("What is your age? Enter '-1' to exit.\n"))
    
    if age == -1:
        active = False 
        break
    elif age < 3 and age >= 0:
        print("Your ticket is free!")
    elif age >= 3 and age <= 12:
        print("Your ticket is 10 dollars.")
    elif age > 12:
        print("Your ticket is 15 dollars.")
    else:
        print("Invalid Number for age...")