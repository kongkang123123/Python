class Restaurant():
    """레스토랑을 클래스화"""

    def __init__(self, restaurant_name, cuisine_type):
        """attribute 초기화"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """레스토랑 소개"""
        print("The name is " + self.restaurant_name.title() + " . And today's cuisine is " + self.cuisine_type)

    def open_restaurant(self):
        """오픈 소식 전달"""
        print("Today, " + self.restaurant_name.title() + " is opend. And numer of served in " + str(self.number_served))

    def set_number_served(self, number):
        """서빙한 고객 숫자를 지정"""
        self.number_served = number

    def increment_number_served(self, number):
        """고객 수 늘림"""
        self.number_served += number

my_restaurant = Restaurant("Montblanc", "Pork")
my_restaurant.set_number_served(15)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.increment_number_served(10)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()