n=int(input('enter a number'))
p=1#REMEBER TO TKAE COUNTER
if n<0:
    print("enter valid no. for computing factorial of it")
if n==0 or n==1:#Remember == not =
    print("Factorial is 1")
for i in range(2,n+1):
    p*=i
print(f"Factorial of {i} is {p}")