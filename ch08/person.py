### 딕셔너리 반환하기 ###
# 함수는 어떤 타입의 값이라도 반환할 수 있다.
def build_person(first_name, last_name, age=''):
    """사람에 관한 정보 딕셔너리를 반환"""
    person = {'first' : first_name, 'last': last_name}
    if(age):
        person['age'] = age     # 딕셔너리 구조 파악하자! 이런 방법이 있다.
    return person

musician = build_person('jimi', 'hendrix', age='25')
print(musician)