# Lab 13 Unit Converter

print('Convert to Meter(s)')

# VERSION 1
# user = float(input('Enter a distance in feet: '))
# ft_to_m = user * 0.3048

# print(f'{user} ft is {ft_to_m} m')

conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm' : 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

'''
# VERSION 2 & 3
while True: 
    distance = float(input('Enter the distance: '))
    unit = input('Enter the unit (ft, mi, m, km, yd, or in): ').lower()
    valid_choices = 'ft', 'mi', 'm', 'km', 'yd', 'in'

    while unit not in valid_choices:
        unit = input('Invalid choice. Try again: ')

    converted = conversion[unit]

    total = distance * conversion[unit]

    print(f'{distance} {unit} is {total} m')
'''

# VERSION 4

while True: 

    distance = float(input('Enter the distance: '))

    valid_choices = 'ft', 'mi', 'm', 'km', 'yd', 'in'
    input_unit = input('Enter the input unit (ft, mi, m, km, yd, or in): ').lower()

    while input_unit not in valid_choices:
        input_unit = input('Invalid choice. Try again: ')

    output_unit = input('Enter the output unit (ft, mi, m, km, yd, or in): ').lower()

    while output_unit not in valid_choices:
        output_unit = input('Invalid choice. Try again: ')

    converted_input = conversion[input_unit]  
    
    total_input = distance * conversion[input_unit]

    total_output = total_input / conversion[output_unit]

    print(f'{distance} {input_unit} is {total_output} {output_unit}')


    