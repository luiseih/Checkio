# Check whether there is a pair of words, such that one word is the end of
# another (a suffix of another). For example: {"hi", "hello", "lo"} --
# "lo" is the end of "hello", so the result is True.
#   Input: Words as a set of strings.
#   Output: True or False, as a boolean.
#   Precondition: 2 <= len(words) < 30
#   all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words) 


def checkValidity(words):  # check precondition.
    for word in words:
        if len(word) < 1 or len(word) > 30:
            return False
        else:
            continue
    return True


def checkio(words):
    if checkValidity(words):
        for word1 in words:
            for word2 in words:
                if (len(word1) > len(word2)) and (word1.endswith(word2)):
                    return True
    return False
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    assert checkio({"longest", "aa", "a"}) == True, "Only end"
