# Python Object-Oriented Programming

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

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}  -  {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


# subclass assignment
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        self.prog_lang = prog_lang
        # Employee class handles these arguments
        super().__init__(first, last, pay)


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        # Never pass mutable datatypes
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())


# Instances in a class
emp_1 = Employee('Derek', 'Carson', 50000)
emp_2 = Employee('Corey', 'Schafer', 60000)
dev_3 = Developer('Derrick', 'Johnson', 100000, 'Python')
dev_4 = Developer('Kevin', 'James', 75000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 90000, [])

print(emp_1.__repr__())
print(emp_1.__str__())

print(1+2)
print(int.__add__(1,2))
print(emp_1 + emp_2)
print(emp_1.__len__())