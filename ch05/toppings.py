## 불일치 체크하기 ##
# != 사용
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("\n")

# 여러 조건 테스트하기
# if-elif-else와 달리 건너뛰기 안함
requested_toppings = ['mushrooms', 'extra cheese']

if ('mushrooms' in requested_toppings):
    print("Adding mushrooms.")
if ('pepperoni' in requested_toppings):
    print("Adding pepperoni.")
if ('extra cheese' in requested_toppings):
    print("Adding extra cheese")

print("\nFinished making your pizza!\n")

# 리스트에서 if 문 사용하기
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

for requested_topping in requested_toppings:
    if(requested_topping == 'green peppers'):
          print("Sorry, we are out of green peppers right now") 
    else:
        print("Adding " + requested_topping + ".")

print("\nFinishing making your pizza!\n\n")

# 리스트가 비어 있지 않은지 확인하기
# 리스트에 항목 하나 이상 있을 때 True 반환
requested_toppings = []

if (requested_toppings):    # 리스트 비어있는지 확인하려면 그냥 리스트명만 쓰면 됨됨
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\n\n")

# 여러 리스트 다루기
available_toppings = ['mushroom', 'olives', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushroom', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if (requested_topping in available_toppings):
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza")