p1 = {
    'name' : 'dle',
    'breed' : 'toy poodle',
    'owner' : 'minseong' 
    }

p2 = {
    'name' : 'chilhuahua',
    'breed' : 'chihuahua',
    'owner' : 'juyeon' 
    }

p3 = {
    'name' : 'goldaeng',
    'breed' : 'retriever',
    'owner' : 'haha' 
    }

pets = [p1, p2, p3]

for pet in pets:
    for key, value in pet.items():
        print(key + ": " + value)
    print("")