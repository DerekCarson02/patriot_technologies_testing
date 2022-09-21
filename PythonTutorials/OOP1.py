# Python Object Oriented Programming


class Employee:
    # constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first[0].lower() + '.' + last.lower() + '@company.com'

    # method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Instances in a class
emp_1 = Employee('Derek', 'Carson', 50000)
emp_2 = Employee('Corey', 'Schafer', 60000)

print(emp_1.email)
print(emp_2.fullname())
print(Employee.fullname(emp_2))
