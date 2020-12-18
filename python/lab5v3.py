import random

eyes = ['^', '-', '*', 'T', 'o', '$', '@']
mouth = ['_', '.', '=', 'o', '>']

x = 0
while x < 5:
    random_eyes = random.choice(eyes)
    random_mouth = random.choice(mouth)
    print(random_eyes + random_mouth + random_eyes)
    x += 1
print('done')