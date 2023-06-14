from user import *

class Admin(User):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        self.privileges = Privileges([["can add post", "can delete post", "can ban user"]])
    
class Privileges:
    def __init__(self, privileges=[]) -> None:
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)   

