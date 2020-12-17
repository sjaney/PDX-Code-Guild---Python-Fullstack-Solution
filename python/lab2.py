adjective1= input('Please input an adjective: ')
adjective2= input('Please input another adjective: ')
type_of_bird= input('Please input a type of bird: ')
room_in_house= input('Please input a room in a house: ')
verb1= input('Please input a verb in past tense: ')
verb2= input('Please input a verb: ')
name= input('Please input a name: ')
noun1= input('Please input a noun: ')
liquid= input('Please input a type of liquid: ')
verb3 = input('Please input verb ending in -ing: ')
body_part= input('Please input a part of the body(plural): ')
noun2= input('Please input a plural noun: ')
verb4= input('Please input a verb ending in -ing: ')
noun3= input('Please input a noun: ')

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