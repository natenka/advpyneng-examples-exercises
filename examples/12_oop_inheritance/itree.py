import inspect
from scrapli.driver.core import IOSXEDriver
from rich.tree import Tree
from rich import print as rprint


def rich_tree(cls, tree=None):
    if not inspect.isclass(cls):
        cls = type(cls)
    tree = Tree(f"{cls.__name__}")
    bases = [c for c in cls.__bases__ if c is not object]
    if bases:
        for base in bases:
            tree.add(rich_tree(base, tree))
    return tree



if __name__ == "__main__":
    tree = rich_tree(IOSXEDriver)
    rprint(tree)
