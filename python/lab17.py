# Lab 17 Quote API

import requests
import json

'''
# Version 1
# get random quote and send request
random_quotes = requests.get('https://favqs.com/api/qotd')

# print(random_quotes)
# parse the JSON in the response into a python dictionary
quotes = json.loads(random_quotes.text)

# show quote and author
print(quotes['quote']['body'])
print(quotes['quote']['author'])
'''


'''
# Version 2
Prompt the user for a keyword, list the quotes you get in response, 
and prompt the user to either show the next page or enter a new keyword. 
You can use string concatenation to build the URL
'''

# prompt the user for a keyword

keyword = input('Enter a keyword to search for quotes: ')

headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

while True:

    page_count = 1
    counter = 0

    # You can use string concatenation to build the URL

    url = 'https://favqs.com/api/quotes?page=' + str(page_count) + '&filter=' + keyword 

    quotes = requests.get(url, headers=headers)

    keyword_quotes = json.loads(quotes.text)

    # list the quotes you get in response

    while counter < 25:
        print(keyword_quotes['quotes'][counter]['body'])
        counter += 1

    # prompt the user to either show the next page

    next_page = input('Enter "next page" or "done": ') 

    if next_page == 'done':
        print('Goodbye.')
        break
    elif next_page == 'next page':
        page_count += 1
    else:
        break
    

    




