# 자동차는 대부분 고유명사이므로 앞글자 대문자
# bmw같은거는 모든 글자를 대문자
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 대소문자 구분없이 하려면 .lower() 키워드 이용하기