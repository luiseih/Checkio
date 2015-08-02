def checkio(number):
    binaryNum = bin(number)
    count = 0
    
    for char in binaryNum:
        if char == '1':
            count += 1
    
    return count
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
