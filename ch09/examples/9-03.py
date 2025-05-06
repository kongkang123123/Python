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

i = User("Felix", "Kim", 25, "Cooking")
i.describe_user()
i.greet_user()