
class Employee:
    def __init__(self,fname, lname, asalary) -> None:
        self.fname = fname
        self.lname = lname
        self.asalary = asalary
    def give_raise(self, amount=5000):
        self.asalary += amount