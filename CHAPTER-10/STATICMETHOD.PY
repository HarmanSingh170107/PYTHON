# AGAR SELF PARAMETER USE NHI KARNA HAI LIKE SIMPLE FUNCTIONS LIKE GREET JO SIRF GOOD MORNING KAR RHA THA USE STATIC METHOD LIKE BELOW
class Employee:
    language='PYTHON'
    salary=100000

    def getI(self):# EK OBJECT AS PARAMETER LENA PADHEGA FOR DATA TO BE CONTAINED chahe define karein ya nhi
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod # write it so no self is required
    def greet():#No self used this time
        print("good morning")
hsl=Employee()
hsl.language='Javascript' #This is an instance attribute
hsl.getI()
#self need not be defined before can be directly taken.............

hsl.greet()