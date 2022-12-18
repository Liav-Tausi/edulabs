# import datetime
#
# # A lambda function is a small anonymous function.
# # A lambda function can take any number of arguments, but can only have one expression.
#
# # mapping numbers to theirs squares
# def sq(x):
#     return x**2
# # equivalent
# sq1 = lambda x: x**2
#
# list(map(lambda x: x**2, [1,2,3,4]))
#
# list(map(lambda x, y :x*y, [1, 3, 5], [2, 4, 6]))
#
# # From buses - print only bus routes using lambda
#
# print(list(map(lambda bus: bus['route_num'], buses_list)))
#
# # Back to ex with dates - rewrite with lambdas
#
# from datetime import datetime
# def map_to_date(date_as_str):
#     return datetime.strptime(date_as_str, "%d-%m-%Y")
#
# def filter_days(date_obj):
#     return date_obj.weekday() not in (4, 5)
#
# print(list(filter(filter_days, map(map_to_date, ['12-12-2021', '18-12-2021', '19-12-2021']))))
#
# print(
#     list(
#         filter(
#             lambda date_obj: date_obj.weekday() not in (4, 5),
#             map(
#                 lambda date_as_str: datetime.strptime(date_as_str, "%d-%m-%Y"),
#                 ['12-12-2021', '18-12-2021', '19-12-2021']
#             )
#         )
#     )
# )
#
# # # sorted([3, 1, -5, 6, 9])
# # # sorted([3, 1, -5, 6, 9], reverse=True)
# # import datetime
# #
# # students = [
# #     {"name": "Moshe", "grade": 89},
# #     {"name": "David", "grade": 93},
# #     {"name": "Jack", "grade": 73},
# # ]
# # # print(list(sorted(students)))
# #
# #
# # # l = [2, 4, -1, 5]
# # # sorted_list = []
# # # for i in range(len(l), -1, -1):
# # #     # find min
# # #     # m = min(l)
# # #     m = l[0]
# # #     for j in l:
# # #         if j < m:
# # #             m = j
# # #     sorted_list.append(m)
# #
# #
# #
# # def my_key_func(student):
# #     return student["grade"]
# #
# # students = [
# #     {"name": "Moshe", "grade": 89},
# #     {"name": "David", "grade": 93},
# #     {"name": "Jack", "grade": 73},
# # ]
# #
# # # print(sorted(set([3,4,65, 3,4])))
# # print(sorted(students, key=lambda s: s['grade'], reverse=True))
# # #
# # # sorted(students, key=my_key_func, reverse=True)
# #
# #
# # class Vehicle:
# #     def __init__(self, model, km):
# #         self._model = model
# #         self._km = km
# #
# #     def get_km(self):
# #         return self._km
# #
# #     def __repr__(self):
# #         return f"{self._model}, {self._km}"
# #
# #     # def __cmp__(self, other):
# #     #     if self._km < other._km:
# #     #         return -1
# #     #     elif self._km == other._km:
# #     #         return 0
# #     #     else:
# #     #         return 1
# #     #
# #     # def __gt__(self, other):
# #     #     return self._km > other._km
# #     #
# #     # def __lt__(self, other):
# #     #     return self._km < other._km
# #
# # vehicles = [Vehicle('mazda', 1000),
# #             Vehicle('toyota', 50),
# #             Vehicle('mercedes', 30000)]
# #
# #
# # print(sorted(vehicles, key=lambda v: v.get_km()))
# # print(sorted(vehicles, key=lambda v: v._model, reverse=True))
# #
# # # List elements: (Student's Name, Grade, Age)
# # # sort first by highest grade, then smallest age
# #
# # participant_list = [
# #     ('Alison', 50, 18), #4
# #     ('Terence', 75, 12), #2
# #     ('David', 75, 20), #3
# #     ('Jimmy', 90, 22), #1
# #     ('John', 45, 12) #5
# # ]
# #
# # (50, 18)
# # (25, 12)
# # (25, 20)
# #
# # print(sorted(participant_list,
# #        key=lambda x: (x[1], x[2])))
# #
# # # comparing tuples
# # print((3, 2) > (1, 4))
# # print((3, 2) > (3, 4))
# # print((3, 2, 1) > (3, 2, 0))
# # print((3, 2, 0) > (3, 2))
# # # "apple" < "amazon"
# #
# # # def multi_key_func(participant):
# # #     return 100 - participant[1], participant[2]
# # #
# # # sorted(participant_list, key=multi_key_func)
# #
# # words = ["sdfdf", "wdda", "re", "sdfgnjfjfku"]
# # sorted(words, key=len)
# #
# # sorted(words, key=lambda w: len(w))
# #
# # my_compare = lambda w: len(w)
# # sorted(words, key=my_compare)
# #
# # def my_best_compare(w):
# #     return len(w)
# # sorted(words, key=my_best_compare)
#
# d1 = "1h 5m"
# tr1: datetime.timedelta = datetime.datetime.strptime(d1, "%Hh %Mm") - \
#       datetime.datetime(year=1900, month=1, day=1)
# print(tr1.total_seconds() // 60)


