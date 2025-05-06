class Dog():    # 클래스 정의. 대부분 class 명 앞글자를 대문자로 씀
    """개를 모델화하는 시도"""  # 해당 클래스를 설명하는 독스트링

    # 클래스에 속한 함수를 method라고 부름
    def __init__(self, name, age):  # 특별한 메서드. Dog클래스에서 새 인스턴스를 만들때마다 자동으로 실행. self 필수. 무조건 앞에 넣어주기
        """name과 age속성 초기화"""
        # self가 붙은 변수는 클래스의 모든 메서드에서 접근 가능. 이 클래스에서 만든 모든 인스턴스에서도 접근 가능
        self.name = name
        self.age = age

    def sit(self):
        """명령에 따라 앉는 개"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """명령에 따라 구르는 개"""
        print(self.name.title() + " rolled over!")



my_dog = Dog("Dle", 14)

print("My dog' name is " + my_dog.name.title() + ".")
print("My dog' age is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()