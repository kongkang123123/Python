def make_sandwich(*toppings):
    """재료 리스트 받아서 샌드위치 제작하는 함수"""
    for topping in toppings:
        print("- " + topping)

make_sandwich('bacon', 'garlic')
make_sandwich('olive', 'cheese')
make_sandwich('lettuce', 'pork')