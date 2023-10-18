# Version 1
feet = input('What is the distance in feet: ')
feet = float(feet)

# Dictionary to convert feet to meters
conversion_factors = {
    'ft': 0.3048,
    'm': 1.0  # Added 'm' for meters
}

unit_type = input('Please enter unit type (ft/m): ')
unit_type = unit_type.lower()  # Convert input to lowercase for case insensitivity

if unit_type in conversion_factors:
    meters = feet * conversion_factors[unit_type]
    print(f'{feet} {unit_type} is {round(meters, 4)} meters')
else:
    print('Invalid unit type. Please enter "ft" or "m".')

# Version 2
unit_type = input('Please enter unit type (ft/mi/m/km): ')
unit_type = unit_type.lower()

distance = input('Please enter distance: ')
distance = float(distance)

conversion_factors = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1.0,
    'km': 1000
}

if unit_type in conversion_factors:
    converted_distance = distance * conversion_factors[unit_type]
    print(f'{distance} {unit_type} is {round(converted_distance, 4)} m')
else:
    print('Invalid unit type. Please enter "ft", "mi", "m", or "km".')

# Version 3
new_items = {
    'yd': 0.9144,
    'in': 0.0254
}

conversion_factors.update(new_items)

unit_type = input('Please enter unit type (ft/mi/m/km/yd/in): ')
unit_type = unit_type.lower()

distance = input('Please enter distance: ')
distance = float(distance)

if unit_type in conversion_factors:
    converted_distance = distance * conversion_factors[unit_type]
    print(f'{distance} {unit_type} is {round(converted_distance, 4)} m')
else:
    print('Invalid unit type. Please enter "ft", "mi", "m", "km", "yd", or "in".')
