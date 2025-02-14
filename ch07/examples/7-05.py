while(1):
    age = input("How old are you? ")
    age = int(age)
    if(age < 3):
        print("Free")
    elif(age<12):
        print("$10")
    else:
        print("$15")