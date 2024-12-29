### About Number ###
# Python은 제곱 사용 가능 **
# 공백은 파이썬 코드 해석에 아무 영향 X. 그저 우리가 코드를 해석할 때 중요한 부분을 더 빨리 찾아내려는 목적으로 둔 것.
# 만약 0.2 * 0.2 입력하면 0.4000000000001 같은 이상한 값 나옴 (컴구)
# python2에서는 3/2 == 1로 출력됨. C언어와 유사함. 3.0 / 2 이런식으로 사용해야 함.
### -------------------------- ###

age = 24
# 아래와 같이 출력하면 에러(Type Error)
# message = "Happy " + age + "th Birthday!"
# Type Error: 우리가 사용하려는 정보를 잘못 연결했을 때 파이썬이 보내는 신호
# int와 string 연결 X ==> str() 함수 사용해서 해결 가능!
 
message = "Happy " + str(age) + "th Birthday"

print(message)