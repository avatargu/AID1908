def search(sequence,number,lower = 0,upper = None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        # assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence,number,middle + 1,upper)
        else:
            return search(sequence,number,lower,middle)

print(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000, 100000, 1000000],1000))