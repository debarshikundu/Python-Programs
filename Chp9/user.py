class User:
    """Makeshift User"""

    first_name = ""
    last_name = ""
    dob = ""

    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob 
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}- Date of Birth: {self.dob}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

user1 = User("Rosario", "Rodriguez", "09/07/03")
user2 = User("Lucy", "Musimo", "04/16/05")
user3 = User("Tracy", "Mellencamp", "02/02/01")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()