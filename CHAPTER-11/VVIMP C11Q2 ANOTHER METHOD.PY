class Animals:
    def __init__(self,a,b,c) :
        self.a=a
        self.b=b
        self.c=c
    
class Pets(Animals):
    def __init__(self, a, b):
        super().__init__(a, b, None)  # Pass None for a since it's not used in Pets
    
    @staticmethod
    def bark():
        print('BOW BOW')
class Dog(Pets):
    def __init__(self, a):
        super().__init__(a, None)  # Pass None for b since it's not used in Dog
    
    @staticmethod
    def bark():
        print('BOW BOW')
x=Animals('Tom','Tommy','Sher')
print(x.a,x.b,x.c)
y=Pets('Tom','Tommy')
print(y.a,y.b)
d=Dog('Tommy')
print(d.a)
d.bark()