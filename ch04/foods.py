my_foods = ['pizza', 'falafel', 'carrot cake']

# 리스트 복사하려면 다음과 같은 방법 사용
friend_foods = my_foods[:]

# 다음과 같이 설정하면 두 변수는 같아짐. 
# 만약 my_foods에 'cannoli'를 추가한다면
# friends_foods에도 추가 됨
# friend_foods = my_foods

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 다음과 같이 추가해주면 달라짐
my_foods.append("cannoli")
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 웬만하면 list 복사할때 slice로 복사하는 것 추천