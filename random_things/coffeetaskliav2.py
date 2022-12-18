#
#
# coffee_list: list =['','1# espresso','2# doppio','3# lungo','4# ristretto','5# macchiato','6# corretto','7# con panna','8# romano'
#              ,'9# cappuccin','10# americano','11# cafe latte','12# flat white','13# marocchino','14# mocha','15# bicerin','16# breve',
#               '17# rafcoffe','18# mead raf','19# vienna coffee','20# chocolate milk','21# latte macchiato','22# glace',
#               '23# freddo','24# irish coffee','25# frappe','26# cappuccino freddo','27# caramel frappe','28# glace']
# print(("""\
#                                                   ,--.
#                                 ,--.   ,--. ,---. |  | ,---. ,---. ,--,--,--. ,---.
#                                 |  |.'.|  || .-. :|  || .--'| .-. ||        || .-. :
#                                 |   .'.   |\   --.|  |\ `--.' '-' '|  |  |  |\   --.
#                                 '--'   '--' `----'`--' `---' `---' `--`--`--' `----'
#                                               ,--.
#                                             ,-'  '-. ,---.  ,---.
#                                             '-.  .-'| .-. || .-. |
#                                               |  |  ' '-' '' '-' '
#                                               `--'   `---'  `---'
#                     ,--.,--.                  ,--.           ,-----.         ,---.
#                     |  |`--' ,--,--.,--.  ,--.|  |,---.     '  .--./ ,--,--./  .-' ,---.
#                     |  |,--.' ,-.  | \  `'  / `-'(  .-'     |  |    ' ,-.  ||  `-,| .-. :
#                     |  ||  |\ '-'  |  \    /     .-'  `)    '  '--'\\ '-'  ||  .-'\   --.
#                      `--'`--' `--`--'   `--'      `----'      `-----' `--`--'`--'   `----'
#  """))
# manu: str = input('Would You Like to See Our Menu? ').lower().strip()
# while manu not in ['yes' , 'no']:                          # Checking Users Input
#     manu: str = input("\033[0;31;1m try again!: \033[0;30;0m").lower().strip()
# if manu == 'yes':
#     print("""\
#   _   _     _       _
#  | |_| |__ (_)___  (_)___    ___  _   _ _ __   _ __ ___   ___ _ __  _   _
#  | __| '_ \| / __| | / __|  / _ \| | | | '__| | '_ ` _ \ / _ \ '_ \| | | |
#  | |_| | | | \__ \ | \__ \ | (_) | |_| | |    | | | | | |  __/ | | | |_| |
#   \__|_| |_|_|___/ |_|___/  \___/ \__,_|_|    |_| |_| |_|\___|_| |_|\__,_|
#   """)
#     print("""
#      1# espresso 2# doppio 3# lungo 4# ristretto
#
#      5# macchiato 6# corretto','7# con panna','8# romano'
#
#      9# cappuccin 10# americano 11# cafe latte
#
#      12# flat white 13# marocchino 14# mocha 15# bicerin'
#
#      16# breve 17# rafcoffe 18# mead raf 19# vienna coffee
#
#      20# chocolate milk 21# latte macchiato 22# glace
#
#      23# freddo 24# irish coffee 25# frappe
#
#      26# cappuccino freddo 27# caramel frappe 28# glace """)
#
# if manu == 'no':
#     quit()
#
#                                                                                                                  # Getting input From User
# remove: str = input('Would You Like to avoid any item From The list? Yes/No: ').lower().strip()                  # Checking Users Input
# while remove not in ['yes','no']:                                                                                # user wants to remove an item
#     remove: str = input("\033[0;31;1m try again!: \033[0;30;0m").lower().strip()
# if remove == "yes":                                                                                              # Getting input From User
#     remove_idx: str = (input('Please Insert The Number of The item? '))
#     while (not remove_idx.isdigit()) or (int(remove_idx) > len(coffee_list)):                                                                          # Checking Users Input
#         remove_idx: str = (input("\033[0;31;1m try again!: \033[0;30;0m"))                                       # Removing the item by index
#     coffee_list.pop(int(remove_idx))
#     print('\033[0;31;1m Item Has been avoided!\033[0;37;0m')
# else:
#     pass                                                                                                         # Getting Time From User
# time: str = (input('When Would You Like Your Coffee? ')).strip()
# while (len(time) != 5) or not time[3].find(':') :
#     time: str = (input("\033[0;31;1m try again!: \033[0;30;0m"))
#     for i in range(4):
#         if not time[i].isdigit() and (len(time) != 5):
#             time: str = (input("\033[0;31;1m try again!: \033[0;30;0m"))                                     # Spliting Time input By ':'
# time_s: list = time.split(':')                                                                               # Turning input To Hours int
# hours: int = (time_s[0])                                                                                     #Turning input To Minutes in
# minutes: int = (time_s[1])                                                                                   # Getting Amount of Friends From User cheking for *int*
# friends: str = (input('With How Many Firends? '))                                                            # Checking Users Input
# while not friends.isdigit() or int(friends) < 0:
#         friends: str = (input("\033[0;31;1m try again!: \033[0;37;0m "))
# time_h: int = int(hours)
# time_m: int = int(minutes)                                                                                   # Getting input From User
# special_inp: str = input('Any Special Request? Yes/No? ').lower().strip()                                    # Checking Users Input
# while special_inp not in ['yes','no']:                                                                       # Getting input From User
#     special_inp: str = input("\033[0;31;1m try again!: \033[0;37;0m").lower().strip()
# if special_inp == "yes":                                                                                     # Getting input From User
#     special: int = int(input('Special Request Number? '))
# else:
#     special = 0
# pass
# time_h += special
# print('='* 55)                                                                                                # printing user's coffee
# print(f"\tMain user's: {coffee_list[time_h]}")
# print('='* 55)                                                                                                # looping for amount of friends
# for i in range(int(friends)-1):
#     time_h += time_m
#     if time_h > 28:                                                                                           # if inputed time for friends higher items in list
#         time_h %= 28
#     print('='* 55)
#     print(f"\tFriend Number {i+1}'s coffee: {coffee_list[time_h]}")                                           # printing friends coffees
#     print('=' * 55)
