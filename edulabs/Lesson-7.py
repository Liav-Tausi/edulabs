from pprint import pprint
#
# # my_car = {
# #     'manufacturer': 'Mazda',
# #     'model': '3',
# #     'color': 'white',
# #     'license_plate': '1234567',
# #     'year': 2015,
# #     'fuel': 50,
# #     'km': 102000,
# #     'fuel_consumption': 20
# # }
# #
# # def add_fuel(car, liters):
# #     car['fuel'] += liters
# #
# # def drive(car, km):
# #     car['km'] += km
# #
# #
# #
# # if __name__ == '__main__':
# #     add_fuel(my_car, 2)
# #     drive(my_car, 100)
# #     drive(my_car, -300)
# #     pprint(my_car)
#
#
# # what should we do if we also want to update info about fuel left?
#
#
#
# # We want something like (pseudocode - will not run!):
#
# # Create an object, it has internal state
# # car = Car(manufacturer='Mazda', model='3', fuel=50,...)
#
# # "Use" the object bu applying actions on it - and internal state will change accordingly
# # (increas km), add/reduce fuel, etc...
# # car.add_fuel(liters=20)
# # car.drive(km=200)
# # car.get_fuel_left()
# # car.is_out_of_fuel()
# # ...
#
# # Cars “remember” things about their current state
# # Cars functions (methods) that can change that state
# # We can manage each car separately
#
#
# class Car:
#     def __init__(self, manufacturer: str, model: str,
#                  color: str, fuel_consumption: float,
#                  fuel_tank_capacity: float,
#                  year: int = None):
#         print(f"Inside __init__ of {manufacturer}")
#         self.manufacturer: str = manufacturer
#         self.model: str = model
#         self.color: str = color
#         self.fuel_consumption = fuel_consumption
#         self.fuel_tank_capacity = fuel_tank_capacity
#         self.km: int = 0
#         self.fuel: float = 0
#         self.year: int = year
#         self.mintenenance = dict()
#
#     def __str__(self):
#         print("Inside __str__")
#         return f"{self.manufacturer} | Model: {self.model} | Year: {self.year}"
#
#
#
#     def fill_tank(self, amnt: float) -> bool:
#
#         print(f"Inside fill_tank, amount: {amnt}")
#         if amnt <= 0:
#             print("Non-positive amnt is not allowed")
#             return False
#         if amnt + self.fuel > self.fuel_tank_capacity:
#             print(f"Cannot fill more than the tank capacity."
#                   f"Current capacity is: {self.fuel_tank_capacity}")
#             return False
#
#         self.fuel += amnt
#         return True
#
#     def fill_to_full(self):
#         self.fuel = self.fuel_tank_capacity
#
#     def drive(self,km_driven: float):
#         if (self.fuel_consumption / 100) * km_driven <= self.fuel:
#             self.km += km_driven
#             self.fuel -= (self.fuel_consumption / 100) * km_driven
#             return True
#         else:
#             print("erorr")
#             return False
#
#     def add_miant(self,date,description):
#        m_list = self.mintenenance.get(date , [])
#        m_list.append(description)
#        self.mintenenance[date] = m_list
#        # self.mintenenance[date] = description
#        print("maintenance added")
#
#
#     def display_all(self):
#         pprint(self.mintenenance)
#
#
#     def display_dashboard(self):
#         print(f"Dashboard for {self.manufacturer} {self.model}")
#         print('====================')
#         print(f"Fuel left: {self.fuel}")
#         print(f"Km: {self.km}")
#         print('====================')
#
#
#
#
#
#
#
#
#
#
# # car_mazda: Car = Car('Mazda', '3', color='white')
# # car_toyota = Car('Toyota', 'Yaris', 'red', 2020)
# # print(car_mazda)
# # print(car_toyota)
# # print(isinstance(car_mazda, Car))
# # print(car_mazda is Car)
# # my_car = car_mazda
# # print(car_mazda is my_car)
#
# # l = list()
# # s = set([3,4,3,5])
#
#
# # car1 = Car()
# # Car.__init__()
# # print(car.manufacturer, car.model, car.color)
# # print(car.__init__)
# # print(car)
#
# # print(Car)
# # print(str)
#
#
# mazda_car = Car('Mazda', '3 Spirit', 'white',
#                 fuel_consumption=20, fuel_tank_capacity=60, year=2015)
#
# toyota_car = Car('Toyota', 'Yaris', 'red',
#                  fuel_consumption=25, fuel_tank_capacity=40, year=2022)
#
# # mazda_car.fill_tank()
# # Car.fill_tank(mazda_car)
#
#
# mazda_car.fill_tank(60)
# mazda_car.drive(100)
# mazda_car.display_dashboard()
# # mazda_car.fill_tank(100)
# # mazda_car.display_dashboard()
# # while not is_success:
# #     is_success = mazda_car.fill_tank(20)
#
#
#
# mazda_car.add_miant("23.11.2022","10000 main")
# mazda_car.display_all()
# mazda_car.add_miant("23.11.2022","new 10000 main")
# mazda_car.display_all()
# mazda_car.add_miant("24.11.2022","fix crash")
# mazda_car.display_all()


