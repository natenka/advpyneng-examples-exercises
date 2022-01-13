from collections.abc import MutableSequence


class Task:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Task('{self.name}')"


class ToDo(MutableSequence):
    #__getitem__, __setitem__, __delitem__, __len__, insert
    def __init__(self, tasks):
        self.tasks = tasks

    def __repr__(self):
        return f"ToDo('{self.tasks}')"

    def __getitem__(self, index):
        print("__getitem__", index)
        return self.tasks[index]

    def __setitem__(self, index, value):
        print("__setitem__", index)
        self.tasks[index] = value

    def __delitem__(self, index):
        print("__detitem__", index)
        del self.tasks[index]

    def __len__(self):
        return len(self.tasks)

    def insert(self, index, value):
        self.tasks.insert(index, value)


task1 = Task("task1")
task2 = Task("task2")
task3 = Task("task3")
task4 = Task("task4")
task5 = Task("task5")
todo_list = [task1, task2, task3, task4, task5]
todo = ToDo(todo_list)
