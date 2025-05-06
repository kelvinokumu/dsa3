#Python Object-Oriented Programming

class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+'@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

# A class is a blueprint for creating instances
emp_1=Employee('Benir','Odeny',60000)
emp_2=Employee('Test','User',70000)
print(emp_1)
print(emp_2)


print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_1))

