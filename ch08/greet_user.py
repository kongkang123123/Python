def greet_users(names):
    """리스트의 각 사용자에게 단순한 환영 인사를 출력"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'urgot']
greet_users(usernames)