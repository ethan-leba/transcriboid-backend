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

# Unneccessary - remove?
# Finds the dimensionality of a matrix, assuming it is square
# Matrix -> Int
def matrix_depth(matrix):
    if isinstance(matrix, list):
        return 1 + matrix_depth(matrix[0])
    else:
        return 0
