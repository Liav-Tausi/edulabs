import random


class Address:

    def __init__(self,country: str, city: str, street: str,):
        self.street: str = street
        self.city: str = city
        self.country: str = country
        self.neighborhood: dict[int, Building] = dict()




class Room:

    def __init__(self):
        for i in range( random.randint(3,5)):
            self.size_of_room: int = random.randint(10, 40)


class Flat:

    def __init__(self, room: Room, amount_of_rooms: int, flat_num: int, flat_floor: int):
        self.amount_of_rooms: int = amount_of_rooms
        self.balcony: int = random.randint(0, 2)
        self.base_arnona = 1000
        self.rooms: dict[int, Room] = {flat_num: room}

    def __str__(self):
        return f"{self.rooms}"


    def avg_size_room(self, room: Room):
       return self.amount_of_rooms + room.size_of_room / 2


    def number_of_rooms(self) -> int:
        pass


    def size_of_balc(self):
        pass


class Building:

    def __init__(self, address: Address, num_of_building: int, num_of_floors: int):
        self.address: Address = address
        self.num_of_building = num_of_building
        self.num_of_floors = num_of_floors
        self.flats: dict[int, Flat] = dict()


    def total_size(self, flat: Flat) -> int:
        if flat.amount_of_rooms in self.flats:
            flat.amount_of_rooms
            pass


if __name__ == "__main__":
    address: Address = Address("israel","Tal-Aviv","ben_yehuda")
    Building(address, num_of_building=5, num_of_floors=10)
    room = Room()
    flat = Flat(room, 5, 2, 10)



