### 매개변수를 임의의 숫자만큼 전달하기 ###
def make_pizza(*toppings):
    """주문받은 토핑 리스트 출력"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
#  *은 파이썬이 빈 튜플을 만들고 받는 값을 모두 이 튜플에 저장하라는 의미


print("\n\n")

def make_pizza(*toppings):
    """만들려고 하는 피자를 요약한다."""
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

print("\n\n")

### 위치형 매개변수와 임의의 매개변수 함께 쓰기 ###
def make_pizza(size, *toppings):
    """만들려고 하는 피자를 요약합니다."""
    print("\nMaking a " + str(size) + 
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- "+ topping)

make_pizza(16, 'pepperoni')
make_pizza(12, "mushrooms", "green peppers", "extra cheese")