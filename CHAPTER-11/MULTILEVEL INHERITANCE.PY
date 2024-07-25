class Employee():#PARENT
    a=1
    def __init__(self,a):
        self.a=a

class Programmer(Employee):#Child
    b=2
    def __init__(self):
        super().__init__()

class Coder(Programmer):#Grandchild
    c=3

o=Employee()
print(o.a)#print the a atrribute
# print(o.b) # SHOWS ERROR BECAUSE b is not in employee
o=Programmer()
print(o.a,o.b) # AS PROGRAMMER CAN USE ATRRIBUTE a FROM Employee as it is child

o=Coder()
print(o.a,o.b,o.c)
