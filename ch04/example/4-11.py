pizzas = ['bacon pizza', 'pepperoni pizza', 'chicken pizza']

friends_pizzas = pizzas[:]

pizzas.append("corn pizza")
friends_pizzas.append("bulgogi pizza")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My Friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)