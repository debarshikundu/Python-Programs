sandwhich_orders = ["Tuna", "Grilled Cheese", "Club", "Pastrami", "Pastrami", "Pastrami"]

finished_sandwhiches = []

print("The Deli has run out of Pastrami!!!")
for sandwhich in sandwhich_orders:
    if sandwhich != "Pastrami":
        print(f"I made you a {sandwhich} sandwhich.")
    else:
        print("The Deli has run out of Pastrami!!!")
    finished_sandwhiches.append(sandwhich)
print("All sandwhich orders have been fulfilled!")
        