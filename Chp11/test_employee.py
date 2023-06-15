from employee import Employee
""" Testing Employee class give_raise() function"""

def test_give_default_raise():
    e = Employee('Debarshi', 'Kundu', 60000)
    e.give_raise()
    assert e.asalary == 65000

def test_give_custom_raise():
    e = Employee('Debarshi', 'Kundu', 60000)
    e.give_raise(20000)
    assert e.asalary == 80000