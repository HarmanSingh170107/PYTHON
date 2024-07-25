class Animals:
    pass
    
class Pets(Animals):
    pass

class Dog(Pets):
    pass
    @staticmethod
    def bark():
        print('BOW BOW')

d=Dog()
d.bark()