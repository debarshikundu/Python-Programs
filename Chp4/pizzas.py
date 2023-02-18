pizzas = ["cheese", "vegetable", "pepperoni"]

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I like {pizza} pizza!")

print("I really love pizza!!!")

friend_pizzas = pizzas[:]

pizzas.append("chicken")

friend_pizzas.append("spinach")

print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)

