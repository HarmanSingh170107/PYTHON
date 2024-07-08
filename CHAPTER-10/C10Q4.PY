class calculator:
    def __init__(self,num):
        self.num=num
    
    def square(self):
        print(f"The square is {self.num*self.num}") # BAAR BAAR SELF DAALNA PADHEGA
        
    def cube(self):
        print(f"The cube is {self.num*self.num*self.num}")
    
    def sqaureroot(self):
        print(f"The squareroot is {self.num**(1/2)}")
    @staticmethod
    def greet():
        print("HI BRO")   
a=calculator(2)
a.square()
a.cube()
a.sqaureroot()
a.greet()