import math

# class Point2D:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def translate(self, dx, dy):
#         self.x += dx
#         self.y += dy
#
#     def __str__(self):
#         return f"({self.x},{self.y})"
#
#     def __eq__(self, other):
#         print("inside __eq__ of Point2D")
#         if not isinstance(other, Point2D):
#             return False
#         return self.x == other.x and self.y == other.y
#
#     def __ne__(self, other):
#         print("inside __ne__ of Point2D")
#         return self.x != other.x or self.y != other.y
#
#     def __add__(self, other):
#         if not isinstance(other, Point2D):
#             return None
#         print("inside __add___ of x and y")
#         new_point = Point2D(self.x + other.x) , (self.y + other.y)
#         return new_point


    # def distance_from(self, other):
    #     dx = self.__x - other.__x
    #     dy = self.__y - other.__y
    #     dist = math.sqrt(dx ** 2 + dy ** 2)
    #     return dist
    #
    # def __str__(self):
    #     return f"({self.__x},{self.__y})"

# class Convert:
#         def __init__(self):
#             self.exchange_rates: dict = dict()
#
#         def add_exchange_rate(self, currency: str, rate: float):
#             self.exchange_rates[currency] = rate
#
#         def convert_from_usd(self, currency, amount) -> float:
#             if currency in self.exchange_rates:
#                 return amount * self.exchange_rates[currency]
#             else:
#                 print("not in data")
#
#         def convert_to_usd(self, currency, amount):
#             if currency in self.exchange_rates:
#                 return amount / self.exchange_rates[currency]
#             else:
#                 print("not in data")





# if __name__ == '__main__':
#     p1 = Point2D()
#     p2 = Point2D(2, 5)
#     print(p1, p2)
#     p2.translate(-2, -2)
#     p1.translate(3, 3)
#     print(p1)
#     print(p2)
#     p3 = Point2D(0, 3)
#     print(f"p1: {p1}, p2: {p2}, p3:{p3}")
#     print(f"p2 == p3: {p2 == p3}")
#     print(f"p2 == p1: {p2 == p1}")
#     print(f"p2 != p3: {p2 != p3}")
#     print(p2 == "hello")
#     # print("hello" == 'world')
#     p2 + p3
#     converter = Convert()
#     converter.add_exchange_rate("nis", 3.16)
#     converter.add_exchange_rate("yen", 113.73)
#     converter.add_exchange_rate("eruo", 0.89)
#     yens = converter.convert_from_usd("yen", 10_000)
#     dollars = converter.convert_to_usd("yen", 10_000)
#     print(f"10000 usd = {yens}")
#     print(f"10000 yen = {dollars} usd")


    # s1 = input()
    # s2 = input()
    # print(s1 == s2)
    # print(s1 is s2)
































