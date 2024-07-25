try:
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    print(a/b)
except ZeroDivisionError as z:
    print('Infinite',z)