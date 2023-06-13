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

restaurant = Restaurant("PTerry's", "Fast Food")

print(restaurant.restaurant_name +" "+ restaurant.cuisine_type)

print(restaurant.describe_restaurant())

restaurant.open_restaurant()


