# from car import Car, ElectricCar

# my_beatle = Car('volkswagen', 'beetle', 2016)
# print(my_beatle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


# 전체 모듈 import하기
import car

my_beatle = car.Car('volkswagen', 'beetle', 2016)
print(my_beatle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())