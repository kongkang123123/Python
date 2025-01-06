magicians = ['alice', 'david', 'carolina']
### 들여쓰기 안하면 오류 발생 ###
# for magician in magicians:
# print(magician)

### 추가 행을 들여쓰지 않았을 때 ###
# logical error(논리적 오류)
for magician in magicians:
    print(magician.title() + ", that was a great trick!") 
print("I can't wait to see your next trick, " + magician.title() + ".\n")   # 마지막 요소인 carolina만 출력

### 불필요한 들여쓰기를 했을 때 ###
# massage = "Hello, Python!"
#     print(message)
# 들여쓰기 해야할 때만 사용

### 루프 다음에 불필요한 들여쓰기를 했을 때 ###
# 원래는 "Thank you~~ "마지막에 한번만 출력하길 바람. 이 또한 logical error
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, " + magician.title() + ".\n")

#     print("Thank you everyone, that was a great magic show!")

### 콜론을 잊었을 때 ###
# 콜론을 통해 for문 인식
# 콜론 잊을 경우 파이썬은 우리의 의도를 해석 못해 syntax error 일으킴
# for magician in magicians
#     print(magician)