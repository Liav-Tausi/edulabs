from datetime import datetime
import requests
import json
import pytz



# class InvalidArgument(Exception):
#     pass
#
#
# # 1 Implement a decorator @single_str_arg that validates that function received exactly one argument and that the argument type is string
# def single_str_arg(other_function):
#
#     def validator(*args, **kwargs):
#         if isinstance(args[0], str) and (len(args[0]) > 0) and len(kwargs) == 0:
#             result = other_function(*args)
#             return result
#         else:
#             raise InvalidArgument()
#
#     return validator
#
#
# # 3 Implement a decorator @valid_param_types that receives as parameter allowed
# # argument types and validates whether the argument passed to a function answers this requirement
#
# def valid_param_types(valid_params: list):
#     def wrapper(other_function):
#
#         def validator(*args, **kwargs):
#             if (type(args[0]) and type(args[1])) in valid_params:
#                 result = other_function(*args, **kwargs)
#                 return result
#             else:
#                 raise InvalidArgument()
#
#         return validator
#
#     return wrapper
#
#
# @single_str_arg
# def convert_str(word: str) -> str:
#     return word.upper()
#
#
# @valid_param_types([int, float])
# def sum_numbers(num1, num2) -> int:
#     return num1 + num2
#
#
# if __name__ == '__main__':
#     print(convert_str("liav"))  # single_str_arg
#     print(sum_numbers(1, 3))  # valid_param_types


# starting from GET

# sending rewqest to URL
#
# BORED_URL = "https://www.boredapi.com/api/activity"
# res = requests.get(BORED_URL)
# # print(res)
# # print(type(res))
# #
# print(res.status_code)
# # print(res.text) # str!!!
# # print(res.text['activity']) # not working
#
# rel = res.json()
# print(rel)
#
# rts = requests.get("https://www.google.com")
# print(rts.status_code)


# response = requests.get("https://bad_url")
# response = requests.get("https://www.boredapi.com/api/act")
# print(response.status_code)
# print(response.text)


# with query param
#
# GENDERIZE_URL = "https://api.genderize.io/"
# response = requests.get(GENDERIZE_URL, params={'name': 'liav'})
# # print(response.status_code, response.text, sep="\n")
# print(response.json())

# GENDERIZE_URL = "https://api.genderize.io/bla/"
# response = requests.get(GENDERIZE_URL, params={'name': 'valeria'})
# print(response.status_code, response.text, sep="\n")

# {"country": [{"country_id": "GH", "probability": 0.224}, {"country_id": "PH", "probability": 0.084},
#              {"country_id": "NG", "probability": 0.073}, {"country_id": "US", "probability": 0.061},
#              {"country_id": "NE", "probability": 0.034}], "name": "nathaniel"}


# with path param
# https://restcountries.com/v3.1/alpha/il

#
# def get_ethnicity() -> None:
#     name = input("Insert your name: ")
#     ethnicity_url = "https://api.nationalize.io/"
#     country_url = "https://restcountries.com/v3.1/alpha/"
#
#     eth = requests.get(ethnicity_url, params={"name": name})
#     eth_json = eth.json()
#
#     ethnicity = sorted(eth_json['country'], key=lambda x: x["probability"], reverse=True)[0]
#     country_id = eth_json['country'][0]['country_id']
#
#     cou = requests.get(country_url+str(country_id).lower())
#     country_dict = cou.json()
#
#     time_zones = country_dict[0]['timezones']
#     utc_time = datetime.utcnow()
#     for time_zone in time_zones:
#         local_time = utc_time.astimezone(pytz.timezone(time_zone))
#         formatted_time = local_time.strftime("%I:%M %p %Z on %B %d, %Y")
#         print(f"The current time in {time_zone} is: {formatted_time}")
#
#     if (eth.status_code or cou.status_code) < 400:
#         print(
#             f"status code: {eth.status_code}, your ethnicity is most probably from "
#             f"{country_dict[0]['name']['common']} in {(country_dict[0]['continents'])[0]} and you speak "
#             f"{list(dict(country_dict[0]['languages']).values())}"
#             f" at {ethnicity['probability'] * 100}% ")
#
#     else:
#         raise Exception()


if __name__ == "__main__":
    try:
        get_ethnicity()
    except Exception:
        print("Error")

