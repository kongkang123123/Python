# String 사용 시 큰 따옴표, 작은 따옴표 모두 가능
# method: 파이썬이 데이터 취하는 행동. 종종 정보 필요해서 괄호 한쌍 같이 씀
# 다음은 대소문자 바꾸는 예제
name = "ada lovelace"
print(name.title())

name = "Kim Minseong"
print(name.upper())
print(name.lower())

first_name = "felix"
last_name = "kim"

print(first_name + " " + last_name)

full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

# <tab> 추가
print("\tPython")

# 개행 추가
print("Languages:\n\tPython\n\tC\n\tJavaScript\n\n")

# 문자열의 오른쪽 공백제거. rstrip()
favorite_language = 'Python    '
print(favorite_language.rstrip())

# 문자열의 왼쪽 공백제거. lstrip()
favorite_language = '     Python'
print(favorite_language.lstrip())

# 문자열의 모든 공백제거. 중간중간 띄어쓰기는 안되고 양옆에 공백만 없애는듯. \t도 안되네. strip()
favorite_language = '   pyt   hon fsa\tdfsdaf'
print(favorite_language.strip())