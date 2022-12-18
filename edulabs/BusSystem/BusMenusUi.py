from BusValidations import *
from BusClassesBack import BestBusCompany, BusRoute, ScheduledRide


class MainMenu:
    def __init__(self, bus_company: BestBusCompany):
        self.bus_company = bus_company

    def run(self):

        while True:
            # display the main menu
            print("""
                       Welcome to the Best Bus Company!
                       
                         .--------------------------.
                        /| _ .---. .---. .---. .---.|
                        |j||||___| |___| |___| |___||
                        |=|||=======================|
                        [_|j||(O)\__________|(O)\___]
                        
                       Are you a manager or a passenger?
                                  
             [1]-> Manager   |   [2]-> Passenger   |   [3]-> Exit
            """)
            # get the user's choice
            choice = input("Enter your choice: ")

            if choice == "1":
                password_attempts = 1
                while password_attempts < 3:
                    password = input("Enter the password: ").strip()
                    if password == "RideWithUs!":
                        Manager(self.bus_company).run()
                        break
                    else:
                        password_attempts += 1
                if password_attempts == 3:
                    raise KeyError("Log in failed")

            elif choice == "2":
                Passenger(self.bus_company).run()

            elif choice == "3":
                break


class Passenger(MainMenu):

    def run(self):
        while True:
            print("""
                            Welcome passenger!
                            
          Which of the following actions would you'd like to perform?
                            
         [1]-> Search route
                            [2]-> Report delay
                                                [3]-> Back to main menu
                """)

            choice = input("Enter your choice: ")

            if choice == "1":
                search_method = input(
                    "Enter the method you would like to search by (line number, origin, destination, bus stop): ").lower().strip()

                while search_method not in ["line number", "origin", "destination", "bus stop"]:
                    search_method = input(
                        "\033[0;31;1mTry Again!\033[0;30;0m search by (line number, origin, destination, bus stop): ").lower().strip()

                if search_method == "line number":
                    line_number = input("Enter the line number: ")
                    while is_num(line_number) is False or int(
                            line_number) not in self.bus_company._get_bus_rotes().keys() or len(line_number) == 0:
                        line_number = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the line's number: ").strip()
                    routes = self.bus_company._get_route_info(int(line_number))
                    if routes:
                        print(f"Route information : {routes}")
                    else:
                        print("Route not found")

                elif search_method == "origin":
                    origin = input("Enter the origin: ").lower().strip()
                    while is_num(origin) is True:
                        origin = input("\033[0;31;1mTry Again!\033[0;30;0m Enter the origin: ").lower().strip()
                    routes = self.bus_company._get_route_info(origin=origin)
                    if routes:
                        print(f"Route information : {routes}")
                    else:
                        print("No routes found")

                elif search_method == "destination":
                    destination = input("Enter the destination: ").lower().strip()
                    while is_num(destination) is True:
                        destination = input("\033[0;31;1mTry Again!\033[0;30;0m Enter the destination: ").lower().strip()
                    routes = self.bus_company._get_route_info(destination=destination)
                    if routes:
                        print(f"Route information : {routes}")
                    else:
                        print("No routes found")

                elif search_method == "bus stop":
                    bus_stop = input("Enter bus stop: ").lower().strip()
                    while is_num(bus_stop) is True:
                        bus_stop = input("\033[0;31;1mTry Again!\033[0;30;0m Enter the bus stop: ").lower().strip()
                    # while bus_stop
                    routes = self.bus_company._get_route_info(bus_stop=bus_stop)
                    if routes:
                        print(f"Route information : {routes}")
                    else:
                        print("No routes found")

            elif choice == "2":
                line_number = input("Insert the line's number: ").strip()
                while is_num(line_number) is False or int(
                        line_number) not in self.bus_company._get_bus_rotes().keys() or len(line_number) == 0:
                    line_number = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the line's number: ").strip()

                o_time = input("Insert the departure time (in H:M format): ")
                while len(o_time) != 5 or is_num(o_time.split(':')[0]) is False or is_num(
                        o_time.split(':')[1]) is False:
                    o_time = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the departure time (in H:M format): ")

                delay_func = self.bus_company._get_route_info(line_number=int(line_number))
                if o_time not in delay_func._get_scheduled_rides():
                    print(f"\033[0;31;1m No scheduled ride for\033[0;30;0m {o_time}")
                else:
                    delay = input("Insert delay in minutes: ")
                    while is_num(delay) is False:
                        delay = input("\033[0;31;1m Try again \033[0;30;0m Insert delay in minutes: ")
                    delay_func.add_delay(delay)
                    print("\033[0;32;1m Delay has been reported!\033[0;30;0m")

            elif choice == "3":
                break


