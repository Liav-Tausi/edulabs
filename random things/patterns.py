# Write a program that receives rows number  and prints the following number pattern:
# num = int(input('Row Number: '))
# for i in range(1,num + 1):
#     for j in range(i):
#        print(f'{i}\t', end="")
#     print(" ")



# Write a program that receives as input 2 numbers - rows and columns, and prints a rectangle of $ with received dimensions.
# rows = int(input("Enter number of Rows: "))
# columns = int(input("Enter number of columns: "))
# for i in range(rows):
#    for i in range(columns):
#        print("$",end="")
#    print(" ")


# left pyramid pattern
# num = int(input("Enter a number: "))
# for i in range(num+1):
#     for j in range(i):
#         print("*", end = " ")
#     print(" ")
# for s in range((num-2),-1,-1):
#     for j in range(s,-1,-1):
#             print("*", end=" ")
#     print(" ")



# Pyramid pattern
# rows = int(input("Enter number of rows: "))
# l = 0
# for i in range(1, rows + 1):
#     for space in range(1, (rows - i) + 1):
#         print(end="  ")
#     while l != (2 * i - 1):
#         print("* ", end="")
#         l += 1
#     l = 0
#     print()



# Right Triangle Star Pattern
# num = int(input('Give me a Number: '))
# for i in range(num+1):
#     for j in range(i):
#         print('*', end="")
#     print()
#
#
# d = 0
# num = int(input('Give me a Number: '))
# for i in range(num):
#     print(end=" ")
#     for j in range(1,(num+1)):
#         print("*" ,end="")
#     while d != i:
#         print()
#     d += 1
#     print()




# Downward Triangle Star Pattern
# num = int(input('Give me a Number: '))
# for i in range(1,num+1):
#     for j in range(1,(num-i)+1):
#         print("*" ,end="")
#     print()
#
#




