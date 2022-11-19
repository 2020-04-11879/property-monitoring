from property import Property
from functions import get_valid_input


class House(Property):
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self):
        super().__init__()
        stories = input("Stories: ")
        self.stories = stories
        self.garage = get_valid_input("Garage ", (House.valid_garage))
        self.fenced = get_valid_input("Fenced ", (House.valid_fenced))

    def set_values_type(self):
        super().set_values()
        stories = input("Stories: ")
        self.stories = stories
        self.garage = get_valid_input("Garage ", (House.valid_garage))
        self.fenced = get_valid_input("Fenced ", (House.valid_fenced))



    def __str__(self):
        return super().__str__() + f"Garage: {self.garage}\tFenced: {self.fenced}\tStories: {self.stories}\t"
