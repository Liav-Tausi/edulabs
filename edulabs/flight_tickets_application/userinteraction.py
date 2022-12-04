import calculations
import time

total_price = 0
num_of_line, letter_of_row = None, None
f_name, l_name, email = None, None, None

# checking for num = str
def is_num(num: str) -> bool:
    while num not in ['1','2','3']:
        return False


# checking for name = str
def is_name(name: str) -> bool:
    while not name.isalpha():
        return False


def end_resit(price_over_all: int,class_seat: str, seat_num: int, row_letter: str, meal_type: int, luggage_price: int, f_name: str, l_name: str, email: str):
  price_over_all_end = total_price
  interested = input("Are you interested in trying your luck and getting discount? y/n: ")
  while interested not in ['y', 'n']:
        interested = input('\033[0;31;1mTry Again!\033[0;30;0m y/n: ')
  if interested == 'n':
        pass
  else:
    lucky_number = input("Please chose number between 1-9 including: ")
    while int(lucky_number) <= 1 and int(lucky_number) >= 9:
        lucky_number = input('\033[0;31;1mTry Again!\033[0;30;0m Please chose number between 1-9 including:')
    result = calculations.lottery(f'{f_name} {l_name}', int(lucky_number))
    time.sleep(2)
    if result is None:
        print("You didn't win the lottery :'(")
        price_over_all_end = total_price
    else:
        print(f"You win! {result}% discount of the total price!")
        price_over_all_end = price_over_all-(price_over_all * (result * 0.1))

    time.sleep(2)

  print("""
                      _____________________

                     |  .-----------.  |   |-----.
                     |  | PRINTING  |  |   |-=---|
                     |  |           |  |   |-----|
                     |  | RESIT...  |  |   |-----|
                     |  |           |  |   |-----|
                     |  `-----------'  |   |-----'/\

                         /                      / / /
                        / //               //  / / /
                       /                      / / /
                      / _/_/_/_/_/_/_/_/_/_/ /   /
                     / _/_/_/_/_/_/_/_/_/_/ /   /
                    / _/_/_/_______/_/_/_/ / __/
                   /______________________/ /    
                   \______________________\/
   """)
  time.sleep(2)
  print(f"""
               ╔══════════════════════════════════════╗
               ║▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒║
               ║▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒ RESIT ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒║
               ║▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒║
               ║▒▓              __|__               ▓▒║
               ║▒        --o--o--(_)--o--o--         ▒║
               ║▒        ISRAEL ->  NEW-YORK         ▒║
               ║▒ ══════════════════════════════════ ▒║
                    for: {f_name} {l_name}
                    Email: {email}
               ║▒ ══════════════════════════════════ ▒║
                    class: {class_seat}
                    seat number: {row_letter}{seat_num}
               ║▒ ══════════════════════════════════ ▒║
                    luggage cost: {luggage_price}    
               ║▒ ══════════════════════════════════ ▒║
                    meal: {meal_type}                
               ║▒ ══════════════════════════════════ ▒║
               ║▒      thanks you for flying         ▒║
               ║▒            with us!                ▒║
               ║▒                                    ▒║
               ║▒ ══════════════════════════════════ ▒║
                   total price is: {price_over_all_end}  
               ║▒▓ ════════════════════════════════ ▓▒║
               ║▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒║
               ╚══════════════════════════════════════╝
  """)


def luggage_menu():
    print("""   
                .   . . .-. .-. .-. .-. .-.   .  . .-. . . . . 
                |   | | |.. |.. |-| |.. |-    |\/| |-  |\| | | 
                `-' `-' `-' `-' ` ' `-' `-'   '  ` `-' ' ` `-'                      

                            ____
                       .---[[__]]----.
                      ;-------------.|       ____
                      |             ||   .--[[__]]---.
                      |             ||  ;-----------.|
                      |             ||  |           ||
                      |_____________|/  |           ||
                                        |___________|/
    """)

