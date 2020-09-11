class A:
    def __init__(self):
        print("A")


class B(A):
    def test(self):
        print("B test")


class C(B, A):
    def __init__(self):
        print("C")
        super().__init__()
        # B.__init__(self)
