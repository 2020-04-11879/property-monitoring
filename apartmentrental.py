from apartment import Apartment
from rental import Rental


class ApartmentRental(Apartment, Rental):
    def __init__(self):
        super().__init__()
        Rental.__init__(self)

    def __str__(self):
        return super().__str__() + Rental.__str__(self)

    def set_values_type_payment(self):
        Apartment.set_values_type(self)
        Rental.set_values_payment(self)
