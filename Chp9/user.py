class User:
    """Makeshift User"""

    first_name = ""
    last_name = ""
    dob = ""

    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob 
        self.login_attempts = 0
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}- Date of Birth: {self.dob}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0