class Manager(MainMenu):

    def run(self):
        while True:
            print("""
                                              
                                     Welcome manager!
                                
                 Which of the following actions would you'd like to perform?
                           
          Add Route    |   Update Route   |   Add Scheduled route   |   Delete Route 
              ↓        |         ↓        |            ↓            |         ↓
             [1]       |        [2]       |           [3]           |        [4]
                      
                      
                                      ← Main Menu [0]        
            """)
            action = input("Enter your choice: ")
            while action not in ["0", "1", "2", "3", "4"]:
                action = input(" Which of the following action you'd like to perform? ")

            if action == "0":
                break

            if action == "1":
                line_number = input("Insert the line's number: ")
                while is_num(line_number) is False or line_number in self.bus_company._get_bus_rotes() or len(
                        line_number) == 0 or len(line_number) < 0:
                    line_number = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the line's number: ")

                origin = input("Insert the origin: ")
                while is_num(origin) is True or len(origin) == 0:
                    origin = input("\033[0;31;1mTry Again!\033[0;30;0mInsert the origin: ")

                destination = input("Insert the destination: ")
                while is_num(destination) is True or len(destination) == 0:
                    destination = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the destination: ")

                stops_list = []
                amount_of_stops = 0
                while True:
                    stop = input("Insert stops (insert $$$ when finished): ")
                    while is_num(stop) is True or len(stop) < 3:
                        stop = input("\033[0;31;1mTry Again!\033[0;30;0m Insert stops (insert $ when finished): ")
                    amount_of_stops += 1
                    if amount_of_stops <= 1 and stop == "$$$":
                        print("\033[0;31;1m Error zero stops \033[0;30;0m")
                    elif stop == "$$$" and amount_of_stops > 1:
                        break
                    stops_list.append(stop)

                bus_route = BusRoute(int(line_number), origin, destination, stops_list)
                self.bus_company.add_route(bus_route)
                print("\033[0;32;1m Route been added!\033[0;30;0m")


            elif action == "2":
                line_number = input("Insert the line's number: ").strip()
                while is_num(line_number) is False or int(
                        line_number) not in self.bus_company._get_bus_rotes().keys() or len(line_number) == 0:
                    line_number = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the line's number: ").strip()

                route = self.bus_company._get_route_info(int(line_number))
                print(f"current bus route: {route}")

                change = input(
                    "what would you like to change (1 for origin | 2 for destination | 3 for stops | 4 for all): ")
                while change not in ["1", "2", "3", "4"]:
                    change = input(
                        "\033[0;31;1mTry Again!\033[0;30;0m (1 for origin | 2 for destination | 3 for both | 4 for all): ")

                if change == "1":
                    new_origin = input("Insert the new origin: ")
                    while is_num(new_origin) is True or len(new_origin) == 0:
                        new_origin = input("\033[0;31;1mTry Again!\033[0;30;0mInsert the origin: ")
                    self.bus_company.update(line_number=int(line_number), new_origin=new_origin,
                                            update_origin=True, update_destination=False, update_stops=False)
                    print("\033[0;32;1m origin has been updated!\033[0;30;0m")


                elif change == "2":
                    new_destination = input("Insert the new destination: ")
                    while is_num(new_destination) is True or len(new_destination) == 0:
                        new_destination = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the destination: ")
                    self.bus_company.update(line_number=int(line_number), new_destination=new_destination,
                                            update_destination=True,
                                            update_origin=False, update_stops=False)
                    print("\033[0;32;1m destination has been updated!\033[0;30;0m")

                elif change == "3":
                    stops_list = []
                    amount_of_stops = 0
                    while True:
                        stop = input("Insert stops (insert $$$ when finished): ")
                        while is_num(stop) is True or len(stop) < 3:
                            stop = input("\033[0;31;1mTry Again!\033[0;30;0m Insert stops (insert $ when finished): ")
                        amount_of_stops += 1
                        if amount_of_stops <= 1 and stop == "$$$":
                            print("\033[0;31;1m Error zero stops \033[0;30;0m")
                        elif stop == "$$$" and amount_of_stops > 1:
                            break
                        stops_list.append(stop)

                    self.bus_company.update(line_number=int(line_number), new_stops=stops_list,
                                            update_destination=False,
                                            update_origin=False, update_stops=True)
                    print("\033[0;32;1m stops has been updated!\033[0;30;0m")

                else:
                    new_origin = input("Insert the new origin: ")
                    while is_num(new_origin) is True or len(new_origin) == 0:
                        new_origin = input("\033[0;31;1mTry Again!\033[0;30;0mInsert the origin: ")

                    new_destination = input("Insert the destination: ")
                    while is_num(new_destination) is True or len(new_destination) == 0:
                        new_destination = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the destination: ")

                    stops_list = []
                    amount_of_stops = 0
                    while True:
                        stop = input("Insert stops (insert $$$ when finished): ")
                        while is_num(stop) is True or len(stop) < 3:
                            stop = input("\033[0;31;1mTry Again!\033[0;30;0m Insert stops (insert $ when finished): ")
                        amount_of_stops += 1
                        if amount_of_stops <= 1 and stop == "$$$":
                            print("\033[0;31;1m Error zero stops \033[0;30;0m")
                        elif stop == "$$$" and amount_of_stops > 1:
                            break
                        stops_list.append(stop)
                    self.bus_company.update(line_number=int(line_number), new_destination=new_destination,
                                            new_origin=new_origin,
                                            new_stops=stops_list, update_destination=True, update_stops=True,
                                            update_origin=True)
                    print("\033[0;32;1m Route has been updated!\033[0;30;0m")

            elif action == "3":
                line_number = input("Insert the line's number: ").strip()
                while is_num(line_number) is False or int(
                        line_number) not in self.bus_company._get_bus_rotes().keys() or len(line_number) == 0:
                    line_number = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the line's number: ").strip()

                name = input("Insert Driver's full name: ")
                while len(name.split()) != 2 or is_name(name) is False:
                    name = input("\033[0;31;1mTry Again!\033[0;30;0m Insert Driver's name: ")

                o_time = input("Insert the departure time (in H:M format): ")
                while len(o_time) != 5 or is_num(o_time.split(':')[0]) is False or is_num(
                        o_time.split(':')[1]) is False:
                    o_time = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the departure time (in H:M format): ")

                d_time = input("Insert the arrival time (in H:M format): ")
                while len(d_time) != 5 or is_num(d_time.split(':')[0]) is False or is_num(
                        d_time.split(':')[1]) is False or d_time <= o_time:
                    d_time = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the arrival time (in H:M format): ")

                route = self.bus_company._get_route_info(line_number=int(line_number))
                scheduled_ride: ScheduledRide = ScheduledRide(driver_name=name, origin_time=o_time,
                                                              destination_time=d_time, )
                route.add_scheduled_ride(scheduled_ride)
                print("\033[0;32;1mScheduled ride has been added!\033[0;30;0m")

            else:
                line_number = input("Insert the line's number: ").strip()
                while is_num(line_number) is False or int(
                        line_number) not in self.bus_company._get_bus_rotes().keys() or len(line_number) == 0:
                    line_number = input("\033[0;31;1mTry Again!\033[0;30;0m Insert the line's number: ").strip()

                insurence_check = input("Are you sure? (Yes/No): ")
                while insurence_check not in ["yes", "no"]:
                    insurence_check = input("\033[0;31;1mTry Again!\033[0;30;0m A (Yes/No): ")
                if insurence_check == 'no':
                    Passenger(self.bus_company).run()
                else:
                    route = self.bus_company.delete_route(line_number=int(line_number))
                    print("\033[0;32;1mRoute has been deleted!\033[0;30;0m")
