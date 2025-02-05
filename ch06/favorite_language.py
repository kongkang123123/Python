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

### 딕셔너리 키에 순서대로 루프 실행하기 ###
# 보통은 순서 신경 안쓰고 딕셔너리에 저장
# sorted() 함수 사용!
for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for taking the poll.")
# favorite_languages.key()를 sorted() 메서드로 감쌌다는거 빼면 다른 for문이랑 동일
print("\n")

### 딕셔너리의 모든 '값'에 루프 실행하기 ###
print("The following languages have been metnioned:")
for language in favorite_languages.values():
    print(language.title())

# 중복 값 없이 출력하려면 set 사용
print("The following languages have been metnioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print("\n")
### 딕셔너리 안에 리스트 넣기 ###
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    }

# item() 메서드 사용하면 key와 value 쌍 얻을 수 있음
for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())