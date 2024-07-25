class Employee:#PARENT CLASS
    company='ITC'
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} ")

'''class Programmer:
    company='Amazon'
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} ")
    
    def showLanguage(self):
        print(f"The name is {self.name} and the salary is {self.salary}")'''

class Programmer(Employee):# INHERITED/DERIVED/CHILD CLASS[Matlab ki employee se derive hui hai ye kinda child class]
    company='Amazon'
    def showLanguage(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
# Now there is no need to write show function again in class Programmer
# as it is inherited from employee class only so commented above and writelike this shortly

x=Employee()
y=Programmer()
print(x.company,y.company)