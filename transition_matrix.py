import constants
# create the empty matrix
# 0 - 11 is note value, multiples of 12 for duration from small to big

# Generates a matrix filled with zeroes with the given dimensions and size
# Int, Int -> Matrix
def genNDMatrix(size, dimension):
   assert dimension > 0
   if dimension == 1:
       return [0 for x in range(size)]
   else:
       return [genNDMatrix(size, dimension - 1) for x in range(size)]

# [(Int, Float)] -> Matrix
def populateMatrix(info_array, size, dimensions):
        mat = genNDMatrix(size,dimensions)
        for idx in range(len(info_array) - dimensions + 1):
            cursor = mat
            for i in range(dimensions - 1):
                cursor = cursor[info_array[idx + i]]
            cursor[info_array[idx + dimensions - 1]] += 1
        print(mat)
        return mat

def prepList(arr, array_dict):
    return list(map(lambda x : array_dict.index(x), filter(lambda x : x in array_dict, arr)))
