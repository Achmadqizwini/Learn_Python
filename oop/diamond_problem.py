class A:
    def show(self):
        print("this is show A")


class B(A):
    def show(self):
        print("this is show B")


class C(A):
    def show(self):
        print("this is show C")


class D(B, C):
    pass


sho = D()
sho.show()
help(sho)
