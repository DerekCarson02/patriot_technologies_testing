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

# Instances in a class
emp_1 = Employee('Derek', 'Carson', 50000)
emp_2 = Employee('Corey', 'Schafer', 60000)

# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.__dict__)
# Employee.raise_amount = 1.05
# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.__dict__)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)