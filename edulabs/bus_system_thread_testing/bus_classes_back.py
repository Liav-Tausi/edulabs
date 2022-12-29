import time
import random
import string
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
import random


class BusRoute:
    """
    this class defines the bus route object that contains the information about a bus route

    """

    def __init__(self, route_number: int, origin: str, destination: str, stops: list[str]):
        self.__route_number: int = route_number
        self.__origin: str = origin
        self.__destination: str = destination
        self.__stops: list[str] = stops
        self.__scheduled_rides: list[ScheduledRide] = list()

        self.lock1: 'threading' = threading.Lock()
        self.lock2: 'threading' = threading.Lock()
        self.lock3: 'threading' = threading.Lock()

    def __str__(self):
        scheduled_rides_str = []
        for ride in self.__scheduled_rides:
            scheduled_rides_str.append(str(ride))
        return f"route number: {self.__route_number} | from: {self.__origin} | to: {self.__destination} | stops: {self.__stops} | scheduled rides: {scheduled_rides_str}"

    def __repr__(self):
        return f"route number: {self.__route_number} | from: {self.__origin} | to: {self.__destination} | stops: {self.__stops}"

        # getters

    def get_route_number(self) -> int:
        return self.__route_number

    def get_origin(self) -> str:
        return self.__origin

    def get_destination(self) -> str:
        return self.__destination

    def get_bus_stops(self) -> list[str]:
        return self.__stops

    def set_origin(self, new_origin: str) -> None:
        with self.lock1:
            self.__origin = new_origin

    def set_destination(self, new_destination: str) -> None:
        with self.lock2:
            self.__destination = new_destination
            print(self.__destination)

    def set_bus_stops(self, new_stops: list[str]) -> None:
        with self.lock3:
            self.__stops = new_stops

    def get_scheduled_rides(self) -> list['ScheduledRide']:
        return self.__scheduled_rides

    def add_scheduled_ride(self, scheduled_ride: 'ScheduledRide') -> None:
        self.__scheduled_rides.append(scheduled_ride)


class ScheduledRide:
    """
    this class defines the scheduled ride object that contains the information about a scheduled ride

    """

    def __init__(self, origin_time: str, destination_time: str, driver_name: str):
        self.__id = random.randint(1, 10000)
        self.__origin_time: datetime = datetime.strptime(origin_time, "%H:%M")
        self.__destination_time: datetime = datetime.strptime(destination_time, "%H:%M")
        self.__driver_name: str = driver_name
        self.__delays: datetime = datetime.strptime("00:00", "%H:%M")

        self.lock1: 'threading' = threading.Lock()

    def __str__(self):
        difference = self.__destination_time - self.__origin_time
        return f"Ride id: {self.__id} | Scheduled departure: {self.__origin_time.time()} |" \
               f" Estimated delay: {self.__delays.minute} minutes | scheduled arrival time: {self.__destination_time.time()}" \
               f"| Drive time: {difference}"

    # getters
    def get_id(self) -> int:
        return self.__id

    def get_origin_time(self) -> datetime:
        return self.__origin_time

    def get_destination_time(self) -> datetime:
        return self.__destination_time

    # usable functions
    def add_delay(self, delay: str):
        delay_time = datetime.strptime(delay, "%M")
        delay_timedelta = timedelta(hours=delay_time.hour, minutes=delay_time.minute)
        if delay_timedelta >= timedelta():
            with self.lock1:
                self.__delays = delay_time
                self.__destination_time += delay_timedelta
        else:
            raise Exception("negative delay not allowed.")


class BestBusCompany:
    """
    this class defines the bus company object that contains the information about the bus routes

    """

    def __init__(self, name: str):
        # bus_routes storage
        self.__bus_routes: dict[int, BusRoute] = dict()
        # company name
        self.__name: str = name

    def __str__(self):
        return f"{self.__bus_routes}"

    def get_bus_rotes(self) -> dict[int, BusRoute]:
        return self.__bus_routes

    def get_name(self):
        return self.__name

    def update(self, thread_num, line_number: int, new_origin: str = None, new_destination: str = None, new_stops: list[str] = None,
               update_origin: bool = False, update_destination: bool = False, update_stops: bool = False):
        if line_number in self.__bus_routes:
            if update_origin:
                self.__bus_routes[line_number].set_origin(new_origin)
            elif update_destination:
                print(f'{thread_num} starting the change...')
                self.__bus_routes[line_number].set_destination(new_destination)
                print(f'{thread_num} finished the change...')
            elif update_stops:
                self.__bus_routes[line_number].set_bus_stops(new_stops)
        else:
            raise ValueError("Line number not found.")

    def add_route(self, bus_route: BusRoute) -> None:
        if bus_route.get_route_number() in self.__bus_routes:
            raise ValueError("Route number already exists.")
        self.__bus_routes[bus_route.get_route_number()] = bus_route

    def delete_route(self, line_number: int):
        if line_number in self.__bus_routes:
            del self.__bus_routes[line_number]
        else:
            raise Exception("Route not in system.")

    def get_route_info(self, line_number: int = None, origin: str = None, destination: str = None,
                       bus_stop: str = None):
        if line_number:
            # Search by line number
            if int(line_number) not in self.__bus_routes.keys():
                raise Exception("Route not found")
            else:
                route = self.__bus_routes[line_number]
                return route
        elif origin:
            # Search by origin
            matching_routes = []
            for route in self.__bus_routes.values():
                if route.get_origin() == origin:
                    matching_routes.append(route)
            return matching_routes
        elif destination:
            # Search by destination
            matching_routes = []
            for route in self.__bus_routes.values():
                if route.get_destination() == destination:
                    matching_routes.append(route)
            return matching_routes
        elif bus_stop:
            # Search by bus stops
            matching_routes = []
            for route in self.__bus_routes.values():
                if bus_stop in route.get_bus_stops():
                    matching_routes.append(route)
            return matching_routes
        else:
            raise Exception("No search criteria provided")


if __name__ == '__main__':

    start = time.perf_counter()
    bus_company = BestBusCompany("liav's")
    route1 = BusRoute(route_number=1234, destination='zofit', origin='kfar saba', stops=['sfasf', 'sfasfsa', 'fafsaf'])
    route2 = BusRoute(route_number=4312, destination='zofit', origin='kfar saba', stops=['sfasf', 'sfasfsa', 'fafsaf'])

    bus_company.add_route(route1)
    bus_company.add_route(route2)

    with ThreadPoolExecutor() as executor:
        for j in range(10_000):
            letters = string.ascii_lowercase
            result_str = ''.join(random.choice(letters))
            future = [executor.submit(bus_company.update, j, 1234, new_destination=result_str, update_destination=True)]

    # with ThreadPoolExecutor() as executor:
    #     for i in range(10_000):
    #         letters = string.ascii_lowercase
    #         result_str = ''.join(random.choice(letters))
    #         future = [executor.submit(bus_company.update, i, 4312, new_destination=result_str, update_destination=True)]

    end = time.perf_counter()
    print(bus_company.get_bus_rotes())
    print(f'time took {end - start} second(s)')
