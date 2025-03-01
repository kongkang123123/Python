def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
    profile = {}
    profile['first_name'] = first 
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)

# 매개변수 앞의 애스터리스크 두 개는 파이썬이 빈 딕셔너리를 만들고 키-값 쌍을 모두 이 딕셔너리에 저장하게 한다
# 함수 안에서는 다른 딕셔너리와 마찬가지로 user_info의 키-값 쌍에 접근할 수 있다.