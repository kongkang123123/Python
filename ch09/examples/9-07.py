class User():
    """사람을 모델링"""

    def __init__(self, first_name, last_name, age, hobby):
        """Attribute 초기화"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby

    def describe_user(self):
        """프로필 소개"""
        print("My name is " + self.first_name.title() + " " + 
              self.last_name.title() + ". And I'm " + str(self.age) + 
              " years old. And my hobby is " + self.hobby + "!")
        
    def greet_user(self):
        """방가인사"""
        print("Welcome, " + self.first_name.title())

class Admin(User):
    """관리자를 나타내는 class"""
    def __init__(self, first_name, last_name, age, hobby):
        """
        부모 클래스의 속성을 초기화한 다음
        admin에만 해당하는 속성을 초기화합니다.
        """
        super().__init__(first_name, last_name, age, hobby)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_previleges(self):
        print("I " + str(self.privileges))

I = Admin("Minseong", "Kim", "23", "Cooking")
I.show_previleges()