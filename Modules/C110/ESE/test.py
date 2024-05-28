def findPairs(lnums, targetSum):
    pairs = []
    for num in lnums:
        if num % targetSum == 0:
            pairs.append((num, targetSum))
    return pairs

=