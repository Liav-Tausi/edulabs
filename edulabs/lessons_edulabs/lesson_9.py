# from datetime import date, datetime
#
# class RavKav:
#
#     __rides = {'short': {'range': (0, 15), 'price': 5.5},
#                'medium': {'range': (16, 40), 'price': 12},
#                'long': {'range': (40, 1000), 'price': 40},
#                }
#     def __init__(self,holder_id: int, holder_name: str):
#         self.holder_name = holder_name
#         self.__riders_log: dict[int, dict] = dict()
#         self.__holder_id: int = holder_id
#         self.__rav_kav: int = 0
#         self.__balance: int = 0
#         self.__rides_types: list[str] = []
#         self.__rides_date: list[date] = []
#
#
#     def add_balance(self, amount: int) -> bool:
#         if amount > 0:
#             self.__balance += amount
#             return True
#         else:
#             return False
#
#
#
#     def ride_range(self, range_of_ride: float, date_of_ride: str,) -> bool | str:
#         date_log = datetime.strptime(date_of_ride, "%d-%m-%Y")
#         if range_of_ride > 0 or self.__balance > 0:
#             for key, value in RavKav.__rides.items():
#                 if value["range"][0] <= range_of_ride <= value["range"][1]:
#                     self.__rides_types.append(key)
#                     self.__rides_date.append(date_log)
#                     self.__riders_log[self.__holder_id] = {"ride_type": key,
#                                                            "km": range_of_ride,
#                                                            "price": value["price"],
#                                                            "date": date_log}
#
#                     return key
#         else:
#             return False
#
#
#     def get_current_balance(self) -> int:
#         return self.__balance
#
#     def get_rides_by_date(self, date_search: str) -> int:
#         if self.__holder_id in self.__riders_log:
#             dates: datetime = datetime.strptime(date_search, "%d-%m-%Y")
#             return self.__rides_date.count(dates)
#
#     def get_rides_by_type(self, ride_type: str) -> int:
#         if self.__holder_id in self.__riders_log:
#             return self.__rides_types.count(ride_type)
#
#
#
#
# if __name__ == "__main__":
#
#     rav_kav = RavKav(1213, "LIAV")
#     rav_kav.add_balance(50)
#
#     rav_kav.get_current_balance()
#     rav_kav.ride_range(40, "12-05-2002")
#     print(rav_kav._RavKav__rides_date)
#     print(rav_kav.get_rides_by_date("12-05-2002"))
#     print(rav_kav.get_rides_by_type("medium"))
#
#


#

#
# # class EBook:
#
#     def __init__(self, file: str, words_per_page: int):
#
#         self.__file: str = file
#         self.__pages: dict[int, str] = {}
#
#         with open(file, "r") as file_handler:
#             content: list[str] = file_handler.read().split()
#
#         page_num = 1
#         for i in range(0,len(content), words_per_page):
#             page_words = content[i:i+words_per_page]
#             self.__pages[words_per_page] = " ".join(page_words)
#             page_num += 1
#
#
#     def get_total_pages(self):
#         return len(self.__pages)
#
#
#     def display_content_for_page(self, page_num: int) -> str:
#         return self.__pages[page_num]
#
#
#
#
#
#
# relative_path = "data\\alice_in_wonderland.txt" # relative from the file it's at and to the folder the files in
# absolute_path = "C:\\Users\\liavt\\PycharmProjects\\LernningPython\\edulabs\\lessons_edulabs" # not good, not the same at every computar
# file_handler = open(relative_path, 'r')
#
# file_handler.close()
#
# # ==
# #
# with open(relative_path,"r") as file_handler:
#     file_handler.read()
#
#













