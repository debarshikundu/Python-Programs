joy = {"First Name":"Joy", "Last Name":"Yeh", "Age":24, "City":"Austin, Texas"}
david =  {"First Name":"David", "Last Name":"Shi", "Age":25, "City":"Houston, Texas"}
christopher = {"First Name":"Christopher", "Last Name":"Prosise", "Age":42, "City":"Austin, Texas"}

people = [joy, david, christopher]

for person in people:
    for k,v in person.items():
        print(k)
        print(str(v)+"\n")