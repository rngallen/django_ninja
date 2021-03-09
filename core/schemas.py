import datetime
from ninja import Schema


class PathDate(Schema):
    year: int
    month: int
    day: int

    def value(self):
        return datetime.date(self.year, self.month, self.date)


class Filters(Schema):
    limit: int = 100
    offset: int = None
    query: str = None


class Item(Schema):
    name: str
    description: str = None
    price: float
    quantity: int
