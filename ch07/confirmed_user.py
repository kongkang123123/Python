### 항목을 리스트에서 다른 리스트로 옮기기 ###
# 확인해야 하는 사용자 리스트,
# 확인된 사용자를 저장할 빈 리스트로 시작한다.
unconfirmed_users = ['alice', 'brian', 'Candace']
confirmed_users = []

# 확인되지 않은 사용자가 더는 없을 때까지 각 사용자를 확인
# 확인된 사용자는 확인된 사용자 리스트로 옮김
while(unconfirmed_users):
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 확인된 사용자를 모두 표시
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())