# economy class seat-line picker
def economy_class(start: bool) -> bool:
    global num_of_line, letter_of_row, total_price
    print("""             
                   -/                    /                         
                 -/ ▓▓ ECONOMY CLASS ▓▓ /                          
                /                      |                           
              -/       EMERG EXIT      /                           
             /         +--------+     |                            
            -----------+--------+---------------------------       
     window ->  |F +--+ +--+ +--+ +--+ +--+ +--+ +--+ +--+ +------+
                |  +--+ +--+ +--+ +--+ +--+ +--+ +--+ +--+ |  WC  |
                |E |  | |  | |  | |  | |  | |  | |  | |  | +------+
                |  +--+ +--+ +--+ +--+ +--+ +--+ +--+ +--+         
                |D |  | |  | |  | |  | |  | |  | |  | |  |   ▓ 11-20 the price = $1700 ▓     
                   +--+ +--+ +--+ +--+ +--+ +--+ +--+ +--+   ▓ 21-40 the price = $1500 ▓     
     aisle ->       1    5    10   20   30   40   50   60    ▓ 41-60 the price = $1200 ▓     
                   +--+ +--+ +--+ +--+ +--+ +--+ +--+ +--+   ▓  Near the window = +$10 ▓ 
                |C |  | |  | |  | |  | |  | |  | |  | |  |         
                |  +--+ +--+ +--+ +--+ +--+ +--+ +--+ +--+         
                |B |  | |  | |  | |  | |  | |  | |  | |  |         
                |  +--+ +--+ +--+ +--+ +--+ +--+ +--+ +--+         
     window ->  |A +--+ +--+ +--+ +--+ +--+ +--+ +--+ +--+         
            -----------+--------+----------------------------      
            \          +--------+   |                              
             -\        EMERG EXIT    \                             
               \                     |                             
                \                     \                            
                 -\                    \                          
    """)
    # getting input from user
    num_of_line = input("Please Insert The NUMBER of The LINE you'd like to seat at: ")
    # input validation
    while int(num_of_line) < 11 or int(num_of_line) > 60:
        num_of_line = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    # getting input from user
    letter_of_row = input("Please Insert The LETTER of ROW you'd like to seat at: ").upper()
    # input validation
    while letter_of_row not in ['A', 'B', 'C', 'D','E','F']:
        letter_of_line_eco = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    # printing if successful
    print('\033[0;32;1m Saved In System!\033[0;30;0m')
    # sending to calculations the seat choice + adding for over all
    total_price += calculations.seat_calc('eco', letter_of_row, num_of_line)
    menu_eco(True)


# biz class seat-line picker
def biz_class(start: bool) -> bool:
    global num_of_line, letter_of_row, total_price
    print("""
                                      - /
               ▓▓ BUSINESS CLASS ▓▓  -/
                                   - /
            ----------------------------------------
 window ->  |   +--+  +--+  +--+  +--+  +--+  +--+ |    ▓ Lines 5-7 => price $3000 ▓
            | D |  |  |  |  |  |  |  |  |  |  |  | |    ▓ Line 8-10 => price $2300 ▓
            |   +--+  +--+  +--+  +--+  +--+  +--+ |  ▓ near the window -> A, D +$55 ▓
            | C |  |  |  |  |  |  |  |  |  |  |  | |
            |   +--+  +--+  +--+  +--+  +--+  +--+ |
            
 aisle ->         5     6     7     8     9    10
            
            |   +--+  +--+  +--+  +--+  +--+  +--+ |
            | B |  |  |  |  |  |  |  |  |  |  |  | |
            |   +--+  +--+  +--+  +--+  +--+  +--+ |
            | A |  |  |  |  |  |  |  |  |  |  |  | |
 window ->  |   +--+  +--+  +--+  +--+  +--+  +--+ |
            ----------------------------------------
                                 -\
                                   -\
                                     -\
    """)
    # getting input from user
    num_of_line = input("Plesae Insert The NUMBER of The LINE you'd like to seat at: ")
    # input validation
    while num_of_line not in ['5','6','7','8','9','10']:
        num_of_line = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    # getting input from user
    letter_of_row = input("Plesae Insert The LETTER of ROW you'd like to seat at: ").upper()
    # input validation
    while letter_of_row not in ['A', 'B', 'C', 'D']:
        letter_of_row = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ').upper()
    # printing if successful
    print('\033[0;32;1m Saved In System!\033[0;30;0m')
    # sending to calculations the seat choice + adding for over all
    total_price += calculations.seat_calc('biz', letter_of_row, num_of_line)
    menu_biz(True)

