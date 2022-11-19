class Property:
    def __init__(self):
        self.set_values()

    def set_values(self):
        self.sq_feet = int(input("Square Feet: "))
        self.bedrooms = int(input("Bedrooms: "))
        self.bathrooms = int(input("Bathrooms: "))

    def __str__(self):
        return f"Feet: {self.sq_feet}\tBedrooms: {self.bedrooms}\tBathrooms: {self.bathrooms}\t"
