def generatetables(n):
    t=""
    for i in range(1,11):
        t+=f"{n}x{i} = {n*i}\n"
    with open(f"tables/t_{n}.txt","w") as f:
        f.write(t)

for j in range(2,21):
    generatetables(j)

