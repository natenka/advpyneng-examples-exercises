from class_mixins import SourceCodeMixin, AttributesMixin


class A(SourceCodeMixin):
    def __init__(self):
        print("A __init__")

class C(SourceCodeMixin, AttributesMixin):
    def __init__(self, name):
        print("C __init__")
        self.name = name

    def method1(self):
        pass
