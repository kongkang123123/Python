### 위치형 매개변수 ###
# 매개변수가 제공된 순서대로 맞추는 방법
def describe_pet(animal_type, pet_name):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("Toy poodle", "dle") # 종과 이름을 순서대로 입력
describe_pet("Cat", "ddalgi")
# 해당 방법 사용시 순서에 유념하자

### 키워드 매개변수 ###
# 함수에 넘기는 키-값 쌍. 순서 틀려도 상관 없고 각 값의 역할 명시적으로 드러남
describe_pet(animal_type='Toy poodle', pet_name='dle')
describe_pet(pet_name='dle',animal_type='Toy poodle')

### 기본값 ###
# 함수 만들 때 각 매개변수의 기본값 정할 수 있음. 매개변수 없을 때 기본값 씀
# 함수 정의 시, 기본값 있는 매개변수는 기본값 없는 매개변수 뒤에 배치해야 함.
def describe_pet(animal_type, pet_name = 'dle'):
    """애완동물에 관한 정보를 출력합니다."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='retriever')
describe_pet(animal_type='dog', pet_name='hi') # 기본값 안 쓰려면 이렇게 매개변수 지정해주면 됨

describe_pet('hamster', 'gangster') # 이런식으로 매개변수 지정해줘도 됨
