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

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
# 기본적으로 딕셔너리에 루프 실행하면 키에만 적용

## 내 친구일때만 출력되게 하기
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if (name in friends):
        print(" Hi " + name.title() + ". I see your favorite language is " +
              favorite_languages[name].title() + "!")
        
if ('erin' not in favorite_languages.keys()):   # keys()나 values() 메서드로 값 접근 가능
    print('Erin please take our poll')