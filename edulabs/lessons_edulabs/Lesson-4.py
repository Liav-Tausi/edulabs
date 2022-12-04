
# drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea']
# new_drinks = []
# for i in drinks:
#     if 'i' not in i:
#        new = new_drinks.append(i)
# print(new_drinks)


# taking out items from list without creating new list
# drinks = ['juice', 'wine', 'beer', 'coca-cola',
#           'sprite', 'martini', 'coffee', 'tea']
# indices_to_remove = []
# for i, drink in enumerate(drinks):
#     if "i" in drink:
#         indices_to_remove.append(i)
#
# indices_to_remove.sort(reverse=True)
# for i in indices_to_remove:
#     drinks.pop(i)
# print(drinks)


# taking out items from list without creating new list
# drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea']
# values_to_remove = []
# for drink in drinks:
#     if "i" in drink:
#         values_to_remove.append(drink)
#
# for val_to_remove in values_to_remove:
#     drinks.remove(val_to_remove)
# print(drinks)


# functions
# def print_greeting():
#     print('hello world')
#

# year = int(input("insert a year: "))
# is_leap = is_leap_year(year)
# if is_leap:
#     print("Leap year")
# else:
#     print("Regular year")


# def print_greeting_name(name: str, last_name: str) -> str:
#     print_greeting()
#     print(f"hello {name} {last_name}")
#
# print_greeting_name('liav','Tausi')

# def is_leap_year(year: int) -> int:
#     not_leap = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)
#     # print(f"not_leap: {not_leap}")
#     return not not_leap
#
# def is_31_days_month(month: int) -> int:
#     months = (1, 3, 5, 7, 8, 10, 12)
#     if month in months:
#         return True
#
# print(is_31_days_month(1))
#
# def how_manny_days(month: int , year: int) -> int:
#     if is_31_days_month(month) is True:
#         return 31
#     elif month == 2 or is_leap_year(year):
#         return 28
#     else:
#         return 30
#
# month = int(input('Enter a month: '))
# year = int(input('Enter a year: '))
# print(f"Days number: {how_manny_days(month,year)}")

# def sum_list(numbers: list) -> float:
#     sum = 0
#     for i in numbers:
#         sum += i
#     return sum
#
# liav = [1,2,4,5,6,8]
# print(sum_list(liav))





# a: str ='blabla'
# num: int = 6
# my_list: list = []
# my_tuple: tuple = ()
# tt: float = 7.7



# Write a Python function to check whether a string is a pangram or not. Pangrams are words or
# sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"
# def is_paragram(text: str) -> bool:
#     alphabet: tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
#     for i in text:
#         return i not in alphabet
#
# print(is_paragram('The quick brown fox jumps over the lazy dog'))




# def sum_of_list(list_of_nums: list) -> int:
#     return sum(list_of_nums)
#
# print(sum_of_list([1,2,3,4,5,5]))



# Write a Python function to multiply all the numbers in a tuple.
# def mull_t(mull_tuple: tuple) -> float:
#      sum: int = 1
#      for i in mull_tuple:
#          sum *= i
#      return sum
# print(mull_t((56,5)))



# Write a Python function to find the Max of three numbers
# def bigger_num(f1: float, f2: float, f3: float) -> float:
#     return max((f1,f2,f3))
#
# print(bigger_num(1.23,0.4523,1.2))



# Write a Python function to calculate the factorial of a number (a non-negative integer
# def sum_factorial(numbers: int) -> int:
#     sum = 1
#     for i in range(1,numbers):
#         sum *= i
#     return sum
# print(sum_factorial(4))



# def passing_tuple_elements(new_tuple: tuple) ->tuple:
#
#
# Write a Python function that takes a list and removes all the duplicate elements from the list
# tausi = ["liav","liav","oran","aviv","ilan",]
# def list_pop_dups(dupes_list: list) -> list:
#     return list(set(dupes_list))
# print(list_pop_dups(tausi))



# tausi = ["liav","liav","oran","aviv","ilan",]
# def list_pop_dups(dupes_list: list) -> list:
#     for j,i in enumerate(dupes_list):
#         if i not in dupes_list[:j]:
#             return dupes_list[:j]
# print(list_pop_dups(tausi))



# Write a Python program that prints the even numbers from a given list.
# nums = [189898,25345,54353,3432,5454,]
# def print_even(even_nums: list) -> int:
#     for i in even_nums:
#         if (i % 2) == 0:
#             print(i)
#         else:
#             continue
# print_even(nums)



# def test_prime(num: int) -> bool:
#     if (num==1):
#         return False
#     elif (num==2):
#         return True
#     else:
#         for i in range(2,num):
#             if(num % i==0):
#                 return False
#         return True
# print(test_prime(97))



# Write a function that receives the string as a parameter and return the string in reverse order.
# def reversed_func(rev: str) -> str:
#     return rev[::-1]



# Write a Python function to check whether a number falls in a given range.
# (The function receives number and range (from/to) as parameters and returns True/False)
# def check_num(num:int,form: int,to: int) -> int:
#     return num in range(form,to)
# print(check_num(5,5,12))



# Write a function that receives a hyphen-separated sequence of words
# as a parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically
# def alphabetically_sort(sequence_of_words: str) -> list:
#     alphabet_sorted: list = []
#     alphabet: tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#                         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z' )
#
#     split_sort: list = sequence_of_words.split('-')
#     for j,indx in enumerate(alphabet):
#         for i in sequence_of_words:
#             if sequence_of_words[i].startswith(indx):
#                 alphabet_sorted.append(j)
#                 return alphabet_sorted
#
#
# print(alphabetically_sort('zviv-liav'))



# def alphabetically_sort(sequence_of_words: str) -> str:
#     lst=[n for n in sequence_of_words.split('-')]
#     lst.sort()
#     return '-'.join(lst)
# print( alphabetically_sort('green-red-yellow-black-white'))



words = []
start: bool = True
while start:
    word: str = input('Append words: ')
    words.append(word)
    if word == '$':
        start = False
    else:
        pass



# def search_insert(place: int, serch_words: str) -> str:
#     for place in words:
#             return place
#
# word: str = input('insert the word your looking for: ')
# place: int = int(input('insert the index your looking for: '))
# print(search_insert(place,word))



# Write a Python function that receives a string as a parameter
# and calculates the number of upper case letters and lowercase letters. (The function should return 2 numbers)
# def check_str(str_input: str) -> tuple:
#     up: int = 0
#     low: int = 0
#     for i in str_input:
#          if i.isupper():
#              up += 1
#          elif i.islower():
#              low += 1
#          else:
#              continue
#     return up , low
#
# print(check_str('Hello World'))



# def is_palindrome(word: str) -> bool:
#     return word[::-1] == word
#
#
# print(is_palindrome('girsffsrig'))



# def square(num: int) -> int:
#     for i in range(1,num+1):
#        print(i*i)
# square(30)



# Write a Python function to check whether a number is perfect or not.
# def is_perfect(num: int) -> bool:
#     sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             sum += i
#     return sum == num
# print(is_perfect(28))



# exec("print('hello') ")



# def add(*numbers: int) -> tuple:
#     print(numbers)
#     print(sum(numbers))
# add(1,2,3,4,5)



# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# def two_sum(nums: list, target: int) -> list:
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[j] == target - nums[i]:
#                 return [i, j]
#
# print(two_sum([2,6,3,4,3],9))








