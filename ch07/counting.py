current_number = 1
while(current_number <= 5):
    print(current_number)
    current_number += 1

### 루프에서 continue 문 사용하기 ###
current_number = 0
while(current_number < 10):
    current_number += 1
    if(current_number % 2 == 0):
        continue

    print(current_number)

### 무한 루프 피하기 ###
# Cntrl + C 누르거나 프로그램이 출력되는 터미널 창 닫기