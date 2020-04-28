from math import sqrt


def derivX(img):
    result = [[0 for row in range(img.dimensions[1])] for column in range(img.dimensions[0])]
    for i in range(img.dimensions[0]-1):
        for j in range(img.dimensions[1]-1):
            result[i][j] = (((int(img.matrix[i][j+1])) - (int(img.matrix[i][j]))) + ((int(img.matrix[i+1][j+1])) - (int(img.matrix[i+1][j]))))/2

    return result


def derivY(img):
    result = [[0 for row in range(img.dimensions[1])] for column in range(img.dimensions[0])]
    for i in range(img.dimensions[0]-1):
        for j in range(img.dimensions[1]-1):
            result[i][j] = (((int(img.matrix[i+1][j])) - (int(img.matrix[i][j]))) + ((int(img.matrix[i+1][j+1])) - (int(img.matrix[i][j+1]))))/2

    return result


def gradient(img):
    result = [[0 for row in range(img.dimensions[1])] for column in range(img.dimensions[0])]
    grad_x = derivX(img)
    grad_y = derivY(img)

    for i in range(img.dimensions[0]):
        for j in  range(img.dimensions[0]):
            result[i][j] = abs(sqrt((grad_x[i][j] ** 2) + (grad_y[i][ j] ** 2)))

    return result


