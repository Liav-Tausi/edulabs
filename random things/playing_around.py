import time


#
# def greeting_decorator(other_func):
#     def printing(*args, **kwargs):
#         print("hello")
#
#         result = other_func(*args, **kwargs)
#
#         print("bye")
#         return result
#
#     return printing
#
#
# @greeting_decorator
# def cubed(num):
#     return num ** 2
#
#
# print(cubed(5))


# def performance_log_decorator(time_units="s"):
#     def wrapper(other_function):
#
#         def time_check(*args, **kwargs):
#             if type(time_units) is not str:
#                 raise KeyError(f'{time_units} is not time unit')
#             val = time_units.lower()
#             if val not in ["s", "ms", "ns"]:
#                 raise Exception("Unit provided not supported.")
#             if val == "ms":
#                 unit = 1000
#             elif val == "ns":
#                 unit = 1000000000
#             else:
#                 unit = 1
#             start: time = time.perf_counter_ns()
#             result = other_function(*args, **kwargs)
#             end: time = time.perf_counter()
#             print(f"{other_function.__name__} took {(end - start) * unit}")
#             return result
#
#         return time_check
#
#     return wrapper
#
#
# @performance_log_decorator(time_units="ms")
# def long_running_func(num, iters):
#     val = 1
#     for i in range(iters):
#         val *= num
#     return val
#
#
# if __name__ == "__main__":
#     print(long_running_func(3, 2))

