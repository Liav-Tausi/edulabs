
# #1
# num = int(input('give num:' ))
# if num < 10:
#   print('1 digits')
# elif num < 100:
#   print('2 digits')
# elif num >= 100 < 1000:
#   print('3 digits')


# #2
# num1 = int(input('number 1: '))
# num2 = int(input('number 2: '))
# num3 = int(input('number 3: '))
# num_list = [num1, num2 ,num3]
# num_list.sort()
# print(num_list)

# #3
# age = int(input('what is your age? '))
# height = int(input('what is your height? '))
# if age <= 18 >-8 and height >= 115:
#   print('have fun!')
# elif age > 18 and height >= 100:
#   print('have fun')
# else:
#   print('sorry, you cannot ride :(')

# #4
# player_one = input("player 1's turn: ")
# player_two = input("player 2's turn: ")
#
# if player_one or player_two == 'paper' or 'rock' or 'scissors':
#     print('1..2..3')
# else:
#     print('invalid play')
#
# if player_one == player_two:
#  print('Its a Drow!')
#
# if player_one != player_two:
#     if player_one == 'paper' and player_two == 'rock':
#        print('Player one Wins!')
#     elif player_one == 'rock' and player_two == 'scissors':
#        print('Player one Wins!')
#     elif player_one == 'scissors' and player_two == 'paper':
#        print('Player one Wins!')
#     else:
#        print('Player one Lost!')
#
#     if player_two == 'paper' and player_one == 'rock':
#         print('Player two Wins!')
#     elif player_two == 'rock' and player_one == 'scissors':
#         print('Player two Wins!')
#     elif player_two == 'scissors' and player_one == 'paper':
#         print('Player two Wins!')
#     else:
#         print('Player two Lost!')
# else:
#  print('invalid turn')

# #6
# day = int(input('day? '))
# month = int(input("month's number? "))
# year = int(input('year? '))

# if day >= 20 <=31 and month == 6:
#   print("it's march and its spring")
# elif day >= 21 <=30 and month == 7:
#   print("it's june and its summer")
# elif day >= 22 <=30 and month >= 8 <=9:
#   print("it's autum")
# elif day >= 22 <=30 and month == 10:
#   print("it's winter")
# else:
#   print('invalid date')

# #7
# year = int(input('Year: '))
# year_leep = ((year % 4) == 0) and ((year % 100) != 0 or (year % 400) == 0)
# print(year_leep)

# #8
# m_inc = int(input('insert your monthly salary: '))
# a_inc = m_inc * 12
# first_tax = (0.1 * 77400)
# sec_tax = (0.14 * 110880) + (0.1 * 77400)
# third_tax = (0.2 * 178080) + (0.14 * 110880) + (0.1 * 77400)
# forth_tax = (0.31 * 247440) + (0.2 * 178080) + (0.14 * 110880) + (0.1 * 77400)
# fifth_tax = (0.47 * 514920) + (0.31 * 247440) + (0.2 * 178080) + (0.14 * 110880) + (0.1 * 77400)
# sixth_tax = (0.5 * 663240) + (0.47 * 514920) + (0.31 * 247440) + (0.2 * 178080) + (0.14 * 110880) + (0.1 * 77400)
#
#
# if a_inc <= 77400 >= 0:
#     print(float(0.1 * 77400))
# elif a_inc >= 77401 <= 110880:
#     print(float(0.14 * (a_inc - 77401)) + first_tax)
# elif a_inc >= 110881 <= 178080:
#     print(float(0.2 * (a_inc - 110881)) + sec_tax)
# elif a_inc >= 178081 <= 247440:
#     print(float(0.31 * (a_inc - 178081)) + third_tax)
# elif a_inc >= 247441 <= 514920:
#     print(float(0.31 * (a_inc - 247441)) + forth_tax)
# elif a_inc >= 514921 <= 663240:
#     print(float(0.47 * (a_inc - 514921)) + fifth_tax)
# elif a_inc <= 663241:
#     print(float(0.5 * (a_inc - 663240)) + sixth_tax)

