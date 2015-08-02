VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper().strip('.,').split()
    count = 0
    
    for word in text:
        letter_count = 0
        for char in word:
            if char in VOWELS:
                letter_count += 1
            elif char in CONSONANTS:
                letter_count -= 1
                    
            if letter_count > 1 or letter_count < -1:
                letter_count = 0
                pass
            else:
                letter_count = 0
                letter_count = 0
                count += 1
        
        
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
