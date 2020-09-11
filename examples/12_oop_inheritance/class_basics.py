class Parent:
    def __init__(self, name=None):
        print("Parent")
        self.name = name
        self.data = [1, 2, 3]

    def upper(self):
        return self.name.upper()


class Child(Parent):
    def __init__(self, name):
        print("Child")
        super().__init__()
        self.name = name
        # Parent.__init__(self, name)

    def test(self):
        pass
