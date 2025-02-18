### 사용자가 입력한 값으로 딕셔너리 채우기 ###
responses = {}

# 설문이 활성화됐다는 플래그를 설정
polling_active = True

while(polling_active):
    # 이름과 응답을 묻는다
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 응답을 딕셔너리에 저장
    responses[name] = response

    # 다른 사람도 설문에 참여할지 물음
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if(repeat == 'no'):
        polling_active = False

# 설문이 끝났습니다. 결과를 출력합니다
print("\n--- Polls Results ---")
for name, response in responses.items():
    print(name + " Would like to climb " + response + ".")