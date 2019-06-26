import random

# Returns a random number based on the weights provided
# [Float] -> Int


def weighted_random(weights):
    tally = random.random()
    for i, wt in enumerate(weights):
        if tally <= wt:
            return i
        else:
            tally -= wt
    raise Exception("The sum of the inputted array must be 1!")

# Unneccessary - remove?
# Finds the dimensionality of a matrix, assuming it is square
# Matrix -> Int


def matrix_depth(matrix):
    if isinstance(matrix, list):
        return 1 + matrix_depth(matrix[0])
    else:
        return 0

# generates a cartesian product
# [Number] [Number] -> [(Number, Number)]


def cartesian_product(list_a, list_b):
    cart_prod = []
    for a in list_a:
        for b in list_b:
            cart_prod.append((a, b))
    return cart_prod


# -- DEPRECATED --
# most common sequences
"""
def sequence_count(info_array, combinations, dimensions):
    cnt = Counter()
    for idx in range(len(info_array) - dimensions + 1):
        seq = []
        for i in range(dimensions):
            seq.append(info_array[idx + i])
        cnt[tuple(seq)] += 1
    return cnt
"""


def all_combos(combinations, dimensions, acc=None):
    if dimensions < 1:
        return acc
    elif acc is None:
        return all_combos(combinations, dimensions - 1, list(map(lambda x: [x], range(combinations))))
    else:
        new_acc = []
        for ele in acc:
            for new_ele in list(range(dimensions)):
                ele.append(new_ele)
                new_acc.append(ele)
        return all_combos(combinations, dimensions - 1, new_acc)
