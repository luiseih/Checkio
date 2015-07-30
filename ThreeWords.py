'''
Module that takes a string with words and/or numbers with a space in between.
Verifies that the string contains THREE alpha words in succession.
If it does, returns TRUE, else FALSE.

Precondition:
Input contains words and/or numbers.
There are no mixed words (letters and digits combined).
0 < len(words) < 100
'''


# Checking precondition...
def words_are_valid(words):
    for word in words:
        if len(word) > 0 and len(word) < 100:
            continue
        else:
            return False
    return True
    
    
def checkio(words):
    if words_are_valid(words):
        # We want to count the WORDS not the CHARS, so we split
        # the string into an array of WORDS...
        word_list = words.split(' ')
        count = 0
        for word in word_list:
            if word.isalpha():
                count += 1
                if count == 3:
                    return True
                else:
                    continue
            else:
                count = 0
                continue
        return False
    else:
        return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
