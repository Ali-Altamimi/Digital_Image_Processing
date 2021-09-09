from models.image import Image
import utilities.io as io
import json


class Subtract:
    def sub_two_files(path1, path2, dimensions, output_name):
        img1 = io.read(path1, dimensions)
        img2 = io.read(path2, dimensions)

        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = int(img1[i][j]) - int(img2[i][j])
        io.write8(result, output_name)

    def sub_two_matrices(img1: Image, img2: Image, name: str='result') ->Image:
        matrix = [[0 for row in range(img1.dimensions[0])] for column in range(img1.dimensions[1])]
        # print(len(img1.matrix), len(img2.matrix))
        # print(len(img1.matrix[0]), len(img2.matrix[0]))
        for i in range(img1.dimensions[1]):
            for j in range(img1.dimensions[0]):
                try:
                    matrix[i][j] = int(img1.matrix[i][j]) - int(img2.matrix[i][j])
                except(IndexError):
                    print(i, j)
        return Image.exist(name, matrix=matrix)

    def add_two_matrices(img1: Image, img2: Image, name: str='result'):
        result = [[0 for row in range(img1.dimensions[0])] for column in range(img1.dimensions[1])]
        for i in range(img1.dimensions[0]):
            for j in range(img1.dimensions[1]):
                result[i][j] = int(img1.matrix[i][j]) + int(img2.matrix[i][j])
        image = Image.exist(name, matrix=result)
        return image