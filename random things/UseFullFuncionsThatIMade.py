from datetime import datetime
from calendar import monthrange

# date iterator, gets a date and returns the days until end of month
def date_generator(date_str: str) -> datetime.date:
    date: datetime.date = datetime.strptime(date_str, "%d-%m-%Y").date()
    days_in_month = monthrange(date.year, date.month)[1]
    val = (i + 1 for i in range(date.day, days_in_month))
    for j in val:
        dates: date = datetime(day=j, month=date.month, year=date.year).date()
        yield dates

