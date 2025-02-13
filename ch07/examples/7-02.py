reserved = input("How many guests are coming for dinner?")

if(int(reserved) >= 9):
    print("For parties of 9 or more, you will need to wait until a table is available.")
else:
    print("Your table is ready")