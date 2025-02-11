favorite_places = {
        'minseong' : [
            'eumseng-cheon',
            'yeosu',
            'haengbok-damgil',
            ],
        'wonsik' : [
            'hi',
            'hello',
            'oh',
        ],
        'suyeong' : [
            'good',
            'bye',
            'there'
        ],
    }

for name, favorite_place in favorite_places.items():
    print(name + ": ")
    for place in favorite_place:
        print(place)