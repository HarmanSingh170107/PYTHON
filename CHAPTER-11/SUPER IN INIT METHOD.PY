class Employee():#PARENT
    a=1
    def __init__(self) :
        print("Constructor of Employee")
class Programmer(Employee):#Child
    b=2
    def __init__(self) :
        print("Constructor of Programmer")
class Coder(Programmer):#Grandchild
    c=3
    def __init__(self) :
        super().__init__() # YE TAB USE KARTEIN HAIN IT ALSO EXECUTES ITS PARENT CLASS AND PRINTS OT AS WELL
        print("Constructor of Coder ")
# o=Employee()
# print(o.a)#print the a atrribute
# print(o.b) # SHOWS ERROR BECAUSE b is not in employee
# o=Programmer()
# print(o.a,o.b) # AS PROGRAMMER CAN USE ATRRIBUTE a FROM Employee as it is child

o=Coder()
print(o.a,o.b,o.c)