from datetime import datetime
import string

# 1 Implement a function that receives a list of english letters and returns a list with alphabet indexes of the letters in the English Alphabet.
# Use map() to map a letter from the English alphabet to its alphabet index.
#
#
# def index_func(letter) -> int:
#     if letter in string.ascii_uppercase:
#         return string.ascii_uppercase.find(letter) + 1
#     elif letter in string.ascii_lowercase:
#         return string.ascii_lowercase.find(letter) + 1
#     else:
#         raise Exception(f"{letter} is not in the alphabet")
#
#
# def alfa_index(alphabet_input: list[str]) -> list[int]:
#     return list(map(index_func, alphabet_input))
#
#
# if __name__ == "__main__":
#     try:
#         print(alfa_index(["a", "z", "C", "e"]))
#         print(alfa_index(["a", "Blah", "C", "e"]))
#     except Exception:
#         print("Error")



# 2 mplement a function that filters out vowels from the given string and returns the original string without the vowels.
# Vowels are the following letters (both lowercase and uppercase):
#
#
# def filter_vowels(word):
#     return "".join(filter(lambda c: c not in 'aeiouAEIOU', word))
#
#
# if __name__ == "__main__":
#    print(filter_vowels("hello world"))



# 3 Implement a function that gets a list of strings that represent dates in format dd-mm-yyyy.
# Use map() and filter() to filter from this list all the dates that are Fridays and Saturdays
#
#
# def filter_dates(dates):
#     dates = map(lambda s: datetime.strptime(s, '%d-%m-%Y'), dates)
#     return filter(lambda d: d.weekday() in (4, 5), dates)
#
#
# if __name__ == "__main__":
#     print(filter_dates(['12-12-2021', '18-12-2021', '19-12-2021]))



# 4  Implement a function that receives a list of strings,
# and returns a new list of strings with all the original strings sorted by the string length.
#
#
# def sort_strings_by_length(strings):
#     return sorted(strings, key=len)
#
# if __name__ == "__main__":
#     print(sort_strings_by_length("fefefefefe", "fefefefe"))



# 5 Implement a function that gets a dictionary of the format below and returns it's elements sorted first by status (great - good - bad)
# , then by total minutes late, then by name.

# buses = [
#     {
#         "delays": ['1h 20m', '25m', '3h', '2h 1m'],
#         "status": 'bad',
#         "name": "Jacob",
#         "route_num": 560
#     },
#     {
#         "delays": ['20m', '5m', '3h'],
#         "status": 'great',
#         "name": "Moshe",
#         "route_num": 769
#     },
#     {
#         "delays": ['2h 3m'],
#         "status": 'good',
#         "name": "Jack",
#         "route_num": 766
#     },
#     {
#         "delays": ['6h'],
#         "status": 'great',
#         "name": "Mark",
#         "route_num": 876
#     },
#     {
#         "delays": ['2h 3m'],
#         "status": 'good',
#         "name": "Anna",
#         "route_num": 456
#     },
# ]
#
#
# def get_total_delay_mins(bus: dict):
#     delay_sum = 0
#     for delay in bus['delays']:
#         d = delay.split()
#         for ts in d:
#             if 'h' in ts:
#                 delay_sum += int(ts[:ts.index('h')]) * 60
#             if 'm' in ts:
#                 delay_sum += int(ts[:ts.index('m')])
#
#     return -delay_sum
#
#
# def sorting() -> list[dict]:
#     return sorted(buses, key=lambda bus: (len(bus['status']), get_total_delay_mins, bus['name']), reverse=True)
#
#
# if __name__ == "__main__":
#     print(sorting())

# 6 Use lambda and filter/map/sort. Given a list of strings, filter out those containing less than 2 "a" chars
# def sorting(strings):
#     filtered_strings = filter(lambda x: x.count('a') >= 2, strings)
#     return list(filtered_strings)
#
#
# if __name__ == "__main__":
#     print(sorting(["apple", "ananas", "banana", "pear"]))
