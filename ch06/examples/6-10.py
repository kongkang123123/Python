favorite_numbers = {
    'felix' : [8,7],
    'sarah' : [1,4],
    'martin' : [2,1],
    'dewey' : [3,9],
    'ian': [4,7],
    }

print(favorite_numbers)

for name, favorite_number in favorite_numbers.items():
    print(name + ":")
    print(favorite_number)