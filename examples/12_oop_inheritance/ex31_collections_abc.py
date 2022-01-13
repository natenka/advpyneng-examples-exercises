from collections.abc import MutableSequence
# __getitem__, __setitem__, __delitem__, __len__, insert

class Task:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Task('{self.name}')"


class ToDo(MutableSequence):
    def __init__(self, tasks):
        self._tasks = tasks

    def __repr__(self):
        return f"ToDo('{self._tasks}')"

    def __getitem__(self, index):
        print("__getitem__", index)
        return self._tasks[index]

    def __setitem__(self, index, value):
        print("__setitem__", index, value)
        self._tasks[index] = value

    def __delitem__(self, index):
        print("__delitem__", index)
        del self._tasks[index]

    def __len__(self):
        return len(self._tasks)

    def insert(self, index, value):
        print("insert", index, value)
        self._tasks.insert(index, value)

task1 = Task("task1")
task2 = Task("task2")
task3 = Task("task3")
task4 = Task("task4")

todo_list = [task1, task2, task3, task4]
