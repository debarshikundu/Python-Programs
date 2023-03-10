joy = {"Owner":"Debarshi Kundu", "Animal":"Dog"}
koda = {"Owner":"Joy Yeh", "Animal":"Cat"}
roger = {"Owner":"Richard", "Animal":"Hamster"}

pets = [joy, koda, roger]

for pet in pets:
    for k,v in pet.items():
        print(k)
        print(str(v) +"\n")