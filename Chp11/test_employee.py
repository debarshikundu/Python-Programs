import pytest
from employee import Employee

@pytest.fixture
def bobOrSally():
    """Employee Object that is available to all test functions"""
    bobOrSally = Employee('Debarshi', 'Kundu', 60000)
    return bobOrSally


""" Testing Employee class give_raise() function"""

def test_give_default_raise(bobOrSally):
    bobOrSally.give_raise()
    assert bobOrSally.asalary == 65000

def test_give_custom_raise(bobOrSally):
    bobOrSally.give_raise(20000)
    assert bobOrSally.asalary == 80000