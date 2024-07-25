def myfunction():
    print("hi")


print(__name__)#obatined when called using from import and also return the file name of import between 2 underscores
if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    myfunction()
    print(__name__)