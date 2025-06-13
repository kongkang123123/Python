"""자동차를 나타내는 클래스"""
class Car():
    """자동차를 표현하려는 단순한 시도"""

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

class Battery():
    """전기자동차의 배터리를 모델화하려는 단순한 시도"""

    def __init__(self, battery_size = 70):
        """배터리의 속성 초기화"""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리의 크기를 설명하는 문장 출력"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """이 배터리가 제공하는 주행 가능 거리를 출력합니다."""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)

class ElectricCar(Car):
    """전기자동차에만 해당하는 특징을 나타낸다."""
    
    def __init__(self, make, model, year):
        """
        부모 클래스의 속성을 초기화한 다음
        전기자동차에만 해당하는 속성을 초기화합니다.
        """
        super().__init__(make, model, year)    # super() 함수는 부모 클래스와 자식 클래스를 연결하게 함.
        self.battery_size = 70
        self.battery = Battery()        # 속성인 인스턴스

    def fill_gas_tank():    # 파이썬은 부모 클래스의 메서드를 무시하고 자식 클래스에서 정의한 메서드만 사용
        """전기자동차에는 연료 탱크가 없습니다."""
        print("This car doesn't need a gas tank!")

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