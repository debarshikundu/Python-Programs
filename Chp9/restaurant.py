class Restaurant:
    """Simulates a real-world restaurant..."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    """Restaurant name + Cuisine Type..."""
    def describe_restaurant(self):
        return self.restaurant_name + " " + self.cuisine_type
    
    def open_restaurant(self):
        print("Restaurant is open!!!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []
    def displayFlavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.displayFlavors()