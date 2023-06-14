from random import choice

lottery = [1, 2]

completed_lottery = []

my_ticket = [1]

trials = 0

def random_number():

    while True:
        if len(completed_lottery) != 1:
            number = choice(lottery)
            completed_lottery.append(number)
        else:
            break

while True:
    completed_lottery = []
    random_number()
    trials += 1
    
    if completed_lottery == my_ticket:
        print(f"Trials: {trials}")
        break
   
