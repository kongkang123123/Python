# 리스트 안에 딕셔너리 넣으려면 딕셔너리 요소 먼저 따로 만들고 리스트에 저장.
person1 = {
        'first' : 'choi',
        'last' : 'wonsik',
        'age' : 25,
        'location' : 'yongin',
    }
person2 = {
        'first' : 'park',
        'last' : 'chanhyuk',
        'age' : 25,
        'location' : 'ochang',
    }
person3 = {
        'first' : 'kim',
        'last' : 'suyeong',
        'age' : 25,
        'location' : 'daejeon',
    }
people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(key + ": " + str(value))