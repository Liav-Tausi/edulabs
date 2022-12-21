from BusMenusUi import *
import pickle
import os


if __name__ == "__main__":
    try:
        if not os.path.exists('bus_company.pickle'):
            bus_company = BestBusCompany("liav's busses")
        else:
            with open('bus_company.pickle', 'rb') as fh:
                bus_company = pickle.load(fh)

        MainMenu(bus_company).run()

    except Exception():
        print("Error restart program.")

    finally:
        with open('bus_company.pickle', 'wb') as fh:
            pickle.dump(bus_company, fh)




