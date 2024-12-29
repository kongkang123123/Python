# 리스트에는 보통 2개 이상의 항목 존재
# 그래서 리스트 이름을 bicycles, names 같이 복수형으로 지정
# print하면 리스트 표현 출력
# 그리고 자료형 맞추기 잊지말자! str()같은 함수 사용.
 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("\n" + str(bicycles))

# 밑에처럼 문자열 메서드 사용가능
print(bicycles[0].title())
print(bicycles[0].upper())

print(bicycles[1].title())
print(bicycles[3].upper())

# 그리고 파이썬에는 -1로 리스트의 마지막 항목 반환.
# 리스트의 길이 모를때 유용함.
print(bicycles[-1])

# 뒤에서 두번째 요소는 -2, 세번째 요소는 -3으로 접근
print(bicycles[-2]) 
print(bicycles[-3]) 

# ch02와 마찬가지로 다른 변수와 같이 쓸 수 있음.
message = "My furst bicycle was a " + bicycles[0].title() + "."
print(message)


## 여기서 문제 함수와 메서드의 차이점
# 함수: 독립적으로 정의되므로 이름만으로만 호출 가능. 함수가 메서드보다 더 포괄적인 의미
# 메서드: 정의된 클래스의 참조에 의해 클래스 호출해야만 함. 클래스 내에서 정의되므로 해당 클래스에 종속됨

# 그리고 인덱스 0부터 시작하는 이유: 컴퓨터의 메모리가 0부터 시작하기 때문