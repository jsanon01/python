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

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('total employee is: {} '.format(employee.empCount))

    def displayEmployee(self):
#        print('{} {} '.format(self.fname, self.salary))
        print('Name: {}\t Salary: ${}'.format(self.name, self.salary))

emp1 = Employee('yanick joseph',1200)

emp2 = Employee('pedro poto', 8500)

emp1.displayEmployee()
emp2.displayEmployee()

#print(emp1.name, emp1.salary)

#print(emp2.name, emp2.salary)

print('total employee is: {} '.format(Employee.empCount))