# first class seat-line picker
def first_class(start: bool) -> bool:
    global num_of_line, letter_of_row, total_price
    print("""              
              ▓▓ FIRST CLASS ▓▓
                                                     /---|
                                              /-----    |
                                       /------  /--\    |
                                 /-----      \-- A --   |
                          /--+---+            ---/      |
                    /-----   |   |     ------|          |
                /---   |     +WC-+    -\  B--|          |
               /       |                --              |
              /        \                                |
              \        |              /-----            |
               \       \             -- C -/            |
               -\-     |            ------\             |
                   -----\                       /--     |
                         -----\              /--   |    |
                               -----\       ---\ D /    |
                                     -----\     --|     |
                                           -----\       |
                                                 ---  --|                                                                             
    """)
    seat = input("Please insert the LETTER of the seat you'd like: ").upper()
    # input validation
    while seat not in ['A','B','C','D']:
       seat = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ').upper()
    # printing if successful
    print('\033[0;32;1m Saved In System!\033[0;30;0m')
    # sending to calculations the seat choice + adding for over all
    letter_of_row = seat
    num_of_line = "0"
    total_price += calculations.seat_calc('first')
    menu_first(True)

# first class menu picker
def menu_first(start: bool) -> int:
    global f_name, l_name, email
    print("""
                           __                       @@;,
                          (  ;          ?           :  );
                         _| |_  |  |   ||  |  |     _| |_
                        |  \  \  \/    ||   \/ ___ /  /  |
                      __|   |\ __||____||___||______/|   |
                      |||   | |_______    _________| |   |||
                      |||   |____     |   |      ____|   |||      
                      \ \______  )    |   |     /  ______/ /
                       ||    | | |    |   |    /___|     ||  
                       ||    | | |_  /| | |\   _| ||     ||
                       ||    | \__, / | | |  \<__/ |     ||

            .-.   .-..----.  .--.  .-.      .-.   .-..----..-. .-..-. .-.
            |  `.'  || {_   / {} \ | |      |  `.'  || {_  |  `| || { } |
            | |\ /| || {__ /  /\  \| `--.   | |\ /| || {__ | |\  || {_} |
            `-' ` `-'`----'`-'  `-'`----'   `-' ` `-'`----'`-' `-'`-----'
                           Luxury meals Chef Gordon Ramzy
                           
     [1] Menu 1 -> |STARTER: Roast veal sweetbread |MAIN: Cornish turbot |DESERT: Hazelnut souffle 
       
     [2] Menu 2 -> |STARTER: Ravioli lobster |MAIN: 100-Day aged Cumbrian Blue Grey |DESERT Pecan praline 
     
     [3] Menu 3 -> |STARTER: Scallops from the Isle of Skye |MAIN Aynhoe Park fallow deer |DESERT Caramelised apple Tarte Tatin 
     
    """)
    num = input('Please Insert The Number Of The Menu You Desire: ')
    # input validation
    while num not in ['1','2','3']:
        num = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    meal = "Luxury meal included"
    luggage_menu()
    luggage = input('Please Insert expected kg of your luggage: ')
    # input validation
    while not luggage.isdigit():
        luggage = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please input kg only numbers:')
    luggage_price = calculations.luggage_calc('first', int(luggage))
    # printing if successful
    print('\033[0;32;1m Saved In System!\033[0;30;0m')
    end_resit(total_price,'First', num_of_line, letter_of_row, meal, f"{luggage}kg +{luggage_price}$", f_name,l_name, email)




