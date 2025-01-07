squares = []
for value in range(1, 11):
    # square = value**2
    # squares.append(square)
    squares.append(value ** 2)

print(squares)

# list comprehension (리스트 내포)
# 단 한줄의 코드로 요소 복잡한 코드 만들 수 있음
# for루프와 새 항목 생성을 한 행에 결합 => 각 새 항목을 자동으로 리스트에 추가
# for문 마지막에 콜론 없음
squares_2 = [value**2 for value in range(1, 11)]
print(squares_2)

#### 숫자 리스트를 이용한 단순한 통계 ####
# min('숫자리스트이름') : 최솟값 출력
# max('숫자리스트이름') : 최댓값 출력
# sum('숫자리스트이름') : 합계 출력