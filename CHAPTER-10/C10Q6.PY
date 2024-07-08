'''slf KI JAGAH SLF YA KUCH BHI OR VARIABLE LIKHEIN TO KYA HOGA LETS SEEE'''
from random import randint#REMEMBER
class Train:
    def __init__(slf,trainNo):
        slf.trainNo= trainNo
    def book(slf,fro,to):
        print(f"Ticket is booked in train no.:{slf.trainNo} from {fro} to {to}")
    def getStatus(slf):
        print(f"Train no.:{slf.trainNo} is running on time")
    def getFare(slf,fro,to):
        print(f"Ticket Fare in Train no.:{slf.trainNo} from {fro} to {to} is {(randint(222,55555))}")#random likhne ki zarurat hi nhi hai kyunki diretc from se call kiya hai
Tejas= Train(1456778)
Tejas.book('Delhi','USA')#Imaginary 
Tejas.getStatus()
Tejas.getFare('Delhi','USA')
#Koi bhi variable name rakh sakte hain self ho ya slf same bat hai init constructor ke liye