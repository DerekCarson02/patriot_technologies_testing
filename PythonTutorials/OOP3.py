# Python Object Oriented Programming


class Employee:
    # class variables
    raise_amt = 1.04
    num_of_emps = 0

    # constructor (instance) runs every time you create a new instance
    def __init__(self, first, last, pay):
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first[0].lower() + '.' + last.lower() + '@company.com'

        Employee.num_of_emps += 1

    # instance methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    # alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split(',')
        return cls(first, last, pay)

    # static methods behave like regular functions inside a class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Instances in a class
emp_1 = Employee('Derek', 'Carson', 50000)
emp_2 = Employee('Corey', 'Schafer', 60000)

emp_str_1 = 'John,Doe,70000'
emp_str_2 = 'Steve,Smith,30000'
emp_str_3 = 'Jane,Doe,90000'
new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)

import datetime
my_date = datetime.date(2022, 7, 11)
print(Employee.is_workday(my_date))