# #9
# temp = int(input('what is the temperature? '))
# wether = input('what is the wether like?')

# #10
# storge = int(input('amount: '))
# unit = int(input('unit: '))
# user_unit = int(input('convert to: '))
# bytes = 'by'
# kb = 'kb'
# gb = 'gb'
# mb = 'mb'
# tb = 'tb'


# if user_unit == bytes:
#   result = storge * 1024
#   print(int(result))

# #1
# width = int(input("insert width? "))
# height = int(input("insert height? "))
# perimeter = (width + height) * 2
# print("the primeter is:", perimeter)

#2
# celsius = input("temperature: ")
# fahrenheit = int(celsius) - 32 * 0.5556
# print(fahrenheit)

# #3
# num1 = int(input('first number: '))
# num2 = int(input('secend number: '))
# sum= num1 + num2
# mul= num1 * num2
# print( ('the sum is:'),sum, ('the multiplication is:'),mul)


##4
# name = str(input('what is your name? '))
# age = int(input('what is your age? '))
# year = 2022 - age
# print(name,',','your birth year was: ',year)


## 5
# num = int(input('number: '))
# if ((num % 2) == 0):
#   print('even')
# else:
#   print('odd')

##6
# num1 = int(input('first number: '))
# num2 = int(input('second number: '))
# result = num1 // num2
# print(result)

##7
# num = input('4 digits plz:  ')
# print( 'first number:',num[0])
# print('last number:',num[3])

##8
# salary = int(input("your salary: "))
# amount = 0.14 * salary
# print(amount)

##9
# current = int(input('current monthly salery: '))
# new_job = int(input('new monthly salery: '))
# new = new_job*12
# cur = current*12
#
# result = new - current
# print('you will ern', result ,'shekels more per year')


# #10-11
# length = int(input('length of the movie: '))
# hours = length // 60
# minutes = length % 60
# secends = minutes % 60
# print('there are',hours,'h and',minutes,'m' ,secends,'s left')

# #11
#
# total_seconds = int(input('length of the movie: '))
# total_minutes = total_seconds // 60
# seconds = total_seconds % 60
# hours = total_minutes // 60
# minutes = total_minutes % 60
# print('The length of the movie is:' ,hours,':',minutes,':',seconds,)

# #4
# drink = input('Drink: ')
# qty = float(input('qty: '))
# can_drive = (drink == 'bear' and qty <= 0.3) or \
#             (drink == 'wine' and qty <= 0.2)
# print("can drive", can_drive)

# print("Twinkle, twinkle, little star,\n\t\t How I wonder what you are!\n\t\t\t "\
#       "Up above the world so high,\n\t\t\t Like a diamond in the"\
# " sky. \nTwinkle, twinkle, little star,\n\t\t How I wonder what you are\n")

# import sys
# print('python version')
# print(sys.version_info)

# import datetime
# now = datetime.datetime.now()
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

# answer = input('how are you? ')
# print(f"you are {answer}")
#
# liav = 0
# while liav < 100_000:
#     liav += 1
# print(liav)

# initial_amount = int(input("Enter storage amount: "))
# initial_unit = input("Enter unit: ")
# num_initial_unit = 4
# new_amount = initial_amount
# new_unit = 'tb'
#
# if initial_amount >= 1 or \
#         initial_unit == 'bytes' or \
#         initial_unit == 'kb' or \
#         initial_unit == 'mb' or \
#         initial_unit == 'gb' or \
#         initial_unit == 'tb':
#     if initial_unit == 'bytes':
#         num_initial_unit = 0
#     elif initial_unit == 'kb':
#         num_initial_unit = 1
#     elif initial_unit == 'mb':
#         num_initial_unit = 2
#     elif initial_unit == 'gb':
#         num_initial_unit = 3
#
#     num_new_unit = num_initial_unit
#
#     if num_new_unit != 4:
#         if new_amount // 1024 >= 1:
#             num_new_unit += 1
#             new_amount /= 1024
#             if new_amount // 1024 >= 1:
#                 num_new_unit += 1
#                 new_amount /= 1024
#                 if new_amount // 1024 >= 1:
#                     num_new_unit += 1
#                     new_amount /= 1024
#                     if new_amount // 1024 >= 1:
#                         num_new_unit += 1
#                         new_amount /= 1024
#
#     new_amount = ((new_amount * 10) // 1) / 10
#
#     if num_new_unit == 0:
#         new_unit = 'bytes'
#     elif num_new_unit == 1:
#         new_unit = 'kb'
#     elif num_new_unit == 2:
#         new_unit = 'mb'
#     elif num_new_unit == 3:
#         new_unit = 'gb'
#
#     print(f"{initial_amount}{initial_unit} is the same as {new_amount}{new_unit}")
# else:
#     print("Invalid Input")



