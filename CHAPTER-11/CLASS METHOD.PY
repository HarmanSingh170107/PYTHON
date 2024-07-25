class Run:
    a=1
    @classmethod # As we need class value of a not instance value this decorator is used
    def show(self):
        print(f"The class value of a is {self.a}")

e=Run()
e.a=45

e.show()
 