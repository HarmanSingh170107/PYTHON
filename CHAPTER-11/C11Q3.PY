class Employee:
    salary=2000000
    increment=49

    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary*(self.increment/100))
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment= ((salary/a.salary)-1)*100

a=Employee()
print(a.salaryafterincrement)
print(a.increment)