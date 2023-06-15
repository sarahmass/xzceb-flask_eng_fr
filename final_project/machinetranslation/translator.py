''' This moduel contains the two functions used in the final project
    for the IBM Coursera course: Python Project for AI & Application Development.
'''

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    '''
        input argument: string in English 
        
        MyMemoryTranslator expects a lowercase strings so to avoid failures due to 
        mis-translations of capital letters all input strings are cast to lower case characters.  
        
        returns: a string for the french tranlastion of the input string
    '''
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text.lower())
    return french_text

def french_to_english(french_text):
    '''
        input: string in French 
        
        MyMemoryTranslator expects a lowercase strings so to avoid failures due to 
        mis-translations of capital letters all input strings are cast to lower case characters. 

        returns: a string of the english translation of the input string
    '''
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text.lower())
    return english_text
