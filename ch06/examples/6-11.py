cities = {
    'seoul': {
        'country': 'south korea',
        'population' : '9.4m',
        'fact' : 'the han river',
    },
    'newyork': {
        'country': 'usa',
        'population' : '8.2m',
        'fact' : 'the hudson river',
    },
    'paris': {
        'country': 'france',
        'population' : '21m',
        'fact' : 'the seine river',
    },
    }

for city, facts in cities.items():
    print(city)
    for key, value in facts.items():
        print(key + ": " + value)