#!/usr/bin/env python3

import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    # Regular Expression Search. Create a list of words composed
    # only of (converted) UPPERcase alpha characters.
    text = re.findall(r"\w+",text.upper())
    count = 0
    for word in text:
        if len(word) < 2:
            continue
        else:
            isVowel = ''
            isValid = True
            for char in word:
                if (char not in VOWELS) and (char not in CONSONANTS):
                    isValid = False
                    break
                elif char in VOWELS:
                    if isVowel == '' or isVowel == False:
                        isVowel = True
                    else:
                        isValid = False
                        break
                elif char in CONSONANTS:
                    if isVowel == '' or isVowel == True:
                        isVowel = False
                    else:
                        isValid = False
                        break
            if isValid:
                count += 1
    return count


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
