class Time:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        year, month, day = [int(i) for i in date_str.split(":")]
        return cls(year, month, day)

    # from_string = classmethod(from_string)
