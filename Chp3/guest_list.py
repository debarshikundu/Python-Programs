names = ["Jesus", "Joy", "Debarshi",  "Rosita", "Elmo", "Julia"]

for i in range(len(names)):
    print(f"You {names[i]}, are welcome to the party!")

print(f"{len(names)} people invited...")
print("Julia cannot make it!")

names[5] = "Oscar"

for i in range(len(names)):
    print(f"You {names[i]}, are welcome to the party!")

print(f"{len(names)} people invited...")
names.insert(0, "God the Father")
names.insert(5, "Drew")

names.append("The Count")

for i in range(len(names)):
    print(f"You {names[i]}, are welcome to the party!")

print(f"{len(names)} people invited...")

print("Only room enough for 2 people!!")

print(f"Sorry, {names.pop()}, too little room!")

print(f"Sorry, {names.pop()}, too little room!")

print(f"Sorry, {names.pop()}, too little room!")

print(f"Sorry, {names.pop()}, too little room!")

print(f"Sorry, {names.pop()}, too little room!")

print(f"Sorry, {names.pop()}, too little room!")

print(f"Sorry, {names.pop()}, too little room!")

for i in range(len(names)):
    print(f"You {names[i]}, are still invited and welcome to the party!")

print(f"{len(names)} people invited...")
del names[1]

del names[0]

print(names)  #printing to show that names[] is empty

print(f"{len(names)} people invited...")