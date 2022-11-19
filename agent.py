from houserental import HouseRental
from housepurchase import HousePurchase
from apartmentrental import ApartmentRental
from apartmentpurchase import ApartmentPurchase
from functions import get_valid_input


class Agent:
    class_dict = {('house', 'rental'): HouseRental, ('house', 'purchase'): HousePurchase,
                  ('apartment', 'rental'): ApartmentRental, ('apartment', 'purchase'): ApartmentPurchase}

    def __init__(self):
        self.property_list = []

    def add_property(self):
        property_type = get_valid_input('What type of property? ', ('house', 'apartment')).lower()
        payment_type = get_valid_input('What payment type? ', ('purchase', 'rental')).lower()
        item = None
        if property_type == 'house' and payment_type == 'purchase':
            item = HousePurchase()
        elif property_type == 'house' and payment_type == 'rental':
            item = HouseRental()
        if property_type == 'apartment' and payment_type == 'purchase':
            item = ApartmentPurchase()
        elif property_type == 'apartment' and payment_type == 'rental':
            item = ApartmentRental()
        self.property_list.append(item)

    def show_all_properties(self):
        count = 1
        for i in self.property_list:
            print(f'{count}) ', end='')
            if type(i) == HousePurchase:
                print('HousePurchase:', i)
            elif type(i) == HouseRental:
                print('HouseRental:', i)
            elif type(i) == ApartmentPurchase:
                print('ApartmentPurchase:', i)
            else:
                print('ApartmentRental:', i)
            count += 1
        if count == 1:
            print("No property has been added yet!")

    def show_match_property(self):
        property_type = get_valid_input("Property Type: ", ('house', 'apartment'))
        payment_type = get_valid_input("Payment Type: ", ('purchase', 'rental'))
        obj_property_class = Agent.class_dict[(property_type, payment_type)]
        count = 1
        for i in self.property_list:
            if type(i) == obj_property_class:
                print(f"{count}) {i}")
                count += 1
        if count == 1:
            print("No specified property is available.")

    def modify_property(self):
        property_no = int(input("Property No: "))
        if 1 > property_no or property_no > len(self.property_list):
            print("Invalid property number")
        else:
            self.property_list[property_no-1].set_values_type_payment()


if __name__ == "__main__":
    pass
    # a1 = Agent()
    # a1.add_property()
    # a1.add_property()
    # if type(a1.property_list[0]) == HousePurchase:
    #     print('Yes boy! its working')
