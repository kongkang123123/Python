# 여러 요소 필요할 경우, 들여쓰기하며 띄우기
# 마지막 }은 키-값 쌍과 같은 수준으로 들여 써서 딕셔너리 키 들과 정렬되게 하기.
# 마지막 키-값 쌍 다음에 쉼표 남겨 두는 건 다음 행에 추가하기 좋음 => 관행처럼 쓰기

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

# 다음과 같은 스타일 쓸 때, 마지막행에 ) 남겨두기
print("'sarah's favorite language is " + 
      favorite_languages['sarah'].title() +
      ".")