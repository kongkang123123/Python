### 키-값 쌍 전체에 루프 실행하기 ###
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
    }


# 각 키-값 쌍의 키와 값을 저장할 변수 이름 정함 (꼭 key, value일 필요 없음)
for key, value in user_0.items():   # items() 메서드는 키-값 상 리시트를 반환
    print("\nkey: " + key)
    print("value: " + value)
# 루프에서 키-값 쌍이 반환되는 순서는 딕셔너리에 저장된 순서와 다름
# 그냥 각 키와 값이 연결된 것만 중시함