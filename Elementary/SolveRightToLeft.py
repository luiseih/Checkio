# Input: A sequence of strings as a tuple.
# Output: The text as a string.
# Precondition: 0 < len(phrases) < 42

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    text = ','.join(phrases)
    result = text.replace('right', 'left')

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
