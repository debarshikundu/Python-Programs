odd = []

for i in range(1,21, 2):
    odd.append(i)

for elem in odd:
    print(elem)


print(f"The first three items of the list are: {odd[:3]}")

print(f"Three items from the middle of the list are: {odd[4:7]}")

print(f"Three items from the end of the list are: {odd[-3:]}")
 