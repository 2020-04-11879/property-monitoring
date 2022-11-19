from house import House
from purchase import Purchase

class HousePurchase(House,Purchase):
    def __init__(self):
        super().__init__()
        Purchase.__init__(self)

    def __str__(self):
        return super().__str__() + Purchase.__str__(self)

    def set_values_type_payment(self):
        House.set_values_type(self)
        Purchase.set_values_payment(self)