class Programmer:
    company="Linkedin"
    def __init__(self,name,salary,pin) :
        self.name=name
        self.salary=salary
        self.pin=pin

p= Programmer("Hsl",10000000,'110055')
print(p.name,p.salary,p.pin,p.company)
r= Programmer("Soham",10000000,'110058')
print(r.name,r.salary,r.pin,r.company)