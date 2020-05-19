import json
from difflib import get_close_matches 

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.capitalize in data:
        return data[word.capitalize()]
    elif word.upper in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press 'y' for yes or 'n' for no:")
        decide = decide.lower()
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            print("Word do not exist. Please check the word again.")    
        else:
            print("You have entered wrong input please enter just y or n")
        


word = input("Enter the word you want search:")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

