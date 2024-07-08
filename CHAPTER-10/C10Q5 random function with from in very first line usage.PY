from random import randint#REMEMBER
class Train:
    def __init__(self,trainNo):
        self.trainNo= trainNo
    def book(self,fro,to):
        print(f"Ticket is booked in train no.:{self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train no.:{self.trainNo} is running on time")
    def getFare(self,fro,to):
        print(f"Ticket Fare in Train no.:{self.trainNo} from {fro} to {to} is {(randint(222,55555))}")#random likhne ki zarurat hi nhi hai kyunki diretc from se call kiya hai
Tejas= Train(1456778)
Tejas.book('Delhi','USA')#Imaginary 
Tejas.getStatus()
Tejas.getFare('Delhi','USA')