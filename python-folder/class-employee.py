"""
I want to define a class named Employee
I want to define init method with 3 class variables: 
- name and salary
I want to define a class method named displayCount
I want to define a class method named displayEmployee
I want to instantiate emp1 and emp2 within the class Emplyee

"""
class Employee:
    empCount = 0

    def __init__(self, name,fname, position, salary):
        self.name = name
        self.fname = fname
        self.position = position
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('\ntotal employee is: {} '.format(employee.empCount))

    def displayEmployee(self):
        print('Name: {} {}\t {}\t Salary: ${}'.format(self.name, self.fname, self.position, self.salary))

print()
emp1 = Employee('yanick'.title(),'joseph'.upper(), 'secretary'.title(), 1200)

emp2 = Employee('pedro'.title(),'poto'.upper(), 'president'.title(), 10500)

emp3 = Employee('busta'.title(),'john'.upper(), 'manager'.title(), 8500)

emp1.displayEmployee()
print()
emp2.displayEmployee()
print()
emp3.displayEmployee()
print()
print('Total employee is: {} '.format(Employee.empCount))

print()
