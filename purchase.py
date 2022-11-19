from functions import get_valid_input


class Purchase:

    def __init__(self):
        self.set_values_payment()

    def set_values_payment(self):
        self.price = int(input("Price: "))
        self.taxes = int(input('Taxes: '))

    def __str__(self):
        return f"Price: {self.price}\tTaxes: {self.taxes}\t"
