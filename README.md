## Задания и примеры из книги "Advanced Python для сетевых инженеров"

[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Книга в процессе написания!

## Как создать свой репозиторий для выполнения заданий

> [Подробнее о работе с Git и Github в книге](https://pyneng.readthedocs.io/ru/latest/book/02_git_github/index.html)

### Создание репозитория на GitHub

Для создания своего репозитория на основе шаблона нужно:

-  залогиниться на [GitHub](https://github.com/)
-  открыть [репозиторий с заданиями](https://github.com/natenka/advpyneng-examples-exercises)
-  нажать "Use this template" и создать новый репозиторий на основе этого шаблона
-  в открывшемся окне надо ввести название репозитория
-  после этого готов новый репозиторий с копией всех файлов из исходного репозитория с заданиями

![](https://raw.githubusercontent.com/natenka/PyNEng/master/images/git/github_use_template.png)

### Клонирование репозитория с GitHub

Для локальной работы с репозиторием его нужно клонировать.
Для этого используется команда git clone:

```
$ git clone git@github.com:natenka/advpyneng-examples-exercises.git
Cloning into 'advpyneng-examples-exercises'...
remote: Counting objects: 241, done.
remote: Compressing objects: 100% (191/191), done.
remote: Total 241 (delta 43), reused 239 (delta 41), pack-reused 0
Receiving objects: 100% (241/241), 119.60 KiB | 0 bytes/s, done.
Resolving deltas: 100% (43/43), done.
Checking connectivity... done.
```

По сравнению с приведённой в этом листинге командой, вам нужно изменить:

-  имя пользователя natenka на имя своего пользователя на GitHub;
-  имя репозитория advpyneng-examples-exercises на имя своего
   репозитория на GitHub.

В итоге, в текущем каталоге, в котором была выполнена команда git clone,
появится каталог с именем репозитория, в моём случае –
"advpyneng-examples-exercises". В этом каталоге теперь находится
содержимое репозитория на GitHub.
