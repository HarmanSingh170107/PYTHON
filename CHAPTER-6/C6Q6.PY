marks=int(input("ENTER YOUR MARKS"))
if marks>=90 and marks<=100:
    print("Ex")
elif 80<=marks<90:
    print("A")
elif 70<=marks<80:
    print('B')
elif 60<=marks<70:
    print('C')
elif 50<=marks<60:
    print('D')
elif marks<50 and marks>0:
    print('F')
elif marks<0:
    print("enter valid marks")
else:
    print("enter valid type")