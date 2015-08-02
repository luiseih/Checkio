# Given a sequence of unique numbers, count the number of inversions in the sequence.
# Input: Tuple of ints.
# Output: The inversion number as an integer
# Precondition: 2 < len(sequence)< 200
#               len(sequence) == len(set(sequence))
#               all(-100 < x < 100 for x in sequence)

def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    count = 0
    i = 0
    while i < len(sequence):
        for num in sequence:
            if sequence[i] > num and sequence.index(num) > i:
                count += 1

            else:
                continue
        i += 1

    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
