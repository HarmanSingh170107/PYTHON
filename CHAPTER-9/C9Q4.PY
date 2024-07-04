w='DONKEY'
with open('donkey.txt','r') as f:
    x=f.read()
c=x.replace(w,'#####')
with open('donkey.txt','w') as f:
    f.write(c)