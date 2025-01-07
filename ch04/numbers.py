# range() 함수는 연속된 숫자를 쉽게 생성 가능
# range(시작_숫자, 끝_숫자)
# 끝 숫자는 포함 X

# 5는 출력 X
for value in range(1, 5):
    print(value)

# range()로 숫자 리스트 만들기
# range()함수를 list()함수로 감쌈
numbers = list(range(1,6))
print(numbers)