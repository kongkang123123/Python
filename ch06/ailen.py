# 딕셔너리: 키-쌍의 모음
# '딕셔너리 이름' = {'키' : '값', ...}
# list와 달리 {}로 묶음
# 값: 숫자, 문자열, 리스트, 다른 딕셔너리 등도 가능능
alien_0 = {'color': 'green', 'points': 5}

### 딕셔너리 값에 접근하기 ###
# '딕셔너리명'['키']
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!\n\n")

### 새 키-값 쌍 추가하기 ###
# 딕셔너리는 동적 구조
# 추가할 때 꼭 저장한 순서대로 안됨
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

### 빈 딕셔너리로 시작하기 ###
# 우선 딕셔너리 정의 시작
alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 5

print(alien_1)
print("\n")
### 딕셔너리 값 수정하기 ###
print("The alien is " + alien_1['color'] + ".")

alien_1['color'] = 'blue'
print("The alien is now " + alien_1['color'] + ".")
print("\n\n")

# 외계인 추적 예제제
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# 외계인을 오른쪽으로 움직인다.
# 현재 속도를 기준으로 외계인이 얼마나 빨리 움직이는지 판단한다.
if(alien_0['speed'] == 'slow'):
    x_increment = 1
elif(alien_0['speed'] == 'medium'):
    x_increment = 2
else:
    x_increment = 3

# 새 위치는 이전 위치에 증가분을 더한 값
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))
print("\n")


### 키-값 쌍 제거하기 ###
# 제거하고 나면 복구 불가
# del '딕셔너리명'['키']
print(alien_0)

del alien_0['speed']

print(alien_0)