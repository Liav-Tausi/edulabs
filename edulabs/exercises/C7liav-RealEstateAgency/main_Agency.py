from RealEstateAgency import RealEstateAgency
from Rent_Sale import ApartmentForRent, ApartmentForSale
from Apartment import Apartment




if __name__ == "__main__":
    agency: RealEstateAgency = RealEstateAgency()

    apartment1 = Apartment(apartment_num=24, address="zofit",
                           parking_type="garage", rooms_num=6,
                           size_in_sq_meters=250, floor=0,
                           deal_state="open",
                           monthly_municipal_tax=2000,
                           sale_price=8_500_000)

    apartment2 = Apartment(apartment_num=54, address="kfar saba",
                           parking_type="building", rooms_num=3,
                           size_in_sq_meters=150, floor=5,
                           deal_state="open",
                           monthly_municipal_tax=2000,
                           rent_per_month=7000)


    print(agency.add_apartment_for_sale(apartment1))
    print(agency.add_apartment_for_rent(apartment2))

    print(agency)

    print(agency.annual_rant(apartment2))

    print(agency.annual_municipal_tax(apartment2))

    print(agency.close_deal(apartment1))

    print(agency.is_for_rent(apartment2))
    print(agency.is_for_rent(apartment2))



