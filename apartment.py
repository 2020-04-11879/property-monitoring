from property import Property
from functions import get_valid_input


class Apartment(Property):
    valid_laudries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'solarium')

    def __init__(self):
        super().__init__()
        self.laundries = get_valid_input("Laundries ", (Apartment.valid_laudries))
        self.balconies = get_valid_input("Balconies", (Apartment.valid_balconies))

    def set_values_type(self):
        super().set_values()
        self.laundries = get_valid_input("Laundries ", (Apartment.valid_laudries))
        self.balconies = get_valid_input("Balconies", (Apartment.valid_balconies))

    def __str__(self):
        return super().__str__() + f"Laundries: {self.laundries}\tBalconies: {self.balconies}\t"