# comics = int(input('how many comic books would you like?'))
# sience = int(input('how many sience books would you like?'))
# history = int(input('how many history books would you like?'))
#
# total_pay = 0
# total_no_discound = (sience * 58 ) + (history * 24) + (comics + 32)
#
# if sience >= 3:
#     total_pay += (sience*32) * 0.9
#
# if history == 2:
#     total_pay += (history * 24) * 0.5
#
# if total_pay >= 300:
#     total_pay += -20



# seat_l = input(('what is layout of the seats: '))
# seat_split = seat_l.split(" ")
#
# if len(seat_split) > 0:
#     first = (len(seat_split[0]))
# if len(seat_split) > 1:
#     secend = (len(seat_split[1]))
# if len(seat_split) > 2:
#     third = (len(seat_split[2]))
# print(first,secend,third )


# count = 0
# grades = []
# grades_sum = 0
# while count < 3:
#     grade = int(input("give grade: "))
#     grades.append(grade)
#     grades_sum += grade
#     count += 1
#
# print(f"grads sum is {grades_sum}")
# print(f"grads avg is {grades_sum / len(grades)}")


# liav = 0
# while liav < 100_000_000:
#     liav+=1
#

# drink_type = input("insert drink: ").lower().strip()
# while drink_type not in ["beer", "wine"]:
#     drink_type = input("incorect you dam dam! beer or wine ").lower().strip()
# print(f"you inserted {drink_type}")


# icorrect_input = True
# while icorrect_input:
#     drink_type = input("insert drink: ").lower().strip()
#     if drink_type in ["beer", "wine"]:
#       icorrect_input = False



# stop = True
# num_list = []
#
# while stop:
#     num = input('Give me numbers: ')
#     num_list.append(num)
#     if num == "$":
#         stop = False
#
# print(max(num_list))
#
#
# end_of_input = False
# temp_max = None
# while not end_of_input:
#     i = input("Insert num or $ to finish: ")
#     if i == '$':
#         end_of_input = True
#     else:
#         num = int(i)
#         if temp_max is None:
#             temp_max = num
#         if num > temp_max:
#             temp_max = num
# print("MAX num", temp_max)

# text = ['liav1', 'liav','2' , 'liav3']
# text_liav = text.insert(2 , 2)
#
# print(text)

# l = [['Paris', 'London', 'New York'], [45, True, 5.5, 'hello'], -3, [5, ['#', '$', '%', '^', [10, 20, 30, 40]]],  [['a'], ['b'], 'c', [['d']]]]

# liav = l[1][2]
# print(liav)

# liav = l[0][::-1]
# print(liav)
#
# liav = l[1:3]
# print(liav)

# liav = l[3][1][3]
# print(liav)

# liav = l[4][0][0]
# print(liav)

# liav = l[4][1][0:1]
# print(liav)

# liav = l[4][3][0][0]
# print(liav)

# liav = l[3][1][4][1]
# hii = l[3][1][4][3]
# print(liav , hii)

# liav = l[3][1][3:4:2]
# liav1 = l[3][1][0:-3:2]
# print(liav,liav1)

