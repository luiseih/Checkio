OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == 'conjunction':
        return x == y and y == 1
    elif operation == 'disjunction':
        return x == 1 or y == 1
    elif operation == 'implication':
        return x == y or y == 1
    elif operation == 'exclusive':
        return x != y
    elif operation == 'equivalence':
        return x == y
    else:
        return  0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
