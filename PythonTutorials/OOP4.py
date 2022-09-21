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

# print(dev_3.pay)
# print(emp_1.pay)
# dev_3.apply_raise()
# emp_1.apply_raise()
# print(dev_3.pay)
# print(emp_1.pay)
# print(dev_3.raise_amt)
# print(emp_1.raise_amt)
# print(dev_3.prog_lang)
# print(dev_4.email)

# mgr_1.add_emp(dev_3)
# mgr_1.print_emps()
print(isinstance(mgr_1, Manager))
print(issubclass(Manager, Employee))