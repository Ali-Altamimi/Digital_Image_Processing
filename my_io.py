import numpy as np


class io:
    def read(file_name, dimensions):
        t = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        with open(file_name, "r+b") as binary_file:
            # Read the whole file at once
            data = binary_file.read()
            string_data = " ".join(map(str, data))
            list_data = string_data.split(" ")
            counter = 0
            for i in range(dimensions[0]):
                for j in range(dimensions[1]):
                    t[i][j] = list_data[counter]
                    counter = counter + 1
        return t

    def read2(file_name, n, dimensions):
        t = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
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

    def write(matrix, filename):
        f = open("output/" + filename + '.raw', 'wb')
        casted_matrix = np.matrix(matrix).astype('uint8')
        f.write(casted_matrix)
        f.close()
