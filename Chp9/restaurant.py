class Restaurant:
    """Simulates a real-world restaurant..."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    """Restaurant name + Cuisine Type..."""
    def describe_restaurant(self):
        return self.restaurant_name + " " + self.cuisine_type
    
    def open_restaurant(self):
        print("Restaurant is open!!!")

restaurant1 = Restaurant("PTerry's", "Fast Food")

restaurant2 = Restaurant("Shake Shack", "Fast Casual Food")

restaurant3 = Restaurant("Haagen Dazs", "Ice Cream")

print(restaurant1.describe_restaurant())

print(restaurant2.describe_restaurant())

print(restaurant3.describe_restaurant())
