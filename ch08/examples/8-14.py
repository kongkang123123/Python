def car_info(brand, model, **elements):
    """차의 정보를 저장하는 함수"""
    info = {}
    info['brand'] = brand.title()
    info['model'] = model.title()

    for key, value in elements.items():
        info[key] = value
    return info

car = car_info('subaru', 'outback', color = 'blue', tow_package=True)
print(car)