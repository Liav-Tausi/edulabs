from datetime import datetime
from calendar import monthrange


# 1 Rewrite DateIterator from D2 - iterators as generator

def date_generator(date_str: str) -> datetime.date:
    date: datetime.date = datetime.strptime(date_str, "%d-%m-%Y").date()
    days_in_month: int = monthrange(date.year, date.month)[1]
    val = (i + 1 for i in range(date.day, days_in_month))
    for j in val:
        dates: date = datetime(day=j, month=date.month, year=date.year).date()
        yield dates


if __name__ == "__main__":
    print(list(date_generator("10-04-2002")))


# 2 Write generator batches(n, my_list) that returns batches of length n of the given list

def butches(n, my_list):
    for i in range(0, len(my_list), n):
        yield my_list[i:i + n]


if __name__ == "__main__":
    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(butches(2, numbers_list)))


# 3 Implement generator fib that yields infinite Fibonacci sequence


# xn = xn−1 + xn−2
def fib_generator(end_num: int = 100) -> list:
    x: int = 0
    e: int = 1
    for i in range(0, end_num):
        yield x
        x, e = e, x + e


if __name__ == "__main__":
    print(list(fib_generator(20)))