# country = input('write a country to get its currency: ').lower().strip()
# eu = 'germany', 'austria','czech','france','italy', 'spain'
#
# def currency_check(country) :
#     match country:
#         case 'usa':
#             print('US dollar')
#         case eu:
#             print('EURO')
#         case 'israel':
#             print('new israeli sheakel')
#         case other:
#             print('i dont know')
#
# currency_check(country)

# word = input('give me a word: ').lower().strip()
# length = len(word)
# print(f"the word is {length} characters long")

# word = input('check for palindrome: ').lower().strip()
# if word[0:] == word[::-1]:
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not palindrome")


# stats = input('give me text: ')
# words = len(stats.split(' '))
# chars = len(stats)
# vowels = stats.count("o") + stats.count("a") + stats.count("e") + stats.count("y") + stats.count("u")
# space = stats.count(' ')
# print(f"there are {words} words and {chars} chars and {vowels} vowels and {space} spaces ")

# word = input('ill tell you if it end with a vowel:')
# vowel = word.endswith(("o","a","u","y","e" ))
# if vowel:
#     print(f'{word} does end with a vowel')
# else:
#     print(f'{word} dosent end with a vowel')

# word = input('give me the seat: ')
# seat_s = word.split(" ")
# if len(seat_s) > 0:
#     first = len(seat_s[0])
# if len(seat_s) > 1:
#     second = len(seat_s[1])
# if len(seat_s) > 2:
#     third = len(seat_s[2])
# print(first,second, third)

# word = input('ill tell you if it has white spaces: ')
# word_v = word.isspace()
# word_c = word.count(" ")
# if word_v is True:
#     print(f"{word_v} there are {word_c} whitespaces")
# else:
#     print(f" not all are whitespaces")
#
# word = input('give me a sentence: ')
# upper = word.title()
# print(upper)



# air_l = input('aircraft layout: ').strip().lower()
# seat_n = input('seat number: ')
#
# if len(seat_n) == 3:
#     row_num = seat_n[0:2]
#     row_l = seat_n[-1]
# else:
#     row_num = seat_n[0]
#     row_l = seat_n[-1]
#
# air_s = air_l.index(row_l)
#
# if air_l.startswith(row_l) or air_l.endswith(row_l):
#     print("\nWindow")
# elif air_l[(air_s)+1] == ' ' or air_l[(air_s)-1] == ' ':
#     print("\nAisle")
# else:
#     print("\nMid plane")
# print(f"row: {row_num}\nseat: {row_l}")
#

# path = input('Give me a path: ').strip()
# back = '\\'
# front = '/'
# path_f = path.count(front)
# path_l = path.count(back)
# path_u_w = path[0].isupper() and path[1] == ':'
# path_u_m = path[1].isupper() and path[0] == '/'
# path_f_end = path.find('.')
#
# if path_u_w:
#     path_w_end = path.split("\\")
#     last_place = path_w_end[-1]
#     place = last_place.split('.')
#     doc = place[0]
#     print(f" 'its a windows machine'\n path is {path_l} folders deep\n file's name: {doc}\n file’s extension: {path[path_f_end:]}")
# if path_u_m:
#     path_m = path.split("/")
#     l_place = path_m[-1]
#     place_m = l_place.split('.')
#     doc_m = place_m[0]
#     print(f" 'its a mac/linox machine'\n path is {path_f} folders deep\n file's name: {doc_m}\n file’s extension: {path[path_f_end:]}")
# else:
#     print("invalid path")


# liav = 0
# while liav < 10:
#     liav += 1
#     print(liav)


# num = 1
# num_user = int(input('give me a number: '))
# while num > 0:
#    num += + 3
#    print(num)
#    if num >= num_user:
#      break

# end_of_input = False
# grades = []
# names = []
# grades_sum = 0
#
# while not end_of_input:
#     name = input('what is your name? ')
#     if name == "$$$":
#         end_of_input = True
#         print(f"list of names:\n{names}\navg:\n{(grades_sum / (len(grades)))}")
#         break
#     else:
#         grade = int(input("what is your grade? "))
#         names_l = names.append(name)
#         grade_l = grades.append(grade)
#         grades_sum += grade

