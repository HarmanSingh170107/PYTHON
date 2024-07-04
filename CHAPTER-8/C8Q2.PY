def ctof(c):
    f=round((((9/5)*c)+32),2)
    return(f'The tempereature in fahrenheit is:{f}°F')
c=int(input('enter temperature in celsius'))
a=ctof(c)
print(a)