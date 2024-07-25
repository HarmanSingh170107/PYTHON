# Using the typing module, you can create more complex type annotations to enhance code readability and maintainability.
# only types like list,tuple,dict,etc. can be used in this method not int,str,float
from typing import Tuple,List, Dict
n : List[int] = [1,2,3,4,5]
name:Tuple[str]='HSL','mjy','lou'
create:dict[str,int]={'HSL':100,'SS':99}
print(name)
print(create)
def sum(a:int, b:int) ->int:
    return a+b
a=sum(1,3)
print(a,n)