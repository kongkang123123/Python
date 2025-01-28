# amusement_park: 놀이공원
# amusement: 즐거움
# if-elif-else 중 하나만 실행

age = 12

if(age < 4):
    price = 0
elif(age < 18):
    price = 5
elif(age<65):
    price = 10
else:
    price = 5
# elif(age>=65):    # else 생략하는 방법
#   price = 5  
# else 블록은 무조건 실행하므로 악의적인 데이터도 체크하지 않고
# 받아들일 가능성 있음

print("Your admission cost is $" + str(price) + ".")