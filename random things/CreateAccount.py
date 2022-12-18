import bcrypt
from BusValidations import *
from BusDataConnector import *


class CreateAccount:

    def __init__(self):
        # creating a main dict
        self.__accounts_info_dict: dict[str, dict] = dict()
        self.__accounts_info: dict = {'id': int, 'email': str, 'full_name': str, 'password': str}
        # cycling throw account info for input
        self.__accounts_dict: dict = dict()

    def account_info(self, start: bool) -> dict:
        while start:
            # looping for amount of account info
            for place in range(len(self.__accounts_info)):
                # creating secondary dict
                # looping throw the account info for each input
                for info in self.__accounts_info:
                    # getting input
                    self.__accounts_dict[info] = input(f'{info}: ').lower().strip()
                    # validating email input
                    invalid_counter = 0
                    if info == "id":
                        while is_num(self.__accounts_dict[info]) is False or len(self.__accounts_dict[info]) < 6 :
                            print(f'\033[0;31;1m ID should be at least 6 characters log\033[0;30;0m')
                            self.__accounts_dict[info] = input(f'{info}: ')
                            invalid_counter += 1
                            # if invalid three times quiting the program
                            if invalid_counter == 3:
                                print('RESTART the program please')
                                quit()
                    elif info == 'email':
                        # looping while invalid
                        invalid_counter: int = 0
                        while is_email(self.__accounts_dict[info]) is False:
                            print(f'\033[0;31;1m{self.__accounts_dict[info]} is invalid!\033[0;30;0m please try again!')
                            self.__accounts_dict[info] = input(f'{info}: ')
                            invalid_counter += 1
                            # if invalid three times quiting the program
                            if invalid_counter == 3:
                                print('RESTART the program please')
                                quit()
                        # validating password input
                    elif info == 'password':
                        # looping while invalid
                        invalid_counter: int = 0
                        while is_pass(self.__accounts_dict[info]) is False:
                            print(f'\033[0;31;1m password should be at least 6 characters log\033[0;30;0m')
                            self.__accounts_dict[info] = input(f'{info}: ')
                            invalid_counter += 1
                            # if invalid three times quiting the program
                            if invalid_counter == 3:
                                print('RESTART the program please')
                                quit()
                        # validating password input
                    else:
                        # looping while invalid
                        invalid_counter: int = 0
                        while is_name(self.__accounts_dict[info]) is False:
                            print(f'\033[0;31;1m{self.__accounts_dict[info]} is invalid!\033[0;30;0m please try again!')
                            self.__accounts_dict[info] = input(f'{info}: ').lower().strip()
                            invalid_counter += 1
                            # if invalid three times quiting the program
                            if invalid_counter == 3:
                                print('RESTART the program please')
                                quit()
                # adding secondary dict to main dict
                self.__accounts_dict['password'] = str(bcrypt.hashpw(self.__accounts_dict['password'].encode(), bcrypt.gensalt()))
                self.__accounts_info_dict[self.__accounts_dict['id']] = self.__accounts_dict
                # indicating validation of program
                print('\033[0;32;1m Account Saved In System!\033[0;30;0m')
                UserData("BusFiles","UserData.json").write_data(self.__accounts_info_dict, "accounts")
                # end of program
                start = False
                return self.__accounts_info_dict