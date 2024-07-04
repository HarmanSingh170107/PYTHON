'''Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''
a=int(input("enter marks p"))
a1=int(input("enter marks c"))
a2=int(input("enter marks m"))
p=(a/(100))*100
p1=(a1/(100))*100
p2=(a2/(100))*100
total_p=((a1+a+a2)/(300))*100
print(p,p1,p2,total_p)
if total_p>=40 and p>=33 and p1>=33 and p2>=33:
    print("You have been passed")
else:
    print("You have been failed")