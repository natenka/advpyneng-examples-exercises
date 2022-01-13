url_func_dict = {}


def route(link):
    def decorator(func):
        url_func_dict[link] = func
        return func
    return decorator


@route("/")
def index():
    pass

@route("/pyneng")
def pyneng_func():
    pass
