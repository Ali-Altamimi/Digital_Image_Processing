
def co_Occurrence(img, intensity):
    result = [[0 for row in range(intensity[1])] for column in range(intensity[0])]

    for i in range(img.dimensions[0]-1):
        for j in range(img.dimensions[1]):
            result[int(img.matrix[i][j])][int(img.matrix[i+1][j])] += 1
    return result