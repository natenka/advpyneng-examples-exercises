class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def __getattribute__(self, *args, **kwargs):
        print(f"__getattribute {args=}, {kwargs=}")
        return super().__getattribute__(*args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        print(f"__setattr {args=}, {kwargs=}")
        super().__setattr__(*args, **kwargs)

    def __delattr__(self, *args, **kwargs):
        print(f"__delattr {args=}, {kwargs=}")
        super().__delattr__(*args, **kwargs)

    def __getattr__(self, *args, **kwargs):
        print(f"__getattr {args=}, {kwargs=}")
        return super().__getattr__(*args, **kwargs)
