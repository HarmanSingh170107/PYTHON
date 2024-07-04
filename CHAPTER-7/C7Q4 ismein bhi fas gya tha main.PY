n=int(input('enter a number'))
if n<=1 :
    print("Not Prime")
for i in range(2,n):
    if n%i==0:
        print('Number is not prime.')
        break   
else:
    print('no. is prime')