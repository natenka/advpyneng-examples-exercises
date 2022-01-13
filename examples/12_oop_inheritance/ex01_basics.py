# child ----> Parent1---+
#       |               |---> GrandParent
#       +---> Parent2

class GrandParent:
    pass


class Parent2:
    def __init__(self, name):
        print("Parent2 init")
        print(f"Parent2 {self=}")
        self.name = name

    def method1(self):
        print("Parent2 method1")


class Parent1(GrandParent):
    def method1(self):
        print("Parent1 method1")

    def method2(self):
        print("Parent1 method2")
        self.method1()


class Child(Parent1, Parent2):
    def method3(self):
        print("Child method3", self.name)

    def method1(self):
        super().method1()
        print("Child method1")
        # Parent1.method1(self)
        # super(Child, self).method1()

