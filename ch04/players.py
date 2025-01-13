# slice: 리스트의 특정한 항목 그룹
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# range() 함수와 마찬가지로 두번째 인덱스 바로 앞의 항목에서 멈춤: 0 ~ 2 인덱스
print(players[1:3])

# 첫번째 인덱스부터 시작한다면 앞 인덱스 생략 가능
print(players[:4])

# n번째 항목부터 마지막 항목까지 슬라이스 만들고 싶다면
# list[n:] 이런식으로 두번째 인덱스 체크
print(players[2:])

# 인덱스의 마지막부터 원하는 만큼 꺼낼 수도 있음
# 다음 예제는 마지막 세 명이 포함된 슬라이스 출력
print(players[-3:])


##### slice에 loop 실행 #####
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())