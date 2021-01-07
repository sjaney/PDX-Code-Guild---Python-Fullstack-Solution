# Lab 15 Count Words
import requests
import string 
# Make everything lowercase, strip punctuation, split into a list of words.

def use_requests():
    response = requests.get('https://www.gutenberg.org/files/64214/64214-0.txt')
    book = response.text.lower() # make everything lowercase
    return book


book = use_requests()

'''
str.maketrans creates a translation table containing the mapping
between two characters. To remove all punctuations str.maketrans('', '', string.punctuation) 
creates mapping from empty string to empty string, and punctuations to None.
'''
no_punctuation = book.translate(str.maketrans('', '',string.punctuation)) 


words = no_punctuation.split() # split into a list of words

''' Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. 
If it is, increment its count.'''

word_list = {} # create empty dict

for word in words:
    if word not in word_list:
        word_list[word] = 0
    word_list[word] += 1

# Print the most frequent top 10 out with their counts. You can do that with the code below.

# word_dict is a dictionary where the key is the word and the value is the count
most_frequent = list(word_list.items()) # .items() returns a list of tuples
most_frequent.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(most_frequent))):  # print the top 10 word, or all of them, whichever is smaller
    print(most_frequent[i])