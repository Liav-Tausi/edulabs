import pprint

# Create a function that receives 2 lists and returns a dictionary, where
# keys are elements from the list #1 and values are elements from the list #2.
# flowers = ['Rose','Lily','Tulip','Orchid','Carnation', 'Hyacinth', 'Rose']
# color = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
#
# def tow_lists_to_dict(keys: list[str],values: list[str]) -> dict:
#     new_dict = list(set(keys))
#     return dict(zip(keys,values))
# pprint.pprint(tow_lists_to_dict(flowers,color))



# B5.2
# Create a function that receives 2 lists and returns a dictionary, where
# keys are elements from the list #1 and values are elements from the list #2.
# colors_1 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']
#
# def list_set(list_of_things: list[str]) -> set[str]:
#     things_list: set = set()
#     for color in list_of_things:
#         things_list.add(color.lower())
#     return things_list
#
# # print(list_set(colors_1))



# B5.3
# # Create a function that receives a list and returns output (choose the right type) with unique elements only
# color_2 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# colors_3 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']
#
# def list_compere(color1: list[str], color2: list[str]) -> set[str]:
#     return list_set(color1).intersection(color2)
# print(list_compere(color_2,colors_3))



# B5.4
# Create a function that receives 3 lists and returns output
# (choose the right single type) that will indicate which colors are derived from basic colors
# base_colors = ['red', 'blue', 'Purple','white']
# colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white', 'sky blue', 'pure purple', 'white cream', 'Eggshell white','Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
# colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz','white & Red', 'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure']
#
# def sorting_colors(base: list, colors1: list[str], colors2: list[str]) -> dict:
#     colors3 = colors1+colors2
#     colors_set: set = set(colors3)
#     derived_dict = {}
#     for place in range(len(base)):
#         derived_dict[base[place]] = []
#         for color in colors_set:
#             if base[place].lower() in color:
#                 derived_dict[base[place]].append(colors_set)
#         return derived_dict
#
# pprint.pprint(sorting_colors(base_colors,colors_1,colors_2))



# B5.5
# Create a function that receives my_cities and returns all the cities I’ve visited without duplications.
# my_cities = {
#    2008:{'Germany':['Berlin', 'Munich'],
#          'France' :['Paris','Leon','Bordeaux']},
#
#    2009: {'China':['Hong Kong', 'Shanghai','Beijing'],
#          'Japan':['Nagoya','Toyokawa','Yatomi'],
#          'Mexico':['Tijuana','Ecatepec']},
#
#    2010: {'Germany': ['Berlin', 'Dusseldorf'],
#          'France': ['Paris', 'Nice', 'Bordeaux'],
#          'Japan':['Tokyo','Toyokawa','Yatomi']}
# }
#
# def visited_cities(cities_dict: dict) -> set:
#     city_set: set = set()
#     for k,values in cities_dict.items():
#         for i in values:
#             city_set.update(values[i])
#     return city_set
#
# print(visited_cities(my_cities))
#



# Create a function that receives my_cities and returns dictionary arranged as follows:
# Keys = cities
# Values = all dates when I was visiting the cities
# my_cities = {
#    2008:{'Germany':['Berlin', 'Munich'],
#            'France' :['Paris','Leon','Bordeaux']},
#    2009: {'China':['Hong Kong', 'Shanghai','Beijing'],
#             'Japan':['Nagoya','Toyokawa','Yatomi'],
#             'Mexico':['Tijuana','Ecatepec']},
#    2010: {'Germany': ['Berlin', 'Dusseldorf'],
#             'France': ['Paris', 'Nice', 'Bordeaux'],
#             'Japan':['Tokyo','Toyokawa','Yatomi']}
# }
#
# def orderd_cities(cities: dict) -> dict:
#     my_dict = dict()
#     for year, countries in cities.items():
#         for cities in countries.values():
#             for city in cities:
#                 if my_dict.get(city) is None:
#                     my_dict[city] = []
#                 my_dict[city].append(year)
#
#     return my_dict
#
# print(orderd_cities(my_cities))
#
#
#
# colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white', 'sky blue', 'pure purple', 'white cream', 'Eggshell white','Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
# colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz','white & Red', 'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure']
# def list_merge(l1: list[str],l2: list[str]) -> list:
#     colors_3: list[str] = list()
#     s3: set[str] = set(l1 + l2)
#     for color in s3:
#         colors_3.append(color.lower())
#     return colors_3
#
# print(list_merge(colors_1,colors_2))


