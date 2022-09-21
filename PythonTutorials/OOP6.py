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

        Employee.num_of_emps += 1

    # instance methods
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property  #converts method to an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}  -  {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


# Instances in a class
emp_1 = Employee('Derek', 'Carson', 50000)
emp_1.fullname = 'Kinston Carson'

print(emp_1.__repr__())
print(emp_1.__str__())

print(1+2)
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname