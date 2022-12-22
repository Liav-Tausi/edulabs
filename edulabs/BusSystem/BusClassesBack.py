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

    def __str__(self):
        scheduled_rides_str = []
        for ride in self.__scheduled_rides:
            scheduled_rides_str.append(str(ride))
        return f"route number: {self.__route_number} | from: {self.__origin} | to: {self.__destination} | stops: {self.__stops} | scheduled rides: {scheduled_rides_str}"

    def __repr__(self):
        return f"route number: {self.__route_number} | from: {self.__origin} | to: {self.__destination} | stops: {self.__stops}"

        # getters

    def _get_route_number(self) -> int:
        return self.__route_number

    def _get_origin(self) -> str:
        return self.__origin

    def _get_destination(self) -> str:
        return self.__destination

    def _get_bus_stops(self) -> list[str]:
        return self.__stops

    def _set_origin(self, new_origin: str) -> None:
        self.__origin = new_origin

    def _set_destination(self, new_destination: str) -> None:
        self.__destination = new_destination

    def _set_bus_stops(self, new_stops: list[str]) -> None:
        self.__stops = new_stops

    def _get_scheduled_rides(self) -> list['ScheduledRide']:
        return self.__scheduled_rides

    def add_scheduled_ride(self, scheduled_ride: 'ScheduledRide') -> None:
        self.__scheduled_rides.append(scheduled_ride)


class ScheduledRide:

    def __init__(self, origin_time: str, destination_time: str, driver_name: str):
        self.__id = random.randint(1, 10000)
        self.__origin_time: datetime = datetime.strptime(origin_time, "%H:%M")
        self.__destination_time: datetime = datetime.strptime(destination_time, "%H:%M")
        self.__driver_name: str = driver_name
        self.__delays: datetime = datetime.strptime("00:00", "%H:%M")

    def __str__(self):
        difference = self.__destination_time - self.__origin_time
        return f"Ride id: {self.__id} | Scheduled departure: {self.__origin_time.time()} |" \
               f" Estimated delay: {self.__delays.minute} minutes | scheduled arrival time: {self.__destination_time.time()}" \
               f"| Drive time: {difference}"

    # getters
    def _get_id(self) -> int:
        return self.__id

    def _get_origin_time(self) -> datetime:
        return self.__origin_time

    def _get_destination_time(self) -> datetime:
        return self.__destination_time

    # usable functions
    def add_delay(self, delay: str):
        delay_time = datetime.strptime(delay, "%M")
        delay_timedelta = timedelta(hours=delay_time.hour, minutes=delay_time.minute)
        if delay_timedelta >= timedelta():
            self.__delays = delay_time
            self.__destination_time += delay_timedelta
        else:
            raise Exception("negative delay not allowed.")


class BestBusCompany:

    def __init__(self, name: str):
        # bus_routes storage
        self.__bus_routes: dict[int, BusRoute] = dict()
        # company name
        self.__name: str = name

    def __str__(self):
        return f"{self.__bus_routes}"

    def _get_bus_rotes(self) -> dict[int, BusRoute]:
        return self.__bus_routes

    def _get_name(self):
        return self.__name

    def update(self, line_number: int, new_origin: str = None, new_destination: str = None, new_stops: list[str] = None,
               update_origin: bool = False, update_destination: bool = False, update_stops: bool = False):
        if line_number in self.__bus_routes:
            if update_origin:
                self.__bus_routes[line_number]._set_origin(new_origin)
            if update_destination:
                self.__bus_routes[line_number]._set_destination(new_destination)
            if update_stops:
                self.__bus_routes[line_number]._set_bus_stops(new_stops)
        else:
            raise ValueError("Line number not found.")

    def add_route(self, bus_route: BusRoute) -> None:
        if bus_route._get_route_number() in self.__bus_routes:
            raise ValueError("Route number already exists.")
        self.__bus_routes[bus_route._get_route_number()] = bus_route

    def delete_route(self, line_number: int):
        if line_number in self.__bus_routes:
            del self.__bus_routes[line_number]
        else:
            raise Exception("Route not in system.")

    def _get_route_info(self, line_number: int = None, origin: str = None, destination: str = None,
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
                if route._get_origin() == origin:
                    matching_routes.append(route)
            return matching_routes
        elif destination:
            # Search by destination
            matching_routes = []
            for route in self.__bus_routes.values():
                if route._get_destination() == destination:
                    matching_routes.append(route)
            return matching_routes
        elif bus_stop:
            # Search by bus stops
            matching_routes = []
            for route in self.__bus_routes.values():
                if bus_stop in route._get_bus_stops():
                    matching_routes.append(route)
            return matching_routes
        else:
            raise Exception("No search criteria provided")
