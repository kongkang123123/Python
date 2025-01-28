current_users = ['felix', 'elynor', 'Sam', 'sara', 'martin']
new_users = ['Felix', 'catarina', 'david', 'sam', 'ishowspeed']

# Convert current_users to lowercase for case-insensitive comparison
# 이 방식 잘 기억해두자
current_users_lower = [user.lower() for user in current_users]

# Check each new user
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")

# 비교 연산자 쓸 때 주위에 공백 하나 쓰는 것이 관행