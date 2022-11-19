from functions import get_valid_input


class Rental:
    valid_furnished = ('yes', 'no')
    valid_utilities = ('yes', 'no')

    def __init__(self):
        self.set_values_payment()

    def set_values_payment(self):
        rent = int(input('Rent: '))
        self.furnished = get_valid_input("Furnished ", (Rental.valid_furnished))
        self.utilities = get_valid_input("Utilities ", (Rental.valid_utilities))
        self.rent = rent

    def __str__(self):
        return f"Rent: {self.rent}\tFurnished: {self.furnished}\tUtilities: {self.utilities}\t"
