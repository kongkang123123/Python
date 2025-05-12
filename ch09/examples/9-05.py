class User():
    """사람을 모델링"""

    def __init__(self, first_name, last_name, age, hobby):
        """Attribute 초기화"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        """프로필 소개"""
        print("My name is " + self.first_name.title() + " " + 
              self.last_name.title() + ". And I'm " + str(self.age) + 
              " years old. And my hobby is " + self.hobby + "!")
        
    def greet_user(self):
        """방가인사"""
        print("Welcome, " + self.first_name.title())
        print("I login in " + str(self.login_attempts) + " times.")

    def increment_login_attempts(self):
        """로그인 횟수 1씩 늘림"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """로그인 횟수 0으로 리셋"""
        self.login_attempts = 0

i = User("Felix", "Kim", 25, "Cooking")

i.increment_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()
i.increment_login_attempts()

i.describe_user()
i.greet_user()

i.reset_login_attempts()

i.describe_user()
i.greet_user()
