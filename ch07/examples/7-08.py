sandwich_orders = ['ham', 'egg', 'bacon', 'potato']
finished_snadwiches = []

while(sandwich_orders):
    sandwich = sandwich_orders.pop()
    print("I just made a " + sandwich + " sandwich!")
    finished_snadwiches.append(sandwich)

print(finished_snadwiches)