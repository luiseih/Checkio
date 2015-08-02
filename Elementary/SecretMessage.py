'''
Program that takes a string as input, reads the CAPITAL letters, and
spits them out to form a message.

Precondition:
    0 < len(text) <= 1000
    all(ch in string printable for ch in text)
'''

# From now on, I will check the PREconditions and what to do
# if they are not met first. Saves a lot of time!

def text_is_eligible(text):
    if len(text) > 0 and len(text) <= 1000:
        return True
    else:
        return False


def find_message(text):
    if text_is_eligible(text):
        message = ""
        for char in text:
            if char.isupper():
                message += char
            else:
                continue
        return message
    else:
        return ""

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
