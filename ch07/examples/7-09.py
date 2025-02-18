sandwich_orders = ['pastrami', 'ham', 'pastrami', 'egg', 'bacon', 'pastrami', 'potato']
finished_snadwiches = []

print("The pastrami is out of stock")

while('pastrami' in sandwich_orders):
    sandwich_orders.remove('pastrami')

while(sandwich_orders):
    sandwich = sandwich_orders.pop()
    print("I just made a " + sandwich + " sandwich!")
    finished_snadwiches.append(sandwich)

print(finished_snadwiches)