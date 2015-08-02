'''
Given a positive integer, calculate the product of the digits excluding zeroes.
Precondition: 0 < number < 10^6
'''

def checkio(number):
    if number < 0 or number > 10**6:
        return 0
    else:
        numbers = str(number)
        result = 1

        for num in numbers:
            if int(num) == 0:
                continue
            else:
                result *= int(num)

        return result



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
