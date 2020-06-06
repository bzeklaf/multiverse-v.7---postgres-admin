from difflib import SequenceMatcher
import difflib
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()
def anticipation():
    small_dictionary = {'First Key':['This is a first sentence', 'Here is another sentence'], 'Second Key': ['And anooother sentence...', 'and one more....']}
    body_of_text = 'Here is the large body of text. Each sentence in this body, should be compared to each of the values in the dictionary. If the comparision ration is above certain treshold, corresponding key should be printed.'
    sentencing = sent_tokenize(body_of_text)
    list_of_keys = []
    for key,value in small_dictionary.items():
        for item in value:
            for token in sentencing:
                resulting = similar(item,token)
                if resulting >= 0.1:
                    list_of_keys.append(key)
    list_of_keys = set(list_of_keys)
    return list_of_keys

keys = anticipation()

print(keys)