Skip
to
content
Search or jump
to…
Pull
requests
Issues
Codespaces
Marketplace
Explore


@Liav - Tausi


valeria - a
/
morning - ninjas
Private
Code
Issues
Pull
requests
Actions
Projects
Security
Insights
morning - ninjas / lesson12 / func_map.py /


@valeria - a


valeria - a
lesson
2
eve
Latest
commit
43
c869c
11
hours
ago
History
1
contributor
87
lines(65
sloc)  2
KB


# map(func, *iterables) --> map object
def foo_squared(num):
    return num ** 2


#
# my_list = [1, 3, 5, 6]
#

# ret_val = list(map(foo_squared, my_list))
#
# print(ret_val)
#

my_list = ['Apple is nice', 'baNana is yellow', 'ANANAS']


# for i in my_list:
# do this on element
# do @2 on element

def my_split(elem):
    return elem.split(" ")


def my_get_last(elem: list[str]):
    return elem[-1]


ret_val_from_map = map(my_get_last, map(my_split, map(str.lower, my_list)))
# print(type(ret_val_from_map))
# print(list(ret_val_from_map))
# for i in ret_val_from_map:
#     print(i)

# print(list(ret_val_from_map))

# list(my_list)


# print(list(map(str.lower, ['Apple', 'baNana', 'ANANAS'])))


# you can also pass multiple iterators to map
# def foo_sum(*args):
#     return sum(args)
#
# my_tuple1, my_tuple2 = (1, 2, 3, 4), (10, 20, 30, 40)
# ret_val = map(foo_sum, my_tuple1, my_tuple2, [100, 200, 300, 400])
# print(list(ret_val))


# we want any number of params
# def s(*args):
#     ret_val = 0
#     for a in args:
#         ret_val += a
#     return ret_val
#
# ret_val = map(s, my_tuple1, my_tuple2, (100, 200, 300, 400))
# print(list(ret_val))

# you can pass any existing function, or functions defined in class (method)
# example - map to upper case
# ret_val = map(str.upper, ['a', 'bb', 'ccc'])
# ret_val = map(lambda x: x.upper(), ['a', 'bb', 'ccc'])
# ret_val = []
# for i in ['a', 'bb', 'ccc']:
#     ret_val.append(i.upper())
# print(list(ret_val))


# my_list = ['Apple is nice', 'baNana is yellow', 'ANANAS']


# def my_split(elem):
#     return elem.split(" ")
#
#
# my_split = lambda elem: elem.split(" ")
#
#
# def my_get_last(elem: list[str]):
#     return elem[-1]
#     # if 'a' in elem[-1]:
#     #     return elem[-1]
#     # else:
#     #     return elem[0]
#     # return elem[-1] if 'a' in elem[-1] else elem[0]
#
#
# # ret_val_from_map = map(my_get_last, map(my_split, map(str.lower, my_list)))
# ret_val_from_map = map(lambda x: x[-1],
#                        map(lambda x: x.split(" "),
#                            map(str.lower, my_list)))
