
topping = ""
while topping != "quit":
    topping = str(input("Please enter the toppings you would like on your pizza or enter 'quit' to exit.\n"))
    if topping != "quit":
        print(f"{topping.title()} will be added to the pizza!")