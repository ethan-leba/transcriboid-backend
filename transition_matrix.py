# create the empty matrix
note_duration = [0.125,0.25,0.5,1]
note_dict = {
        0.125 : 0,
        0.25 : 1,
        0.5 : 2,
        1 : 3
        }
maj_scale = {0, 2, 4, 5, 7, 9, 11}
maj_scale_list = [0, 2, 4, 5, 7, 9, 11]
# 0 - 11 is note value, multiples of 12 for duration from small to big
def genMtMatrix(size):
        mat = []
        for x in range(size):
                inner_mat = []
                for y in range(size):
                        inner_mat.append(0)
                mat.append(inner_mat)
        return mat

# [(Int, Float)] -> Matrix
def populateMatrix(raw_notes):
        mat = genMtMatrix(12)
        for idx in range(len(raw_notes)-1):
            mat[raw_notes[idx][0]][raw_notes[idx + 1][0]] += 1
        print(mat)
        return mat

# [(Int, Float)] -> Matrix
def populateMajorScaleMatrix(raw_notes):
        mat = genMtMatrix(7)
        prepped_notes = prepMajorScale(raw_notes)
        for idx in range(len(prepped_notes)-1):
            mat[prepped_notes[idx]][prepped_notes[idx + 1]] += 1
        print(mat)
        return mat

def prepMajorScale(raw_notes):
    return list(map(lambda x : maj_scale_list.index(x), filter(lambda x : x in maj_scale, map(lambda x : x[0], raw_notes))))
# [(Int, Float)] -> Matrix
def populateDurationMatrix(raw_notes):
        mat = genMtMatrix(4)
        for idx in range(len(raw_notes)-1):
                mat[note_dict.get(raw_notes[idx][1], 0)][note_dict.get(raw_notes[idx + 1][1], 0)] += 1
        print(mat)
        return mat
