from agent import *
from functions import *


def main():
    agent = Agent()
    print("<--------- Property Management System --------->")
    while True:

        print_menu()
        choice = get_valid_no("Enter Your Choice: ", 1, 5)
        if int(choice) == 1:
            agent.add_property()
        elif int(choice) == 2:
            agent.show_match_property()
        elif int(choice) == 3:
            agent.show_all_properties()
        elif int(choice) == 4:
            agent.modify_property()
        else:
            print('Thanks, for using the system')
            break


main()
