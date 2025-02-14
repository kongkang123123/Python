prompt = "\nWould you like to add toppings to your pizza?"
prompt +="\n(Enter 'quit' to exit the program):"

topping =""

while(topping != 'quit'):
    topping = input(prompt)

    if(topping == 'quit'):
        break
    else:
        print(topping.title() + " is a good choice!")