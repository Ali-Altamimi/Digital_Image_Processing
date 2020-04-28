import numpy as np


def read(path, dimensions):
    t = [[0 for row in range(dimensions[1])] for column in range(dimensions[0])]
    with open(path, "r+b") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        string_data = " ".join(map(str, data))
        list_data = string_data.split(" ")
        for i in range(dimensions[0] * dimensions[1]):
            x = i % dimensions[0]
            y = int(i / dimensions[0])
            cordenent = x + (y * dimensions[0])
            # if cordenent < dimensions[0]
            t[x][y] = int(list_data[cordenent])
    return t


def read2(file_name, n, dimensions):
    t = [[0 for row in range(dimensions[1])] for column in range(dimensions[0])]
    with open(file_name, "r+b") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        string_data = " ".join(map(str, data))
        list_data = string_data.split(" ")
        counter = 0
        for i in range(dimensions[0] - n):
            for j in range(dimensions[1] - n):
                t[i][j] = list_data[counter]
                counter = counter + 1
    return t


def customised_matrix_write8(img, new_dimensions):
    f = open("output\\" + img.name + '.raw', 'wb')
    casted_matrix = [0 for row in range(new_dimensions[0] * new_dimensions[1])]
    for i in range(new_dimensions[0]):
        for j in range(new_dimensions[1]):
            casted_matrix[i + (j * new_dimensions[0])] = img.matrix[i][j]
    x = np.array(casted_matrix)
    x = np.uint8(x)
    f.write(x)
    f.close()


def write(img, bites_type):
    f = open("output\\" + img.name + '.raw', 'wb')
    casted_matrix = [0 for row in range(img.dimensions[0] * img.dimensions[1])]
    for i in range(img.dimensions[0]):
        for j in range(img.dimensions[1]):
            casted_matrix[i + (j * img.dimensions[0])] = img.matrix[i][j]
    x = np.array(casted_matrix)
    if bites_type == "int8":
        x = np.int8(x)
    elif bites_type == "int16":
        x = np.int16(x)
    elif bites_type == "uint16":
        x = np.uint16(x)
    f.write(x)
    f.close()
