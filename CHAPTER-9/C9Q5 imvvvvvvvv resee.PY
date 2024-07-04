Lword = ["Donkey",'tough','bad']

with open("file.txt", "r") as f:
    content = f.read()
    for i in Lword:
        content = content.replace(i, "######")

        with open("file.txt", "w") as f:
            f.write(content)