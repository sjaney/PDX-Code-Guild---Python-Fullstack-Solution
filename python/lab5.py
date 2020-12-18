# Lab 5 Random Emoticon Generator

# Version 1
import random

eyes = [';', ':', '8']
nose = ['-', 'o', '>']
mouth = ['D', ')', '(', 'P', 'x', '[']

# random_eyes = random.choice(eyes)
# random_nose = random.choice(nose)
# random_mouth = random.choice(mouth)

# print(random_eyes + random_nose + random_mouth) 
 # --------------------------- #

# Version 2 
x = 0
while x < 5:
    random_eyes = random.choice(eyes)
    random_nose = random.choice(nose)
    random_mouth = random.choice(mouth)
    print(random_eyes + random_nose + random_mouth)
    x += 1
print('done')
 