responses = {}

polling_active = True

while polling_active:
    name = str(input("What is your name?\n"))
    response = str(input("Where is your dream vacation?\n"))

    responses[name] = response 

    repeat = input("Another person? yes/no\n") 

    if repeat == "no":
        polling_active = False
for p,r in responses.items():
    print(f"\n{p}\n")
    print(f"{r}\n")
