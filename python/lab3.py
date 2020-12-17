 # Lab 3 - Grading

grade = input('Please enter a number grade (0-100) to get a letter grade: ')
grade = int(grade)

if grade > 100:
    print('Invalid input.')
elif grade >= 95: 
    print('You get an A+!')
elif grade >= 90:
    print('You get an A-!')
elif grade >= 85:
    print('You get a B+!')
elif grade >= 80:
    print('You get a B-!')
elif grade >= 75:
    print('You get a C+!')
elif grade >= 70:
    print('You get a C-!')
elif grade >= 65:
    print('You get a D+!')
elif grade >= 60:
    print('You get a D-!')
else:
    print('You get an F!')