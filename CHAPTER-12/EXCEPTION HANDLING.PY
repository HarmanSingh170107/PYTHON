'''try:
    x=int(input("enter a number"))
    print(x)
except Exception as e: #IT CAN BE USED WHEN LIKE WE PASS NON INTEGER VALUE IN TERMINAL WE SHOULD GET ENTER VALID LITERAL BUT IT SHOWS ERROR AND ALSO WOULD NOT PRINT ANYTHING AFTEr
    print(e)

print("Thank You")'''

#FOR USING FOR SPECIFIC ERRORS ALONE:-
try:
    x=int(input("enter a number"))
    print(x)
except ValueError as v:
    print('VALUE ERROR OCCURED BRO')
    print('v')
except Exception as e: #IT CAN BE USED WHEN LIKE WE PASS NON INTEGER VALUE IN TERMINAL WE SHOULD GET ENTER VALID LITERAL BUT IT SHOWS ERROR AND ALSO WOULD NOT PRINT ANYTHING AFTEr
    print(e)

print("Thank You")

