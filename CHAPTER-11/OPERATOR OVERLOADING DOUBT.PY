class num:
    a=1
    b=2
    def __init__(self,n) :
        self.n=n
    def __add__(self,num1):
        return self.n+num1.n
n=num(1)
m=num(2)#IT WILL BECOME VALUE OF NUM1 ABOVE AS PASSED
print(n+m) #this will not work due to a lot of operators used so it will be unsupported
#__add__,__mul__,etc. are operator overload functions