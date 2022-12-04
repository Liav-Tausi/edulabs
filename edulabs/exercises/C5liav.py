from datetime import timedelta , datetime


class Table:

    TIME_LIMIT: timedelta = timedelta(minutes=90)

    def __init__(self, table_id: int, seats: int, table_location: str):

        self.__table_location: str = table_location
        self.__table_id: int = table_id
        self.__seats: int = seats
        self.__occupied_seats: int = 0
        self.__available: bool = True
        self.__reservation_time = datetime.now()
        self.__reservation_limit = self.__reservation_time + self.TIME_LIMIT


    def __repr__(self):
        return f"{self.__occupied_seats}, {self.__seats}, {self.__table_location}"


    def is_available(self):
        if self.available is True:
            return self.available
        else:
            return self.available


    def reserve_table(self, guests: int):
        if self.__seats >= guests and self.__available is True:
            self.__occupied_seats += guests
            self.available = False
            return True
        else:
            return False


    def get_table_id(self):
        return self.__table_id


    def get_reservation_time(self):
        return self.__reservation_time


    def get_reservation_limit(self):
        return self.__reservation_limit


class TableReservationSystem:

    def __init__(self):
        self.__seats_dict: dict[int: Table] = dict()
        self.__reserved_tables: dict[int: Table] = dict()


    def add_table(self, table: Table) -> dict:
        if table.get_table_id() not in self.__seats_dict.keys():
            self.__seats_dict[table.get_table_id()] = table
        return self.__seats_dict


    def reserve_table(self,table: Table, guests: int) -> bool:
        if table.reserve_table(guests) is True:
            self.__reserved_tables[table.get_table_id()] = {table.get_reservation_time(): table}
            print(f"table reserved at {table.get_reservation_time()} to {table.get_reservation_time() + table.TIME_LIMIT}")
            return True
        else:
            return False


    def is_available_system(self,table: Table) -> None:
        if table.get_table_id() in self.__seats_dict and table.is_available() is True:
            print("table is available")
        else:
            print("table is unavailable")



    def time_left(self, table: Table) -> timedelta | bool:
        if table.get_table_id() in self.__reserved_tables or table.is_available() is True:
            return False
        else:
            time_left_for_table = table.get_reservation_limit() - table.get_reservation_time()
            return time_left_for_table




if __name__ == "__main__":
    table_system = TableReservationSystem()

    table1 = Table(table_id=1122, seats=5, table_location="Bar")
    table2 = Table(table_id=2314, seats=6, table_location="Terrace")
    table3 = Table(table_id=2211, seats=5, table_location="Indoors")
    table4 = Table(table_id=1253, seats=7, table_location="Indoors")

    table_system.add_table(table1)
    table_system.add_table(table2)
    table_system.add_table(table3)
    table_system.add_table(table4)

    table_system.is_available_system(table4)
    table_system.reserve_table(table4, 7)
    table_system.reserve_table(table1, 3)
    table_system.is_available_system(table4)


    print(table_system.time_left(table4))
















