"""EXAMPLE FOR USE"""

import db_connector

"""PARSING DATA INTO DB.JASON"""
email: str = "test@test.com"
f_name: str = "test"
l_name: str = "testovich"
password: str = "123$"
try:
    db_connector.write_data({email: {"first_name": f_name, "last_name": l_name, "pass": password}}, "accounts")
except:
    print("ERROR")

"""GETTING DATA FROM DB.JASON"""
email: str = "test@yooho.org"
try:
    data: dict = db_connector.get_data(email, "accounts")
    first_name, last_name, password = data[email]["f_name"], data[email]["l_name"], data[email]["password"]
    print(f"Email: {email}\nFirst name: {first_name}\nLast name: {last_name}\nPassword: {password}")
except:
    print("ERROR")