# biz class meal picker
def menu_biz(start: bool) -> int:
    global total_price, f_name, l_name, email
    print("""
                           __                       @@;,
                          (  ;          ?           :  );
                         _| |_  |  |   ||  |  |     _| |_
                        |  \  \  \/    ||   \/ ___ /  /  |
                      __|   |\ __||____||___||______/|   |
                      |||   | |_______    _________| |   |||
                      |||   |____     |   |      ____|   |||      
                      \ \______  )    |   |     /  ______/ /
                       ||    | | |    |   |    /___|     ||  
                       ||    | | |_  /| | |\   _| ||     ||
                       ||    | \__, / | | |  \<__/ |     ||

            .-.   .-..----.  .--.  .-.      .-.   .-..----..-. .-..-. .-.
            |  `.'  || {_   / {} \ | |      |  `.'  || {_  |  `| || { } |
            | |\ /| || {__ /  /\  \| `--.   | |\ /| || {__ | |\  || {_} |
            `-' ` `-'`----'`-'  `-'`----'   `-' ` `-'`----'`-' `-'`-----'
              [1] Luxury meal (+ $42)         [2] Business meal (included)    
    """)
    num = input('Please Insert The Number Of The Menu You Desire: ')
    # input validation
    while num not in ['1','2']:
        num = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    if num == '1':
        print("""                           Luxury meals Chef Gordon Ramzy

     [1] Menu 1 -> |STARTER: Roast veal sweetbread |MAIN: Cornish turbot |DESERT: Hazelnut souffle 

     [2] Menu 2 -> |STARTER: Ravioli lobster |MAIN: 100-Day aged Cumbrian Blue Grey |DESERT Pecan praline 

     [3] Menu 3 -> |STARTER: Scallops from the Isle of Skye |MAIN Aynhoe Park fallow deer |DESERT Caramelised apple Tarte Tatin 

    """)
        meal = "Luxury meal +$42"
        num_menu = input('Please Insert The Number Of The Menu You Desire: ')
        # input validation
        while num_menu not in ['1', '2', '3']:
            num_menu = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    else:
        meal ="Business meal included"
    luggage_menu()
    luggage = input('Please Insert expected kg of your luggage: ')
    # input validation
    while not luggage.isdigit():
        luggage = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please input kg only numbers:')
    luggage_price = calculations.luggage_calc('biz', int(luggage))
    # printing if successful
    print('\033[0;32;1m Saved In System!\033[0;30;0m')
    # passing for included
    if num == '2':
        pass
    # sending to calculations the meal choice + adding for over all
    else:
        total_price += calculations.meal_price(num)
    end_resit(total_price,'Business', num_of_line, letter_of_row, meal, f"{luggage}kg +{luggage_price}$", f_name,l_name, email)


