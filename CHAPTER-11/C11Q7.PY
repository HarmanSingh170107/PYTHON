'''class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __add__(self,vnew):
        return vector(self.i+vnew.i,self.j+vnew.j,self.k+vnew.k)
    def __mul__(self,vnew):
        return ((self.i*vnew.i)+(self.j*vnew.j)+(self.k*vnew.k))
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    def __len__(self):
        return 3


v1=vector(1,2,3)
v2=vector(4,5,6)
v3=vector(7,8,9)
print(v1+v2+v3)
print((v1*v2))
print(len(v1))'''
# IF LEN OF VARIABLE IS VARIABLE :-
class vector:
    def __init__(self,l):
        self.l=l
    def __len__(self):
        return len(self.l)


v1=vector([1,2,4,3])
print(len(v1))