volvo_catalog_old = {
     "trucks" :{
          "vnr" :{
            300:"Vnr-300",
            600:"Vnr-600",
          },
          "vnl" :{
             760:"Vnl-760",
             860:"Vnl-860",
          },
          "vnd" :{
             500:"Vnd-500",
             900:"Vnd-900",
          },
     },
     "private":{
         "s":{
             "S-30":"S-30",
             "S-40":"S-40",
             "S-60":"S-60",
             "S-80":"S-80",
             "S-90":"S-90",
         },
     },
        "production year":{
            2018:3223,
            2019:3435,
            2020:4334,
            2021:3232,
            2022:1234
        },
        "motor type":{
            "Diesel":1874,
            "Patrol":1242,
            "Electric":654,
            "Hydrogen":6343
     },
        "colors":{
            "orange":45,
            "green":898,
            "violet":67,
            "Red - Orange": 454,
            "Yellow - Orange": 767,
            "Yellow - Green": 876,
            "Blue - Green": 894,
            "Blue - Violet": 2334,
            "Red - Violet": 4343
        }
}

# I didn't know how to increase the amount of the "value"

# def volvo_catalog(current_catalog: dict) -> dict:
#     criterias = ["Vehicle_type","motor type","color","Year of production"]
#     new_car = dict()
#     times = int(input('number of cars '))
#     for criteria in criterias:
#         fields = input(f'please insert {criteria}: ').lower().strip()
#         if criteria == "Vehicle_type" and fields == "trucks":
#             trucks_model_dict: dict = {}
#             inputs = ["Class Model", "Name Model", "Number Model"]
#             inputs_for_insert = []
#             for inp in inputs:
#                 Model_trucks_inp = input(f'please insert {inp}: ').lower().strip()
#                 inputs_for_insert.append(Model_trucks_inp)
#             trucks_model_dict[inputs_for_insert[0]] = {int(inputs_for_insert[2]): inputs_for_insert[1]}
#             volvo_catalog_old["trucks"].update(trucks_model_dict)
#             new_car = trucks_model_dict
#         elif criteria == "Vehicle_type" and fields == "private":
#             private_model_dict: dict = {}
#             inputs = ["Class Model","Name Model","Number Model"]
#             inputs_for_insert = []
#             for inp in inputs:
#                 Model_private_inp = input(f'please insert {inp}: ').lower().strip()
#                 inputs_for_insert.append(Model_private_inp)
#             private_model_dict[inputs_for_insert[0]] = {int(inputs_for_insert[2]): inputs_for_insert[1]}
#             volvo_catalog_old["private"].update(private_model_dict)
#             new_car = private_model_dict
#         if criteria == "motor type":
#             motor_type_dict: dict = dict()
#             motor_type_dict = {fields:+times}
#             volvo_catalog_old["motor type"].update(motor_type_dict)
#         elif criteria == "color":
#             color_dict: dict = dict()
#             color_dict = {fields:+times}
#             volvo_catalog_old["colors"].update(color_dict)
#         elif criteria == "Year of production":
#             Year_of_production_dict: dict = dict()
#             Year_of_production_dict = {int(fields): + times}
#             volvo_catalog_old["production year"].update(Year_of_production_dict)
#     volvo_catalog_new = volvo_catalog_old
#     return volvo_catalog_new
#
# pprint.pprint(volvo_catalog(volvo_catalog_old))
#



















