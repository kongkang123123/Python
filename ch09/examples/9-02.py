class Restaurant():
    """레스토랑을 클래스화"""

    def __init__(self, restaurant_name, cuisine_type):
        """attribute 초기화"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """레스토랑 소개"""
        print("The name is " + self.restaurant_name.title() + " . And today's cuisine is " + self.cuisine_type)

    def open_restaurant(self):
        """오픈 소식 전달"""
        print("Today, " + self.restaurant_name.title() + " is opend.")

my_restaurant = Restaurant("Montblanc", "Pork")
your_restaurant = Restaurant("Gentle", "Beef")
her_restaurant = Restaurant("Mosu", "Lamb")

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
her_restaurant.describe_restaurant()