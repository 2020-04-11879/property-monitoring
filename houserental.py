from house import House
from rental import Rental


class HouseRental(House, Rental):
    def __init__(self):
        super().__init__()
        Rental.__init__(self)

    def __str__(self):
        return super().__str__() + Rental.__str__(self)

    def set_values_type_payment(self):
        House.set_values_type(self)
        Rental.set_values_payment(self)
