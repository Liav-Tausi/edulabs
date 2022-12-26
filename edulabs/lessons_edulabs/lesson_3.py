#
# grades = [19, 34,76]
# i = 0
# while i < len(grades): #no <=
#     print(grades[i])
#     i += 1
#
#
# num1 = int(input("Insert num 1: "))
# num2 = int(input("Insert num 2: "))
# num3 = int(input("Insert num 3: "))
#
# min_num , middle_num , max_num = None, None, None
#
# if num1 <= num2 and num1 <= num3:
#     min_num = num1
#     if num2 < num3:
#         middle_num, max_num = num2, num3
#     else:
#         middle_num, max_num = num3, num2
# elif num2 <= num1 and num2 <= num3:
#     min_num = num2
#     if num1 < num3:
#         middle_num, max_num = num1, num3
#     else:
#         middle_num, max_num = num3, num1
# else:
#     min_num = num3
#     if num1 < num2:
#         middle_num, max_num = num1, num2
#     else:
#         middle_num, max_num = num2, num1
#
# print(min_num, middle_num, max_num)
#
#
# grades = [19, 34, 65, 76]
# for grade in grades:
#     print(f'The grade is: {grade}')
#
#
# grades = [19, 34, 65, 76]
# for i, grade in enumerate(grades):
#     print(f'The grade is:{i+1} {grade}')
#
# text = 'hello world'
# text_split = text.split(' ')
# for char in text_split:
#     print(f'The grade is: {char}')
#
#
# liav = [1 , 2, 3]
# for i in range(len(liav)-1,-1,-1):
#     print(liav[i], end=' ')
#
#
# for j, i in enumerate(range(10,-1,-1)):
#     print(f"{j+1}-{i+1}")
#
#
# for i in range(1,4):
#     num = input('insert a number: ')
#     while not num.isdigit():
#         num = input('Try again: ')
#     print(f'Nomber {i} is {int(num)}')
#
#
# for i in range(1,4):
#     num = input('insert a number: ')
#     while not num.isdigit():
#         num = input('Try again: ')
#     num = int(num)
#     while num < 1 or num > 31:
#         num = input('insert a num between 1 ... 31: ')
#         num = int(num)
#     print(f'Nomber {i} is {int(num)}')
#
#
# for i in range(1,4):
#     num = input('insert a number: ')
#     while not num.isdigit() and int(num) < 1 or int(num) > 31:
#         num = input('Try again! insert a num between 1 ... 31: ')
#     print(f'Nomber {i} is {int(num)}')
#
#
# num = int(input("give me a number: "))
# for i in range(0,num):
#     print('')
#     for j in range(i+1):
#         print('*', end=' ')


#
# num = int(input("Enter a number: "))
# for i in range(num+1):
#     for j in range(i):
#         print("*", end = " ")
#     print(" ")
# for s in range((num-2),-1,-1):
#     for j in range(s,-1,-1):
#             print("*", end=" ")
#     print(" ")



# num1=None
# print(id(num1))
# num=True
# print(id(num))



# names = []
# grades = []
# for name_index in range(3):
#     grades.append([])
#     names.append(input('insert a name: '))
#     for grade_index in range(2):
#         grades[name_index].append(int(input('insert a grade: ')))
# print(names , grades)



# names = ["liav","liav","liav"]
# names1 = names.copy()
# names2 = names
# print(names is names2)
# print(names is names1)



# Display Fibonacci series up to 10 terms.
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it
# num1, num2 = 0, 1
# for i in range(10):
#     temp = num1
#     num1 = num2
#     num2 += temp
#     print(temp, end=' ')



# Use a loop to display elements from a given list present at odd index positions.
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(1,len(my_list),2):
#         print(my_list[i], end=" ")



# Given two lists - one with city names, and one with country names,
# print pairs with country-city. You can assume that the lists are of the same length
# cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
# countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']
#
# for i in range(len(cities)):
#     print(f"{cities[i]}-{countries[i]}")



# Calculate the cube of all numbers from 1 to a given number
# num = int(input("Give me a Number: "))
# for j in range(1, num+1):
#      print(f"number: {j} cubed: {pow(j, 3)}")
#


# Find the sum of the series up to n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become
# number_of_terms = int(input('Number please: '))
# sum1=0
# for i in range (1,number_of_terms+1):
#     num=eval('2'*i)
#     sum1+=num
# print(sum1)



# You have a list of names. Using a for loop append each item with a Dr. prefix,
# and insert the new strings in a new list.
# Print the result list.
# names = ['Moshe', 'Orly', 'David', 'Jack', 'Ofer', 'James']
# for i in range(len(names)):
#     names[i] = ' '.join(['Dr.', names[i]])
# print(names)



# Write a program that receives an integer number from a user and appends
# squares of the numbers starting from 1 up to the number inserted by a user to a new list.
# Print the new list with the squares
# nums = []
# num = int(input('Give me a Number: '))
# for i in range(1,num+1):
#     mull = i*i
#     nums.append(mull)
# print(nums)



# Given a list with elements of various types, create a new list that will store only positive integers. Print the list.
# various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
# positive = []
# for i in various:
#        if (type(i) is int or type(i) is float) and i > 0:
#         positive.append(i)
# print(positive)



