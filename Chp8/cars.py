def make_car(manufacturer, model_name, **args):
    cars = {}

    cars['manufacturer'] = manufacturer
    cars['model'] = model_name

    for key, val in args.items():
        cars[key] = val
    return cars 
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)