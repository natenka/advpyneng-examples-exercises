from seven_dwwarfs import (
    Grumpy,
    Happy,
    Sleepy,
    Bashful,
    Sneezy,
    Dopey,
    Doc,
    Section,
    TestLine,
)

x = {"a": 37, "b": 42, "c": 927}

x = 123456789.123456789e123456789

if (
    very_long_variable_name is not None
    and very_long_variable_name.field > 0
    or very_long_variable_name.is_debug
):
    z = "hello " + "world"
else:
    world = "world"
    a = "hello {}".format(world)
    f = rf"hello {world}"