# input_end = False
# input_list = []
# len_man = 0
# digit = letter = 0
#
# while not input_end:
#     li_st = input('Enter Your Word: ')
#     if li_st == '$':
#       print(f"their are {len(input_list)} words\ntheir are {avg_in_list} digits and characters\n{digit} digits\n{letter} characters ")
#       break
#     for ch in li_st:
#         if ch.isdigit():
#           digit += 1
#         elif ch.isalpha():
#             letter += 1
#         else:
#             pass
#     else:
#         input_list.append(li_st)
#         li_st_len = len(li_st)
#         len_man += li_st_len
#         len_sum = len(input_list)
#         avg_len = len_man / len_sum
#         avg_in_list = avg_len * len(input_list)

# input_on = 0
# li_st = []
# while input_on <= 10:
#      li_st.append(input('Give me text: ').lower().strip())
#      input_on += 1
#      if input_on == 10:
#          break
# check_pivot = 0
# while True:
#     check_string = li_st[check_pivot]
#     if check_pivot == len(li_st):
#         break
#     if not len(check_string) % 2:
#          print(check_string)
#     check_pivot += 1
#
# end_of_input = True
# while end_of_input :
#     num = int((input('Give me Numbers: ')))
#     if  (num % 2) == 0:
#         print('eiven')
#     else:
#         print('odd')
#         end_of_input = False
#

#num = int(input('give me numbers: '))
#count = 0
#while num != 0:
#    num //= 10
#    count += 1
#print("Number of digits: " + str(count))


# while True:
#     num = str(input('give me numbers: '))
#     print(num[::-1])


# num = int(input('give me numbers: '))
# reversed_num = 0
#
# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10
#
# print("Reversed Number: " + str(reversed_num))
#
# end_of_input = False
# wins_count = 0
# count_one = None
# count_two = None
# wins_one = []
# wins_two = []
#
# while not end_of_input:
#     player_one = str(input("Player one! Rock, Paper, Scissors? ")).strip().lower()
#     player_two = str(input("Player two! Rock, Paper, Scissors? ")).strip().lower()
#     if player_one == 'quit' or player_two == 'quit':
#          new_g = input('New Game? Yes/No: ').strip().lower()
#          if new_g == 'yes':
#              end_of_input = False
#          else:
#           print(f"player one won {count_one} times\nplayer two won {count_two} times\nThanks for Playing!")
#
#     if player_one == 'rock' and player_two == 'scissors':
#         wins_count += 1
#         wins_one.append(wins_count)
#         count_one = len(wins_one)
#     elif player_one == 'scissors' and player_two == 'paper':
#         wins_count += 1
#         wins_one.append(wins_count)
#         count_one = len(wins_one)
#     elif player_one == 'paper' and player_two == 'Rock':
#         wins_count += 1
#         wins_one.append(wins_count)
#         count_one = len(wins_one)
#     elif player_two == 'rock' and player_one == 'scissors':
#         wins_count += 1
#         wins_two.append(wins_count)
#         count_two = len(wins_two)
#     elif player_two == 'scissors' and player_one == 'paper':
#         wins_count += 1
#         wins_two.append(wins_count)
#         count_two = len(wins_two)
#     elif player_two == 'paper' and player_one == 'Rock':
#         wins_count += 1
#         wins_two.append(wins_count)
#         count_two = len(wins_two)
#     else:
#         print('Drow!')

# import random
# guess = 0
# out_of_guess = False
#
# while not out_of_guess:
#     random_num = random.randint(1, 100)
#     guess += 1
#     user_num = int(input('Guess The Number: '))
#     if user_num == 'exit':
#         print(f'You had {guess} guesss')
#         out_of_guess = True
#     if user_num < random_num:
#         print(f'Your Number is Too Low\nthe number is {random_num}\n')
#     elif user_num > random_num:
#         print(f'Your Number is Too High\nthe number is {random_num}\n')
#     else:
#         print(f'Exactly it took you {guess} guesss')
#


