import re


def is_pass(password: str) -> bool:
    while len(password) < 6:
        return False


def is_email(email: str) -> bool:
    path: str = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    while not re.match(path, email):
        return False


def is_name(name: str) -> bool:
    name_split = name.split()
    while (name_split[0].isalpha() and name_split[1].isalpha()):
        return True
    else:
        return False


def is_num(num: str) -> bool:
    while num.isdigit():
        return True
    else:
        return False


def is_str(str: str) -> bool:
    while not str.isalpha() and str.isdigit() is False:
        return True
    else:
        return False
