def city_country(city, country):
    city_and_country = {'city' : city.title(), 'country' : country.title()}
    return city_and_country

print(city_country('santiago', 'chile'))
print(city_country('seoul', 'south korea'))
print(city_country('pyeonyang', 'north korea'))