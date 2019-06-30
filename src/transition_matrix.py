
# Converts an abritrarily nested array so that every 1D array sums to one.
# [N-D Matrix] -> [N-D Matrix]


def nd_convert_to_probabilities(mat):
    if isinstance(mat[0], list):
        return list(map(lambda x: nd_convert_to_probabilities(x), mat))
    else:
        if sum(mat) != 0:
            return list(map(lambda x: x / sum(mat), mat))
        else:
            return mat


# Generates a matrix filled with zeroes with the given dimensions and size.
# Int, Int -> Matrix


def gen_nd_matrix(size, dimension):
    assert dimension > 0
    if dimension == 1:
        return [0 for x in range(size)]
    else:
        return [gen_nd_matrix(size, dimension - 1) for x in range(size)]


# Populates a transition matrix with the given size and dimensions.
# [Int] Int Int -> Matrix


def populate_matrix(info_array, size, dimensions):
    mat = gen_nd_matrix(size, dimensions)
    for idx in range(len(info_array) - dimensions + 1):
        cursor = mat
        for i in range(dimensions - 1):
            cursor = cursor[info_array[idx + i]]
        cursor[info_array[idx + dimensions - 1]] += 1
    print(mat)
    return mat


# Picks a random entry point for the matrix to initialize
# [Int] Int -> [Int]
def entry_point(info_array, dimensions):
    lst = []
    for idx in range(len(info_array) - dimensions + 1):
        lst.append([info_array[i] for i in range(idx, dimensions + idx)])
    return lst


# Converts a list of numbers into indexes for creating a transition matrix.
# [X] [X] -> [Int]


def prep_list(arr, array_dict):
    return list(map(lambda x: array_dict.index(x), filter(lambda x: x in array_dict, arr)))
