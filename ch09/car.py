class Car():
    """자동차를 나타내는 코드"""

    def __init__(self, make, model, year):
        """자동차를 나타내는 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        # 기본값은 속성에 정해둠. 
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """알아보기 쉬운 이름 반환"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """주행거리를 나타내는 문장을 출력합니다."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):  # 메서드를 통해 속성값 바꾸기기
        """
        주행거리 표시기를 주어진 값으로 바꿉니다.
        주행거리 표시기를 더 작은 값으로 바꾸려 하면 거부합니다.
        """
        if (mileage>=self.odometer_reading):
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """주행거리를 주어진 양만큼 늘립니다."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(25)
my_new_car.read_odometer()

my_new_car.update_odometer(2)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()