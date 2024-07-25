def main():
    try:
        x=int(input("enter a number"))
        print(x)
    except Exception as e:
        print(e)
    finally:
        print("I am inside finally")# It means this will be executed for sure agar hamne isko function mein daala without finally so it can't get executed so finally ensures that it must be printed

main()