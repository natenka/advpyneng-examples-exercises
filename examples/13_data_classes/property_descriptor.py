class MyProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, book_inst, Book_class=None):
        print("MyProperty: ", self, book_inst, Book_class)
        if book_inst is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(book_inst)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)
