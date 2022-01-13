from collections import deque

class Task:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Task('{self.name}')"


class ToDo:
    def __init__(self, tasks, max_tasks_todo=None):
        self._tasks = deque(tasks, max_tasks_todo)

    def __repr__(self):
        return f"ToDo('{self._tasks}')"

    def __getitem__(self, index):
        print("__getitem__", index)
        return self._tasks[index]

    def __iter__(self):
        print("__iter__")
        return iter(self._tasks)

    def __len__(self):
        print("__len__")
        return len(self._tasks)

    def append(self, value):
        if not isinstance(value, Task):
            raise ValueError
        self._tasks.append(value)

    def postpone(self):
        first_task = self.data.popleft()
        self.data.append(first_task)

    def add_first_priority_task(self, task):
        if not isinstance(task, Task):
            raise ValueError
        self._tasks.appendleft(task)


task1 = Task("task1")
task2 = Task("task2")
task3 = Task("task3")
task4 = Task("task4")

todo_list = [task1, task2, task3, task4]
todo = ToDo(todo_list)
