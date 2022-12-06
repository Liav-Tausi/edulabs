class Apartment:

    def __init__(self, apartment_num: int, address: str, parking_type: str, rooms_num: int,
                 floor: int, size_in_sq_meters: int, monthly_municipal_tax: float, deal_state: str,
                 rent_per_month: int = None, sale_price: int = None, is_penthouse: bool = None,
                 is_villa: bool = None, has_balcony: bool = None):

        self.deal_state: str = deal_state
        self.__parking_type: str = parking_type
        self.__address: str = address

        self.__monthly_municipal_tax: float = monthly_municipal_tax
        self.__size_in_sq_meters: int = size_in_sq_meters
        self.__rooms_num: int = rooms_num
        self.__apartment_num: int = apartment_num
        self.__sale_price: int = sale_price
        self.__rent_per_month: int = rent_per_month

        self.__floor: int = 0

        self.__is_villa: bool = False
        self.__is_penthouse: bool = False
        self.__has_balcony: bool = False


    def _get_apartment_num(self):
        return self.__apartment_num


    def _get_rent_per_month(self):
        return self.__rent_per_month


    def _monthly_municipal_tax(self):
        return self.__monthly_municipal_tax



