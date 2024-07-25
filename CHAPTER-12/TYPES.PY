from typing import Tuple
n : int =5 #THESE ARE JUST TYPE HINTS IF N WILL CONATIN FLOATING VALUE 
# IT WILL NOT BE CHAMGED TO INT VALUE AS TYPE HINTS ONLY AID DEVELOPERS FOR WRITING CORRECT CODE 
# just like comments so even if write dict instead of int no error is returned

name:str='HSL'

def sum(a:int, b:int) ->int:
    return a+b
a=sum(1,3)
print(a,n)