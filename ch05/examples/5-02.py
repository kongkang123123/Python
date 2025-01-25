dog = 'Poodle'

print(dog.lower() == 'poodle')
print(dog != 'poodle')
print(dog == 'corgi')

print(dog == "Poodle")
print(dog.title() == "Poodle")

height_0 = 160
height_1 = 180

print(height_0 == height_1)
print(height_0 >= height_1)
print(height_0 > height_1)
print(height_0 < height_1)
print(height_0 <= height_1)

print(height_1 == 180 and dog == 'Poodle')
print(height_0 > 190 or dog == 'corgi')

dogs = ['corgi', 'poodle', 'jindo']
print(dog.lower() in dogs)

if not dog in dogs:
    print("hi")