# Lab 16 Compute ARI

import string 

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


with open('princess_of_chaos.txt', 'r', encoding='utf-8') as file:
    book = file.read()
    

'''
The score is computed by multiplying the number 
of characters divided by the number of words by 4.71, 
adding the number of words divided by the number of sentences 
multiplied by 0.5, and subtracting 21.43. If the result is a decimal, 
always round up, and if the result is higher than 14, it should be set to 14.
'''
# get number of sentences

sentences = book.count('.')
sentences += book.count('!') 
sentences += book.count('?')

# get number of characters

no_punctuation = book.translate(str.maketrans('', '',string.punctuation)) 

characters = len(no_punctuation)

# get number of words

words = len(no_punctuation.split()) # split into a list of words

# get the score

score = (round(4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43))

# Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.

print(f"""
--------------------------------------------------------
The ARI for princess_of_chaos.txt is {score} 
This corresponds to a {ari_scale[score]['grade_level']} level of difficulty 
this is suitibale for an average person {ari_scale[score]['ages']} years old.
--------------------------------------------------------
""")