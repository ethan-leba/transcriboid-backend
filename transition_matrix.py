import constants
# Generates a matrix filled with zeroes with the given dimensions and size
# Int, Int -> Matrix
def genNDMatrix(size, dimension):
   assert dimension > 0
   if dimension == 1:
       return [0 for x in range(size)]
   else:
       return [genNDMatrix(size, dimension - 1) for x in range(size)]

# Populates a transition matrix with the given size and dimensions 
# [Int] Int Int -> Matrix
def populateMatrix(info_array, size, dimensions):
        mat = genNDMatrix(size,dimensions)
        for idx in range(len(info_array) - dimensions + 1):
            cursor = mat
            for i in range(dimensions - 1):
                cursor = cursor[info_array[idx + i]]
            cursor[info_array[idx + dimensions - 1]] += 1
        print(mat)
        return mat

# Converts a list of numbers into indexes for creating a transition matrix
# [Number] [Int] -> [Int]
def prepList(arr, array_dict):
    return list(map(lambda x : array_dict.index(x), filter(lambda x : x in array_dict, arr)))
