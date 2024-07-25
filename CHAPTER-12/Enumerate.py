l=[100,33,78,89,95]

# index=0
# for i in l:
#     print(f"The item no. at index {index} is: {i}")
#     index+=1

#The above commented code can be simplified using enumerate function

for index,i in enumerate(l):
    print(f"The item no. at index {index} is: {i}")