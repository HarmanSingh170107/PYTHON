class Employee:#PARENT CLASS 1
    company='ITC'
    name='HSL'
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company} ")
class Coder:#PARENT CLASS 2
    language="Python"
    def printlanguage(self):
        print(f"out of all the languages here is your preffered language:{self.language}")
class Programmer(Employee,Coder):# DOUBLE INHERITANCES FROM TWO PARENT CLASSES
    company='Amazon'
    name='AK'
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
    
a=Employee()
b=Programmer()
b.show()
b.printlanguage()
b.showLanguage()
