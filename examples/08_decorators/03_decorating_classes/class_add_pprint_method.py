from rich import print as rprint


def add_pprint(cls):
    def pprint(self, special_methods=False, class_attr=False):
        methods_class_attrs = vars(type(self))
        methods = {
            name: method
            for name, method in methods_class_attrs.items()
            if not name.startswith("__") and callable(method)
        }
        special_methods_dict = {
            name: method
            for name, method in methods_class_attrs.items()
            if name.startswith("__") and callable(method)
        }
        class_attrs_dict = {
            name: value
            for name, value in methods_class_attrs.items()
            if not callable(value)
        }
        self_attrs = vars(self)
        rprint(self_attrs)
        rprint(methods)
        if special_methods: rprint(special_methods_dict)
        if class_attr: rprint(class_attrs_dict)

    cls.pprint = pprint
    return cls