# economy class meal picker
def menu_eco(start: bool) -> int:
    global total_price, num_of_line, letter_of_row, f_name, l_name, email
    print("""
                           __                       @@;,
                          (  ;          ?           :  );
                         _| |_  |  |   ||  |  |     _| |_
                        |  \  \  \/    ||   \/ ___ /  /  |
                      __|   |\ __||____||___||______/|   |
                      |||   | |_______    _________| |   |||
                      |||   |____     |   |      ____|   |||      
                      \ \______  )    |   |     /  ______/ /
                       ||    | | |    |   |    /___|     ||  
                       ||    | | |_  /| | |\   _| ||     ||
                       ||    | \__, / | | |  \<__/ |     ||
                       
            .-.   .-..----.  .--.  .-.      .-.   .-..----..-. .-..-. .-.
            |  `.'  || {_   / {} \ | |      |  `.'  || {_  |  `| || { } |
            | |\ /| || {__ /  /\  \| `--.   | |\ /| || {__ | |\  || {_} |
            `-' ` `-'`----'`-'  `-'`----'   `-' ` `-'`----'`-' `-'`-----'
    [1] Luxury meal (+ $42)    [2] Business meal (+ $22)    [3] Economy meal (+ $7)
    """)
    num = input('Please Insert The Number Of The Menu You Desire: ')
    # input validation
    while num not in ['1','2','3']:
        num = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    if num == '1':
        print("""                           Luxury meals Chef Gordon Ramzy
                           
     [1] Menu 1 -> |STARTER: Roast veal sweetbread |MAIN: Cornish turbot |DESERT: Hazelnut souffle 
       
     [2] Menu 2 -> |STARTER: Ravioli lobster |MAIN: 100-Day aged Cumbrian Blue Grey |DESERT Pecan praline 
     
     [3] Menu 3 -> |STARTER: Scallops from the Isle of Skye |MAIN Aynhoe Park fallow deer |DESERT Caramelised apple Tarte Tatin 
     
    """)
        meal = "Luxury meal +$42"
        num_menu = input('Please Insert The Number Of The Menu You Desire: ')
        # input validation
        while num_menu not in ['1', '2', '3']:
            num_menu = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    elif num == '2':
        meal = "Business meal +$22"
    else:
        meal = "Economy meal +$7"
    luggage_menu()
    luggage = input('Please Insert expected kg of your luggage: ')
    # input validation
    while not luggage.isdigit():
        luggage = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please input kg only numbers: ')
    luggage_price = calculations.luggage_calc('eco', int(luggage))
    # printing if successful
    print('\033[0;32;1m Saved In System!\033[0;30;0m')
    # sending to calculations the meal choice + adding for over all
    total_price += calculations.meal_price(num)
    end_resit(total_price,'Economy' , num_of_line, letter_of_row, meal, f"{luggage}kg +{luggage_price}$", f_name,l_name, email)




def see_destination(start: bool) -> bool:
    print("""
                  current designations available: 
                   ,_   .  ._. _.  .
           , _-\','|~\~      ~/      ;-'_   _-'     ,;_;_,    ~~-
  /~~-\_/-'~'--' \~~| ',    ,'      /  / ~|-_\_/~/~      ~~--~~~~'--_
  /              ,/'-/~ '\ ,' _  , '|,'|~                   ._/-, /~
  ~/-'~\_,       '-,| '|. '   ~  ,\ /'~                /    /_  /~
.-~      '|        '{*}NEW-TORK    _\~     ,_               /|
          '\        /'~          |_/~\\,-,~  \ "         ,_,/ |
           |       /            ._-~'\_ _   {*}ISRAEL     \ ) /
            \   __-\           '/      ~ |\  \_          /  ~
  .,         '\ |,  ~-_      - |          \\_' ~|  /\  \~ ,
               ~-_'  _;       '\           '-,   \,' /\/  |
                 '\_,~'\_       \_ _,       /'    '  |, /|'
                   /     \_       ~ |      /         \  ~'; -,_.
                   |       ~\        |    |  ,        '-_, ,; ~ ~\
                    \,      /        \    / /|            ,-, ,   -,
                     |    ,/          |  |' |/          ,-   ~ \   '.
                    ,|   ,/           \ ,/              \       |
                    /    |             ~                 -~~-, /   _
                    |  ,-'                                    ~    /
                    / ,'                                      ~
                    ',|  ~
                      ~'
    """)
    # getting input from user
    num = input('To Pick Your FLIGHT PACKAGE enter 1:  ')
    # input validation
    while str(num) not in ['1']:
        num = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    # sending to function
    if num == '1':
        see_prices(True)


