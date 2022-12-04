# from datetime import date
#
#
# class RavKav:
#
#     def __init__(self,holder_id: int, holder_name: str):
#         self.__riders_log: dict = dict()
#         self.__holder_id: int = holder_id
#         self.__rav_kav = 0
#         self.__balance = 0
#         self.__short: float = 15
#         self.__medium: float = 40
#         self.__long: float = 41
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
#     def ride_range(self, date: date, range_of_ride: float) -> bool:
#         if range_of_ride < self.__short or self.__balance > 5.5:
#             self.__balance -= 5.5
#             self.__riders_log[date] = {"range": {"short", range_of_ride}, "amount": 5.5}
#             return True
#         elif range_of_ride < self.__medium or self.__balance > 12:
#             self.__balance -= 12
#             self.__riders_log[date] = {"range": {"medium", range_of_ride}, "amount": 12}
#             return True
#         elif range_of_ride < self.__long or self.__balance > 23:
#             self.__balance -= 23
#             self.__riders_log[date] = {"range": {"long", range_of_ride}, "amount": 23}
#
#
#             return True
#         else:
#             return False
#
#
#     def get_current_balance(self) -> int:
#         return self.__balance
#
#
#     def get_rides_by_date(self, date_search: date) -> dict:
#         return self.__riders_log[date_search]
#
#
#     def get_rides_by_type(self, range: str) -> dict:
#         return self.__riders_log[date]["range"]
#
#
# if __name__ == "__main__":
#
#
#     ravkav = RavKav(1213, "LIAV")
#     ravkav.add_balance(50)
#
#     print(ravkav.ride_range(date(2022,12,5), 40))
#
#     print(ravkav.get_current_balance())
#     print(ravkav.get_rides_by_date(date(2022, 12, 5)))
#     print(ravkav.get_rides_by_type("short"))
#



