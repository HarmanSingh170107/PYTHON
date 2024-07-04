import random
print('''A:SNAKE==-1
B:WATER==1
C:GUN==0''')

computer=random.choice([-1,1,0])
n=(input("enter your choice"))
d1={'Snake':-1,'Water':1,'Gun':0}
reverse_d1={-1:'SNAKE',1:'WATER',0:'GUN'}
print(f"Your choice is {n}")
print(f"Computer's choice is {reverse_d1[computer]}")
y=d1[n]
if (computer==-1 and y==1):
    print("YOU LOSE ")
elif (computer==1 and y==-1):
    print("YOU WIN ")
elif (computer==1 and y==0):
    print("YOU LOSE")
elif (computer==0 and y==1):
    print("YOU WIN ")
elif (computer==0 and y==-1):
    print("YOU LOSE")
elif (computer==-1 and y==0):
    print("YOU WIN ") 
elif computer==y:
    print("DRAW")
else:
    print("enter valid choice")