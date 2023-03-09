current_users = ["admin", "rosetta", "debarshi", "strawHide", "driver"]

new_users = ["ADMIN", "rosetta", "shaw", "lowHide", "server"]

for user in new_users:
    if user.upper() in current_users or user.lower() in current_users:
        print(f"Try a different username! {user} is already taken!")
    else:
        print(f"{user} is available!")
    