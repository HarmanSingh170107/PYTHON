n=[]
word='am'  
def strip(n,word,lst1):
    for i in lst1:
        if i!=word:
            n.append(i.strip(word))
    print(n)
lst1=['harry','rohan','shubham','am']
strip(n,word,lst1)