# Write a program to count the number of even and odd numbers from a given list of numbers
# num = [132323, 245454, 3433, 3, 343,434]
# for i in range(len(num)):
#     if (num[i]%2) == 0:
#         print(f'{num[i]} is even')
#     else:
#         print(f'{num[i]} is odd')



## Write a program that prints each item and its corresponding type from the given list.
# For example, given the list
# li_st = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
# for i in li_st:
#         print("Type of:",i,"is",type(i))



# Write a Python program which iterates the integers from 1 to 50.
# For multiples of three print "Fizz" instead
# of the number and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     print(i)



# Write a program that receives as input 2 numbers - rows and columns, and prints a rectangle of $ with received dimensions.
rows = int(input("Enter number of Rows: "))
columns = int(input("Enter number of columns: "))
for i in range(rows):
   for i in range(columns):
       print("$",end="")
   print(" ")


## Write a program that receives a number from a user and constructs the following pattern, using a nested loop.
# num = int(input("Enter a number: "))
# for i in range(num+1):
#     for j in range(i):
#         print(i, end = "")
#     print(" ")



## Write a program that receives a number from a user and calculates the sum of all numbers from 1 to a given number
# num = int(input('Give me a Number: '))
# sum = 0
# for i in range(1,num+1,1):
#     sum = i+i
#     print(sum)



## Write a program that receives a list of numbers, and prints the minimum number
# nums = [1,6,3,7,232,8,78,121]
# print(f"min number in {nums}\tis\t:\t{min(nums)}")



# Write a number that receives a list of numbers, and finds the second-largest number
# nums = [1,6,3,7,232,8,78,121]
# min_nums_li = []
# min_num = min(nums)
# nums.remove(min_num)
# print(f'{min(nums)}')



# Print list in reverse order using a for loop
# nums = [1,6,3,7,232,8,78,121]
# rev = []
# for i in reversed(nums):
#     rev.append(i)
# print(rev)



# Get 10 dates from the user. The date is in the following format: dd.mm.yyyy (no need to check.
# After you get all the 10 dates, print the amount of dates in winter, autumn, sprint, summer,
# and print the dates themselves.
# dates = []
# for i in range(10):
#     date = (input('Give me a Date: '))
#     date_s = date.split('.')
#     dates.append(int(date_s[0]))
#     dates.append(int(date_s[1]))
#     dates.append(int(date_s[2]))
#     days = dates[0::2]
#     months = dates[1::2]
#     years = dates[2::3]
#     if months[0] == 12 or months[0] in range(1,3):
#         print(f'its the {days[0]} and its winter in {years[0]}')
#     elif months[0] in range(3,6):
#         print(f'its the {days[0]} and its spring in {years[0]}')
#     elif months[0] in range(6,9):
#         print(f'its the {days[0]} and its summer in {years[0]}')
#     elif months[0] == 9 or  months[0] == 10 or months[0] == 11:
#         print(f'its the {days[0]} and its autumm in {years[0]}')
#



#Find the factorial of a given number.
# Take into account that factorial of 0 is 1, and factorial does not exist for negative numbers
# fac = 1
# num = int(input('Give me a Number: '))
# if num < 0:
#    print("factorial does not exist for negative numbers")
# elif num == 0:
#    print(f"The factorial of {num} is 1")
# else:
#    for i in range(1,num + 1):
#        fac *= i
#    print(f"The factorial of {num} is {fac} ")



# Write a program that receives a number from a user and prints a multiplication table of a given number
# num = int(input('Give me a Number:  '))
# print(f'\t num inserted: {num}')
# for i in range(1,num+1):
#     print(f'\t\t{i}*{num} = {num*i}')



# Write a program that receives rows number and prints the following number pattern:
# num = int(input('Row Number: '))
# for i in range(1,num + 1):
#     for j in range(i):
#        print(f'{i}\t', end="")
#     print(" ")


# Python program to display all the prime numbers within an interval
# num = int(input('Give me a Number: '))
# for i in range(1,num+1):
#     if i > 1:
#         for j in range(2,i):
#             if (i% j) == 0:
#                 break
#         else:
#             print(i)


# Write a program that receives a number from a user and prints the following start pattern.
# For example, for input 5, you should print:
# num = int(input("Enter a number: "))
# for i in range(num+1):
#     for j in range(i):
#         print("*", end = " ")
#     print(" ")
# for s in range((num-2),-1,-1):
#     for j in range(s,-1,-1):
#             print("*", end=" ")
#     print(" ")



# You get a list of lists of strings (like the one defined above).
# Write programs that perform the following operations (separate program for each bullet)
# goods = [['apple', 'pear', 'peach', 'chery'],
#          ['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
#         'bayberry', 'blueberry', 'cloudberry', 'raspberry', 'blackberry']]
#
# longest_name = ""
# external_idx = -1
# internal_idx = -1
# max_inner_len = 0
#
# for inx, fruits_list in enumerate(goods):
#     for j, fruit_str in enumerate(fruits_list):
#         fruit_len = len(fruit_str)
#         if fruit_len > max_inner_len:
#             max_inner_len = fruit_len
#             longest_name = fruit_str
#             external_idx = inx
#             internal_idx = j
#
# print(longest_name, max_inner_len, external_idx, internal_idx)