def see_prices(start: bool,return_to: bool = None) -> bool:
    # FLIGHT PACKAGES menu
    print("""
                                THEIS ARE THE AVAILABLE FLIGHT PACKAGES 
    
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
   ▓▓       ECONOMY CLASS        ▓▓ ▓▓       BUSINESS CLASS      ░▓▓  ▓▓        FIRST CLASS        ░▓▓
   ▓▓   over all Lines fee:      ▓▓ ▓▓  Lines 5-7 -> Price $3000  ▓▓  ▓▓  Lines 1-6 -> Price $4000  ▓▓ 
   ▓▓  11-20 the price -> $1700  ▓▓ ▒▒  Line 8-10 -> price $2300  ▓▓  ▓▓  Seats - no additional fee ▓▓
   ▓▓  21-40 the price -> $1500  ▓▓ ▒▒   Seats A,B,C,D            ▓▓  ▓▓         A,B,C,D            ▓▓
   ▓▓  41-60 the price -> $1200  ▓▓ ▒▒    near window             ▓▓  ▓▓   near window: A, D        ▓▓
   ▓▓   Seats:                   ▓▓ ▒▒        ╚→  A, D (+ $55)    ▓▓  ▓▓  Luggage:                  ▓▓
   ▓▓  Near the window -> +$10   ▓▓ ▒▒                            ▒▒  ▒▒       no additional fee    ▓▓
   ▓▓   Lines:                   ▓▓ ▓▓  Meal:                     ▓▓  ▓▓  Luxury meal:              ▓▓
   ▓▓  12,22,42  extra fee +$15  ▓▓ ▓▓    Luxury meal   (+ $42)   ▓▓  ▓▓ included in price          ▓▓
   ▓▓  Luggage:                  ▓▓ ▓▓   Business meal included   ▓▓  ▓▓         Chef Gordon Ramzy  ▓▓ 
   ▓▓   $10/kg if exceeds 20kg   ▓▓ ▓▓                            ▓▓  ▓▓                            ▓▓
   ▓▓   Meal:                    ▓▓ ▓▓                            ▓▓  ▓▓                            ▓▓
   ▓▓   Luxury meal - (+ $42)    ▓▓ ▓▓                            ▓▓  ▓▓                            ▓▓
   ▓▓   Business meal - (+ $22)  ▓▓ ▓▓                            ▓▓  ▓▓                            ▓▓
   ▓▓   Economy meal - (+ $7)    ▓▓ ▓▓                            ▓▓  ▓▓                            ▓▓
   ░░▒▒          [1]           ░▒▓  ░░▒           [2]            ▒▒▓  ▓▓▒            [3]          ░░▒▓
     ░░░░░░░░░░░░░░░░░░░░░░░░░░        ░░░░░░░░░░░░░░░░░░░░░░░░░░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░  
    """)
    print("""
         (1) for ECONOMY CLASS           (2) for BUSINESS CLASS             (3) for FIRST CLASS
    """)
    # getting input from user
    num = input('Your Dithered FLIGHT PACKAGE:')
    # input validation
    while str(num) not in ["1", "2","3"]:
        num = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    num = str(num)
    # sending to functions depending on choice
    if num == '1':
        economy_class(True)
    elif num == '2':
        biz_class(True)
    elif num == '3':
        first_class(True)


def accunt(first_name: str, last_name: str, u_email: str) -> bool:
    global f_name, l_name, email
    f_name = first_name
    l_name = last_name
    email = u_email
    print(f"""                       
                            --====|====--
                                  |  
                             HELLO {f_name.title()}!
                              .-'''''-. 
                            .'_________'. 
                           /_/_|__|__|_\_\

    ,-------------------- |    `-. .-'    |--------------------,
    -please enter the number of the action you'd like to execute-
              `"-/ / \ \.._\             /_../ / \ \-"`
                 \░[1]░/    '._       _.'    \░[2]░/
             SEE DESTINATIONS             BOOK A FLIGHT 
     """)
    # getting input from user
    num = input('Number Of Your Dithered Action: ')
    # input validation
    while str(num) not in ["1","2"]:
        num = input(f'\033[0;31;1m input is invalid!\033[0;30;0m please try again: ')
    # sending to functions depending on choice
    if num == '1':
        see_destination(True)
    else:
        see_prices(True)




























