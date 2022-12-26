from rent_sale import ApartmentForRent, ApartmentForSale
from apartment import Apartment


class RealEstateAgency:

    def __init__(self):

        self.__apartments_for_sale: dict[int, ApartmentForSale] = dict()

        self.__apartments_for_rent: dict[int, ApartmentForRent] = dict()

    def __repr__(self):
        return f"rent: {self.__apartments_for_rent} | sale: {self.__apartments_for_sale}"

    def add_apartment_for_sale(self, apartment: Apartment) -> bool:
        for_sale = ApartmentForSale(apartment)
        if for_sale.apartment._get_apartment_num() not in self.__apartments_for_sale:
            if apartment.deal_state == "open":
                self.__apartments_for_sale[for_sale.apartment._get_apartment_num()] = for_sale
                return True
            raise KeyError
        raise KeyError

    def add_apartment_for_rent(self, apartment: Apartment) -> bool:
        for_rent = ApartmentForRent(apartment)
        if for_rent.apartment._get_apartment_num() not in self.__apartments_for_rent:
            if apartment.deal_state == "open":
                self.__apartments_for_rent[for_rent.apartment._get_apartment_num()] = for_rent
                return True
            raise KeyError
        raise KeyError

    def annual_rant(self, apartment: Apartment) -> int:
        if apartment._get_apartment_num() in self.__apartments_for_rent.keys():
            return apartment._get_rent_per_month() * 12
        raise KeyError

    def annual_municipal_tax(self, apartment: Apartment) -> int:
        if apartment._get_apartment_num() in self.__apartments_for_rent.keys() \
                or apartment._get_apartment_num() in self.__apartments_for_sale.keys():
            return apartment._monthly_municipal_tax() * 12
        raise KeyError


    def close_deal(self, apartment: Apartment) -> None:
        if apartment._get_apartment_num() in self.__apartments_for_rent.keys() \
                and apartment.deal_state == "open":
            self.__apartments_for_rent[apartment._get_apartment_num()].apartment.deal_state = "closed"
            print("deal closed")
        if apartment._get_apartment_num() in self.__apartments_for_sale.keys() \
                and apartment.deal_state == "open":
            self.__apartments_for_sale[apartment._get_apartment_num()].apartment.deal_state = "closed"
            print("deal closed")
        raise KeyError


    def is_for_rent(self, apartment: Apartment) -> bool:
        if apartment._get_apartment_num() in self.__apartments_for_rent.keys() \
                and apartment.deal_state == "open":
            return True
        return False

    def is_for_sale(self, apartment: Apartment) -> bool:
        if apartment._get_apartment_num() in self.__apartments_for_rent.keys() \
                and apartment.deal_state == "open":
            return True
        return False
