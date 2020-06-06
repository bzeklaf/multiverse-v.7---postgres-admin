import re

from difflib import SequenceMatcher
import difflib
import nltk
from nltk.tokenize import sent_tokenize

from .app1 import a1_af, a1_anti_af, a1_cw, a1_cw_not, a1_pattern, a1_rs, a1_app, a1_app_not, a2_pattern, a2_rs

def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

#anticipation 
def anticipation_func(body_of_text):
    list_of_dictionaries = [a1_af] 
    sentencing = sent_tokenize(body_of_text)
    list_of_keys = []
    for small_dictionary in list_of_dictionaries:
      for key,value in small_dictionary.items():
        for item in value:
            for token in sentencing:
                resulting = similar(item,token)
                if resulting >= 0.95:
                    list_of_keys.append(key)
    if(len(list_of_keys)>0):
        list_of_keys = set(list_of_keys)
    return list_of_keys

#anti_anticiption
def anti_anticipation(body_of_text):

    list_of_dictionaries = [a1_anti_af]
    sentencing = sent_tokenize(body_of_text)
    
    list_of_keys = []
    for small_dictionary in list_of_dictionaries:
     for key,value in small_dictionary.items():
        
        for item in value:
            found_value = 0
            for token in sentencing:
                resulting = similar(item,token)
                
                if resulting >=0.9:
                    found_value = 1
                    continue
                    
                    
            if found_value == 0:
                list_of_keys.append(key)
    list_of_keys = set(list_of_keys)
    return list_of_keys

#CW
def cw_processing(text):
    wording = text
    list_of_dictionaries_a = [a1_cw]
    for small_dictionary_a in list_of_dictionaries_a:
     for key,value in small_dictionary_a.items():
        for item in value:
            if item in wording:
                yield(key)
                break
    list_of_dictionaries_b = [a1_cw_not]
    for small_dictionary_b in list_of_dictionaries_b:        
     for key,value in small_dictionary_b.items():
        for item in value:
            if item not in wording:
                yield(key)
                break   
#REGEX
def reg_pro(text):
    
    list_of_patterns = [a1_pattern, a2_pattern]
    list_of_rs=[a1_rs, a2_rs]
    wording = text
    little_box = []
    for patterns in list_of_patterns:
      for rs in list_of_rs:   
       for item in patterns:
        if re.search(item, wording):
            little_box.append((rs[patterns.index(item)]))
    return(little_box)
       
#APP
def appoint_processing(text):
   wording = text
   list_of_dictionaries_a = [a1_app]
   for small_dictionary in list_of_dictionaries_a:
    for key,value in small_dictionary.items():
       for item in value:
           if item in wording:
               yield (key)
               break
   list_of_dictionaries_b = [a1_app_not]
   for small_dictionary in list_of_dictionaries_b:
    for key,value in small_dictionary.items():
       for item in value:
           if item not in wording:
               yield (key)
               break 

