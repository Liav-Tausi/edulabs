class Apartment:

    def __init__(self, apartment_num: int, address: str, parking_type: str, rooms_num: int,
                 size_in_sq_meters: int, monthly_municipal_tax: float, deal_state: str,
                 rent_per_month: int = None, sale_price: int = None, is_penthouse: bool = None,
                 is_villa: bool = None, has_balcony: bool = None):

        self.__is_penthouse = is_penthouse
        self.__is_villa: bool = is_villa
        self.__has_balcony: bool = has_balcony
        self.__deal_state: str = deal_state
        self.__parking_type: str = parking_type
        self.__address: str = address

        self.__monthly_municipal_tax: float = monthly_municipal_tax
        self.__size_in_sq_meters: int = size_in_sq_meters
        self.__rooms_num: int = rooms_num
        self.__apartment_num: int = apartment_num
        self.__sale_price: int = sale_price
        self.__rent_per_month: int = rent_per_month

        self.__floor: int = 0

        self.for_rent: dict[int, Apartment] = dict()

        self.for_sale: dict[int, Apartment] = dict()


    def get_apartment_num(self):
        return self.__apartment_num

    def get_for_rent_dict(self):
        return self.for_rent

    def get_for_sale_dict(self):
        return self.for_sale




class ApartmentForRent(Apartment):

    def __init__(self, apartment_num: int, address: str, parking_type: str, rooms_num: int,
                 size_in_sq_meters: int, monthly_municipal_tax: float, deal_state: str,
                 rent_per_month: int = None, sale_price: int = None, is_penthouse: bool = None,
                 is_villa: bool = None, has_balcony: bool = None):

        super().__init__(apartment_num, address, parking_type, rooms_num,
                         size_in_sq_meters, monthly_municipal_tax, deal_state, rent_per_month,
                         sale_price, is_penthouse, is_villa, has_balcony)

        def add_apartment_for_sale(apartment: Apartment) -> bool:
            if apartment.get_apartment_num() in apartment.get_for_sale_dict():
                return True



class ApartmentForSale(Apartment):

    def __init__(self, apartment_num: int, address: str, parking_type: str, rooms_num: int,
                 size_in_sq_meters: int, monthly_municipal_tax: float, deal_state: str,
                 rent_per_month: int = None, sale_price: int = None, is_penthouse: bool = None,
                 is_villa: bool = None, has_balcony: bool = None):

        super().__init__(apartment_num, address, parking_type, rooms_num,
                         size_in_sq_meters, monthly_municipal_tax, deal_state, rent_per_month,
                         sale_price, is_penthouse, is_villa, has_balcony)



if __name__ == "__main__":
    apartment1 = Apartment(apartment_num=24, address="zofit",
                                  parking_type="garage", rooms_num=6,
                                  size_in_sq_meters=250,
                                  deal_state="open",
                                  monthly_municipal_tax=2000,
                                  sale_price=8_500_000)



    apartment2 = ApartmentForSale(apartment_num=54, address="kfar saba",
                                  parking_type="building", rooms_num=3,
                                  size_in_sq_meters=150,
                                  deal_state="open",
                                  monthly_municipal_tax=2000,
                                  rent_per_month=7000)


