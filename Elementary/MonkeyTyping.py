'''
Program that checks if any WORD contained in an array (apropiately named WORDS)
is in a TEXT string.

Precondition:
0 < len(text) <= 256
all(3 <= len(w) and w.islower() and w.isalpha() for w in words) 
'''

# Includes 2 FREE additional functions to save your sanity!

def text_is_eligible(text):  # Boolean function... method... whatever...
    if (len(text) > 0) and (len(text) <= 256):
        return True
    else:
        return False


def words_are_eligible(words):  # You gotta love booleans...
    for word in words:
        if len(word) >= 3 and word.islower() and word.isalpha():
            continue
        else:
            return False
    return True


def count_words(text, words):
    if text_is_eligible(text) and words_are_eligible(words):
        # Put the whole text thing in lowercase. i.e. 'How' and 'hoW' are the same.
        text = text.lower()
        count = 0
        for word in words:
            if word in text:
                count += 1
            else:
                continue
        return count
    else:
        return 0

# And this is why I love Python. Try to do all this in Java... o_O

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
