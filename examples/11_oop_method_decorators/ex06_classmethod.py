class Datetime:
    def __init__(self, year=None, month=None, day=None):
        print("__init__")
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_str(cls, date_str):
        print(f"{cls=}")
        date = [int(i) for i in date_str.split()]
        return cls(*date)

    def __repr__(self):
        return f"Datetime('..')"


d1 = Datetime(2021, 10, 31)
d1.from_str("2021 10 31")
d2 = Datetime.from_str("2021 10 31")


# d1.method(args)
# Datetime.method(d1, args)
