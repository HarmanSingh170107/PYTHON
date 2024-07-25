a=int(input("enter a number:"))
b=int(input("enter another number:"))

if (b==0):
    raise ZeroDivisionError("HEY OUR ROGRAM IS NOT MEANT TO DIVIDE NUMBERS BY ZERO")

else:
    print(f"The division a/b is: {a/b}")