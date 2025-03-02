def build_profile(first, last, **user_info):
    """사용자에 관해 아는 것을 모두 딕셔너리로 만듭니다."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

user_profile = build_profile('felix', 'kim',
                             middle_name = 'minseong',
                             location = 'cheongju',
                             field = 'computer sceince')
print(user_profile)