import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: # for cases like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn =  input("Did you mean %s instead?\nEnter y for Yes or n for No: " % get_close_matches(word, data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'n':
            return "The word does not exist, please double check it."
        else:
            return "Sorry, we didn't understand your entry, please try again."
    else:
        return "The word doesn't exist!"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
