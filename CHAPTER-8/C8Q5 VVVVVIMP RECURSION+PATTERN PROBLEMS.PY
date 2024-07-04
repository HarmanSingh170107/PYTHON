def pattern(n):
    #n=int(input('enter a number'))
    if n==0:
        pass
    else:
        print('*'* n)
        pattern(n-1)
pattern(5) 