from random import randint

list = [6, 3, 72, 634, 1234, "a", "d", "h", "r", "t", 4, 5343, 6, 234, 7343]

print("Any Ticket matching these four numbers or letters, wins a prize!!!")


def selectIndex():
    index = randint(0, len(list)-1)
    return list[index]

for i in range(4):
    print(selectIndex())

  