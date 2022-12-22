import re
from userinteraction import accunt
import db_connector


# checking for name = str
def is_name(name: str) -> bool:
    while not name.isalpha():
        return False


# checking for email validation
def is_email(email: str) -> bool:
    pat: str = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    while not re.match(pat, email):
        return False


# cheak for password validation
def is_pass(password: str) -> bool:
    while len(password) < 6:
        return False


# Create Account Function
def account_info(start: bool) -> dict:
    while start:
        # creating a main dict
        accounts_info_dict: dict = dict()
        # cycling throw account info for input
        accounts_info: dict = {'email': str,'first_name': str, 'last_name': str, 'password': str}
        # looping for amount of account infoSS
        for place in range(len(accounts_info)):
            # creating secondary dict
            accounts_dict: dict = {}
            # looping throw the account info for each input
            for info in accounts_info:
                # getting input
                accounts_dict[info] = input(f'{info}: ').lower().strip()
                # validating email input
                if info == 'email':
                    # looping while invalid
                    while is_email(accounts_dict[info]) is False:
                        print(f'\033[0;31;1m{accounts_dict[info]} is invalid!\033[0;30;0m please try again!')
                        accounts_dict[info] = input(f'{info}: ')
                        # if invalid twice quiting the program
                        if is_email(accounts_dict[info]) is False:
                            print('RESTART the program please')
                            quit()
                    # validating password input
                elif info == 'password':
                    # looping while invalid
                    while is_pass(accounts_dict[info]) is False:
                        print(f'\033[0;31;1m password should be at least 6 characters log\033[0;30;0m')
                        accounts_dict[info] = input(f'{info}: ')
                        # if invalid twice quiting the program
                        if is_pass(accounts_dict[info]) is False:
                            print('RESTART the program please')
                            quit()
                    # validating password input
                else:
                    # looping while invalid
                    while is_name(accounts_dict[info]) is False:
                        print(f'\033[0;31;1m{accounts_dict[info]} is invalid!\033[0;30;0m please try again!')
                        accounts_dict[info] = input(f'{info}: ').lower().strip()
                        # if invalid twice quiting the program
                        if is_name(accounts_dict[info]) is False:
                            print('RESTART the program please')
                            quit()
                # adding secondary dict to main dict
            accounts_info_dict[accounts_dict['email']] = accounts_dict
            # indicating validation of program
            print('\033[0;32;1m Account Saved In System!\033[0;30;0m')
            db_connector.write_data(accounts_info_dict, "accounts")
            # end of program
            start = False
            accunt(accounts_dict['first_name'], accounts_dict['last_name'], accounts_dict['email'])
            return accounts_info_dict

# Login Account Function
def account_login(start: bool):
    while start:
        while True:
            email = input("Please insert account Email: ")
            data = db_connector.get_data(email, "accounts")
            # validating email input
            if email not in data:
                # looping while invalid
                print(f'\033[0;31;1m{email} is not in our data base!\033[0;30;0m please try again / register')
                continue
            else:
                while True:
                    password = input(f"{list(data.values())[0]['first_name']} please type your password: ")
                    # validating email input
                    if password != str(list(data.values())[0]['password']):
                        # looping while invalid
                        print(f'\033[0;31;1m password is incorrect!\033[0;30;0m please try again!')
                        continue
                    else:
                        accunt(list(data.values())[0]['first_name'], list(data.values())[0]['last_name'], list(data.values())[0]['email'])
                        break
                break

        break


def user_picks(num: str) -> None:
    if num == '1':
        account_info(True)

    if num == '2':
        account_login(True)

    if num == '3':
        f_name = input('Please Insert Your First Name: ')
        l_name = input('Please Insers Your Last Name: ')
        email = input('Please Insers Your Email: ')
        while is_name(f_name) is False:
            f_name = input('\033[0;31;1mTry Again!\033[0;30;0m Your Name:')
        while is_name(l_name) is False:
            l_name = input('\033[0;31;1mTry Again!\033[0;30;0m Your Name:')
        while is_email(email) is False:
            email = input(f'\033[0;31;1m{email} is invalid!\033[0;30;0m please try again!')
        accunt(f_name, l_name, email)
