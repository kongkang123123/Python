# sort()로 리스트 영구 정렬   -   실제 리스트 순서 바뀜
print("sort() 사용")
cars = ['bmw', 'audi', 'toyota', 'subaru']  # 알파벳 순으로 정렬
cars.sort()     # 리스트이름.sort()
print(cars)
print("\n\n")

#  알파벳 반대 순서로 정렬
print("알파벳 반대순서로 sorting()")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
# cars.sort(reverse = 1)     # True 대신 1 넣어도 됨.
print(cars)
print("\n\n")

# sorted()로 리스트 임시 정렬    -  실제 리스트 순서 안 바뀜
print("sorted()로 임시 정렬")
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here iis the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))     # sort()와 달리 sorted()함수에 리스트를 집어 넣음.    sorted('리스트이름')

print("\nHere is the sorted list reverse ver: ")
print(sorted(cars, reverse=1))     # reverse=True 매개변수 추가하면 반대 순서로 표시

print("\nHere is the origin list again :")
print(cars)
print("\n\n")

# 리스트를 반대 순서로 출력   -  알파벳 순서 고려 안하고 현재 순서의 반대로만 정렬
print("sorted()로 임시 정렬")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()          # 리스트이름.reverse()    리스트순서 영구히 바꿈. reverse() 한번 더 적용하면 원래 순서로 돌아감
print(cars)

# 리스트 길이 구하기
print(len(cars))            # len('리스트이름삽입')