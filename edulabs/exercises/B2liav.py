# Write a function to drop empty or None items from a given Dictionary.

# original: dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': "",}
# def dict_cleaner(dirty_dict: dict) -> dict:
#     clean_dict: dict = dict()
#     for i in range(len(dirty_dict)):
#         for k,v in dirty_dict.items():
#             if v not in [True,None,False]:
#                 if str(v).isalpha():
#                     clean_dict[k] = v
#     return clean_dict
#
# print(dict_cleaner(original))



# Write a function that receives a sequence of key-value pairs and creates a dictionary of lists (and returns it)

# didn't know how to add the values together
# original:list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# def dict_assembly(o_dict: list) -> dict:
#     result: dict = dict()
#     for k,v in o_dict:
#         result.setdefault(k,set()).add(v)
#
#     return result
#
# print(dict_assembly(original))



# Write a function that receives a dictionary of lists and splits it into a list of dictionaries.

# original: dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#
# def split_dict(o_dict: dict) -> list:
#     new: list[dict] = list()
#     for k,v in o_dict.items():
#         for val in range(len(v)):
#                 new.append({k:v[val]})
#     return new
#
# print(split_dict(original))


