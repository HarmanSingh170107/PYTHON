#V.V.IMPP CODEEEEE containing propert and setter decorators
class Run:
    a=1
    @classmethod
    def show(self):
        print(f"The class value of a is {self.a}")
    @property#property decorator
    def name(self):
        return self.fname*9
    @name.setter#property decorator value is just a variable name assigned to e.name  remember you doubted first
    def name(self,value):
        self.fname=value.split(" ")[0]# NOW YOU CANNOT USE ENAME AS now fname is part of it and saved only in it
        self.lname=value.split(" ")[1]
e=Run()
e.a=45
e.name='Harman SL'
print(e.name)#due to above functions in propert named decorator the return function will be printed
e.show()
#there is also a method called getter to get value
# setters and getters prename should always be name of function not str or int