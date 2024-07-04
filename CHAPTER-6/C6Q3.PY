a=["Make a lot of money", "buy now", "subscribe this", "click this"]
c=input("enter a valid comment")
for i in a:
    if i in c:
        print("The comment is spam")
        break
else:
    print("Safe comment")