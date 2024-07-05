with open("file.txt") as f:
    cnt=0
    x=f.read()
    p="python"
    if p in x:
        print("yes")
    else:
        print("no")
