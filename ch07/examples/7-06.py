active = True

while(active):
    age = input("How old are you? ")

    if(input == 'quit'):
        break

    age = int(age)
    if(age < 3):
        print("Free")
    elif(age<12):
        print("$10")
    elif(age<120):
        print("$15")
    else:
        active = False