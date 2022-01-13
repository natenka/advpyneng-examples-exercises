class Parent1:
    def __init__(self, name):
        print("Parent1 init")
        self.name = name

    def method1(self):
        print("Parent1 method1")

    def method2(self):
        print("Parent1 method2")
        self.method1()

class Parent2:
    def __init__(self, name):
        print("Parent2 init")
        self.name = name

    def method2(self):
        print("Parent2 method2")
        self.method1()

class Child(Parent1, Parent2):
    def __init__(self, name):
        self.name = name
        print("Child init")

    def method1(self):
        print("Новая штука")
        #Parent2.method1(self)
        super().method1()
        #super(Child, self).method1()

    def method3(self):
        print("method3")
        self.method1()




