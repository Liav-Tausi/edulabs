from datetime import timedelta , datetime


class Table:

    TIME_LIMIT: timedelta = timedelta(minutes=90)

    def __init__(self, table_id: int, seats: int, table_location: str):

        self.table_location: str = table_location
        self.table_id: int = table_id
        self.seats: int = seats
        self.occupied_seats: int = 0
        self.available: bool = True
        self.reservation_time = datetime.now()
        self.reservation_limit = self.reservation_time + self.TIME_LIMIT



    def is_available(self):
        if self.available is True:
            return self.available
        else:
            return self.available


    def reserve_table(self, guests: int):
        if self.seats >= guests and self.available is True:
            self.occupied_seats += guests
            self.available = False
            return True
        else:
            return False



class TableReservationSystem:

    def __init__(self):
        self.seats_dict: dict[int: Table] = dict()
        self.reserved_tables: dict[int: Table] = dict()


    def add_table(self, table: Table) -> dict:
        if table.table_id not in self.seats_dict.keys():
            self.seats_dict[table.table_id] = table
        return self.seats_dict


    def reserve_table(self,table: Table, guests: int) -> bool:
        if table.reserve_table(guests) is True:
            self.reserved_tables[table.reservation_time] = {table.table_id: table}
            print(f"table reserved at {table.reservation_time} to {table.reservation_time + table.TIME_LIMIT}")
            return True
        else:
            return False


    def is_available_system(self,table: Table) -> None:
        if table.table_id in self.seats_dict and table.is_available() is True:
            print("table is available")
        else:
            print("table is unavailable")



    def time_left(self, table: Table) -> timedelta | bool:
        if table.table_id in self.reserved_tables or table.is_available() is True:
            return False
        else:
            time_left_for_table = table.reservation_limit - table.reservation_time
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
    print(table_system.reserved_tables)
    table_system.is_available_system(table4)


    print(table_system.time_left(table4))
















