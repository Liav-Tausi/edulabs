from BusMenusUi import *
import pickle
import os


if __name__ == "__main__":

    if not os.path.exists('bus_company.pickle'):
        bus_company = BestBusCompany("liav's busses")
    else:
        with open('bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)

    MainMenu(bus_company).run()

    with open('bus_company.pickle', 'wb') as fh:
        pickle.dump(bus_company, fh)



