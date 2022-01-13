from itertools import cycle
from collections import UserList


class Task:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Task('{self.name}')"


class ToDo(UserList):
    def postpone(self):
        first_task = self.data.pop(0)
        self.data.append(first_task)


task1 = Task("task1")
task2 = Task("task2")
task3 = Task("task3")
task4 = Task("task4")
task5 = Task("task5")

todo_list = [task1, task2, task3]
todo = ToDo(todo_list)
