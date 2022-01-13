from itertools import cycle


class Task:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Task('{self.name}')"


class ToDo:
    def __init__(self, tasks):
        self.tasks = tasks

    def __repr__(self):
        return f"ToDo('{self.tasks}')"

    def __getitem__(self, index):
        print("__getitem__", index)
        return self.tasks[index]

    def __iter__(self):
        print("__iter__")
        return iter(self.tasks)

    def __contains__(self, item):
        print("__contains__")
        return item in self.tasks

task1 = Task("task1")
task2 = Task("task2")
task3 = Task("task3")
task4 = Task("task4")
task5 = Task("task5")

todo_list = [task1, task2, task3, task4, task5]
todo = ToDo(todo_list)
