adjective1= input(f'Please input an adjective: ')
adjective2= input(f'Please input an adjective: ')
type_of_bird= input(f'Please input a type of bird: ')
room_in_house= input(f'Please input a room in a house: ')
verb1= input(f'Please input a verb in past tense: ')
verb2= input(f'Please input a verb: ')
name= input(f'Please input a name: ')
noun1= input(f'Please input a noun: ')
liquid= input(f'Please input a type of liquid: ')
verb3 = input(f'Please input verb ending in -ing: ')
body_part= input(f'Please input a part of the body(plural): ')
noun2= input(f'Please input a plural noun: ')
verb4= input(f'Please input a verb ending in -ing: ')
noun3= input(f'Please input a noun: ')

print('Mad Lib \nThanksgiving Day \n----------------')


output = f'''
It was a {adjective1}, cold November day. 
I woke up to the {adjective2} smell of {type_of_bird} roasting in the {room_in_house} downstairs.
I {verb1} down the stairs to see if I could help {verb2} the dinner.
My mom said, "See if {name} needs a fresh {noun1}."
So I carried a tray of glasses full of {liquid} into the {verb3} room. 
When I got there, I couldn't believe my {body_part}! 
There were {noun2} {verb4} on the {noun3}!'''

print(output)