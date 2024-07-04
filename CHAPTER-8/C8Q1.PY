def greatest(a,b,c):
    if (a>b) and (a>c):
        print(f'{a} is the greatest')
    elif (b>a) and (b>c):
        print(f'{b} is the greatest')
    elif (c>b) and (c>a):
        print(f'{c} is the greatest')
    else:
        print("some error")
greatest('a','z','r')
