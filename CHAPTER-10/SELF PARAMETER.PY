'''class Employee:
    language='PYTHON'
    salary=100000

    def getI():
        print(f"The language is {language}. The salary is {salary}")
hsl=Employee()
hsl.language='Javascript' #This is an instance attribute
hsl.getI() # Jab ye call karte hain using object hsl to:-
Employee.getI(hsl) # Tab aisa kuch hota hai ye 
#line sirf samjhne ke liye hai ki self as a 
# paramter function header mein lena padhta 
# hai warna error aajata hai:-
#Employee.getI() takes 0 positional arguments but 1 was given'''

class Employee:
    language='PYTHON'
    salary=100000

    def getI(self):# EK OBJECT AS PARAMETER LENA PADHEGA FOR DATA TO BE CONTAINED chahe define karein ya nhi
        print(f"The language is {self.language}. The salary is {self.salary}")
    def greet(self):
        print("good morning")
hsl=Employee()
hsl.language='Javascript' #This is an instance attribute
hsl.getI()
#self need not be defined before can be directly taken.............

hsl.greet()