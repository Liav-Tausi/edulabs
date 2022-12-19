from datetime import datetime
from calendar import monthrange

# date iterator, gets a date and returns the days until end of month

class DateIterator:

    def __init__(self, date: str):
        self.date = datetime.strptime(date, "%d-%m-%Y").date()
        self.days_in_month = monthrange(self.date.year, self.date.month)[1]

    def __iter__(self):
        self.start = int(self.date.day)
        return self

    def __next__(self):
        if self.start < self.days_in_month:
            self.start += 1
        else:
            raise StopIteration
        return datetime(day=self.start, month=self.date.month, year=self.date.year).date()


if __name__ == "__main__":
    for i in DateIterator("10-04-2002"):
        print(i)


