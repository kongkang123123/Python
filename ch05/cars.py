# 자동차는 대부분 고유명사이므로 앞글자 대문자
# bmw같은거는 모든 글자를 대문자
cars = ['audi', 'bmw', 'subaru', 'toyota']

cars = ['audi', 'bmw', 'subaru', 'toyota']

# if '조건':
# else:
# 이런 형태임

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 대소문자 구분없이 하려면 .lower() 키워드 이용하기
# 조건 테스트가 True로 평가되면 if문 다음의 코드 실행
# 조건 테스트가 False로 평가되면 if문 다음에 있는 코드 무시

## 일치하는지 체크할 때 대소문자 무시하기
# car = 'Audi'
# car == 'audi'
# False

# 대소문자 중요하지 않다면 다음과 같이 설정 가능
# car = 'Audi'
# car.lower() == 'audi'
# False
# lower()는 저장된 값 안 바꿈 => 변수에 어떤 영향도 안 줌