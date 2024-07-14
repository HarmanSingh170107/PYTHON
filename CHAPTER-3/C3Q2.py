letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''
a=input("enter a valid name to be replaced")
b=input("enter any approiate date")
print(letter.replace('<|Name|>',a).replace('<|Date|>',b))
