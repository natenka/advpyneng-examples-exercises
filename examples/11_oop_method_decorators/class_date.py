class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_str(cls, date_as_str):
        day, month, year = list(map(int, date_as_str.split(":")))
        return cls(day, month, year)

    def __repr__(self):
        return f"Date('{self.day}, {self.month}, {self.year}')"
