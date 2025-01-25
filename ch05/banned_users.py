# 값이 리스트에 없는지 체크하기
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# CLI에서 코딩 시, 특정 값이 리스트에 이미 존재하는지
# 체크할 때는 키워드 'in' 사용
# e.g.)
# requested_toppings = ['mushrooms', 'onions', 'pineapples']
# 'mushrooms' in requested_toppings
# => True
# 'pepperoni' in requested_toppings
# => False


# 불리언 표현식
# 조건 테스트의 다른 이름
# True / False 값

# && 대신 and
# || 대신 or