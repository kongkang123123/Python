# 리스트는 '동적' - 리스트를 만든 뒤 항목 추가 / 제거 / 변경 가능

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 변경
motorcycles[0] = 'ducati'
print(motorcycles)

# append()로 리스트 끝에 항목 추가
motorcycles.append("honda")  # 리스트이름.append('값')
print(motorcycles)

# 빈 리스트에서 시작해 요소 추가
dogs = []

print(dogs)

dogs.append('poodle')
dogs.append('retriever')
dogs.append('shepherd')

print(dogs)

# insert()로 리스트 항목 중간 삽입
dogs.insert(1, "samoyed")   # 리스트이름.insert(인덱스, '값')

print(dogs)

# del 문으로 항목 제거
del motorcycles[1]  # del 리스트이름[제거할 항목의 인덱스]
print(motorcycles)

# pop()으로 항목 제거. 리스트에서 빼낸 항목의 값이 필요할 때. 리스트의 마지막 항목을 빼내서 사용(Stack)
last_owned = motorcycles.pop(0)  # 또한 pop() 통해 접근하고 싶은 인덱스 정할 수 있음
print(motorcycles)
print(last_owned)

print("The last motorcycle I owned was a " + last_owned.title() + ".")

favorite_owned = motorcycles.pop()

print(motorcycles)
print("The favorite motorcycle I owned is a " + favorite_owned + ".")


motorcycles = ['honda', 'yamaha', 'suzuki']

# 값으로 항목 제거하기. remove() 메서드 사용
print(motorcycles)
motorcycles.remove("honda")

print(motorcycles)

# remove() 메서드도 제거할 값을 변수에 저장했다가 인덱스로 사용 가능

too_expensive = "yamaha"
motorcycles.remove(too_expensive)

print(motorcycles)
print("\n" + too_expensive.title() + " is too expensive for me.")

# too_expensive = motorcycles.remove("yamaha")   # pop()처럼 사용하는 건 불가능한듯.

# remove() 통해 없는 값 지우려고 하면 error
# motorcycles.remove("hyundai")

# 만약 리스트에 같은 값이 여러 개 있다면 remove() 메서드는 첫 번째 항목만 제거. 값 전부 제거하고 싶다면 루프 사용해야 함. (ch07에서 배움)