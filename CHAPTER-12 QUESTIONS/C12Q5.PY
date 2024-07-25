try:
    with open('lol.txt','a') as f:
        n=int(input('enter a number'))
        table=[i*n for i in range(1,11)]
        print(table)
        f.write(f"The table of {n} is {str(table)} \n")
except Exception as e:
    print(e)