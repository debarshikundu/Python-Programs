try:
    x = input("Enter a number: ")
    x = int(x)

    y = input("Enter another number: ")
    y = int(y)
except ValueError:
    print("Sorry, enter a number, not anything else...")
else:
    sum = x + y 
    print(f"The sum of {x} and {y} is {sum}.")