my_foods = ['pizza', 'falafel', 'carrot cake']

# 리스트 복사하려면 다음과 같은 방법 사용
friend_foods = my_foods[:]

# 다음과 같이 추가해주면 달라짐
my_foods.append("cannoli")
friend_foods.append('ice cream')

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)