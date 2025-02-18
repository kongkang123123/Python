vacation_place = {}
print("If you could visit one place in the world where would you go?\n")

polling_active = True

while(polling_active):
    name = input("name: ")
    place = input("Place: ")

    vacation_place[name] = place

    repeat = input("Would you like to let another person respond? (y/n)")

    if(repeat == 'n'):
        polling_active = False


print("--- poll results ---")
for name, responses in vacation_place.items():
    print(name +  ": " + responses)