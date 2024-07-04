import random
def game():
    print("You are playing a luck based game")
    c=random.randint(1,100)
    with open('hiscore.txt') as f:
        x=f.read()
        if x=='':
            print("empty string")

        else:
            print(x,'= Current high score')
            with open('hiscore.txt','w') as fh:
                r=int(x)
                if c>r:
                    r=c
                    print(f"new high score:{r} ")
                    fh.write(str(c))
                else:
                    print(f"{r} remains as the unbeaten high score")
                    fh.write(str(r))
game()