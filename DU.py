def down(img):
    result = [[0 for row in range(int(img.dimensions[1]/2))] for column in range(int(img.dimensions[0]/2))]
    for i in range(int(img.dimensions[0]/2)):
        for j in range(int(img.dimensions[1]/2)):
            result[i][j] = img.matrix[i*2][j*2]
    return result

def up(img):
    result = [[0 for row in range(img.dimensions[1])] for column in range(img.dimensions[0])]
    for i in range(int(img.dimensions[0]/2)):
        for j in range(int(img.dimensions[1]/2)):
            # result[i][j] = img.matrix[i][j]
            result[i*2][j*2] = img.matrix[i][j]
            result[i*2+1][j*2] = img.matrix[i][j]
            result[i*2][j*2+1] = img.matrix[i][j]
            result[i*2+1][j*2+1] = img.matrix[i][j]
    return result