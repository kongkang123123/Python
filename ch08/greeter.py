def greet_user(username):       # 함수 이름 그리고 필요에 따라 어떤 정보 필요한지 알림 => 함수 정의
    """간단한 환영 인사를 표시합니다."""    # document string 또는 docstring: 함수 역할 설명하는 주석. 꼭 쓰는거 추천
    print("Hello!" + username.title() + "!")

greet_user('Felix')