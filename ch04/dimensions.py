# 튜플
# immutable.
# () 사용한다는 거 제외하면 list와 동일

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 다음과 같이 값 바꾸려 시도하면 에러
# dimensions[0] = 100

# 튜플의 모든 값에 루프 실행하기
print("loops in tuple:")

for dimension in dimensions:
    print(dimension)

# 튜플을 수정할 순 없지만
# 튜플을 가리키던 변수에 새 값을 할당하는 건 가능.
# 즉, 튜플 새로 정의하는 건 가능!
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = [500, 241]
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)