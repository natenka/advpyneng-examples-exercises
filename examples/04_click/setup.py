from setuptools import setup

setup(
    name='pomodoro',
    version='1.0',
    py_modules=['example_05_pomodoro_timer'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pomodoro=example_05_pomodoro_timer:cli
    ''',
)
