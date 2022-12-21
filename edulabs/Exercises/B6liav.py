def birthday_function(start: bool) -> str:
    birthday_dict: dict[str] = dict()
    while True:
        birthday: str = input('Welcome to the birthday dictionary! would you like to insert or look up a birthday: ')
        while birthday not in ['insert','look up']:
            birthday: str = input('try again! would you like to insert or look up a birthday: ')
            if birthday not in ['insert','look up']:
                quit()
        if birthday == "insert":
            insert_dict: dict = dict()
            name = input('Insert name: ')
            while not name.isalpha():
                name = input('Try again! Insert name: ')
                if not name.isalpha():
                    quit()
            date = input('Insert date: ')
            while date[2].find('/'):
                date = input('Try again! Insert date: ')
                if date[2].find('/'):
                    quit()
            insert_dict[name] = date
            birthday_dict.update(insert_dict)
            print('name and date inserted!')
        else:
            name = input('Insert name: ')
            if name in birthday_dict:
                return (f"{name}'s birtday is {birthday_dict.get(name)}")
            else:
                return (f'{name} is not in our record')

print(birthday_function(True))
