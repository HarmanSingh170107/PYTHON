class Employee:
    language='PYTHON'
    salary=100000

    def __init__(self,name,salary,language):# dunder method[method starting and closing with double under score] which is automatically called
        self.name =name
        self.salary=salary
        self.language=language
        print("I am creating an object")
        
        

    def getI(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod 
    def greet():
        print("good morning")

hsl=Employee("Hsl",10000000,'C')
#hsl.name='Hrn'
print(hsl.name,hsl.salary,hsl.language)

#ss=Employee() # init constructor object ke bante hi call hojata hai and gets executed[gets automatically called when an object is created]
#INIT KE FUNCTION HEADER MEIN JO PARAMETERS DAALOGE UNKI VALUE PASS KARNI PADHEGI 
# IN CLASS NAME'S BRACKETS TO BE CALLED LIKE ABOVE
# ALL VALUES SHOULD BE PASSED NO DEFAULT TAKEN