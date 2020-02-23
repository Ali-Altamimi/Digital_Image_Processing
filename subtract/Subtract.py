from my_io import io


class Subtract:
    def sub_two_files(path1, path2, dimensions, output_name):
        img1 = io.read(path1, dimensions)
        img2 = io.read(path2, dimensions)

        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = int(img1[i][j]) - int(img2[i][j])
        io.write(result, output_name)
    def sub_two_matrices(img1, img2, dimensions):

        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = int(img1[i][j]) - int(img2[i][j])
        return result

    def add_two_matrices(img1, img2, dimensions):

        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = int(img1[i][j]) + int(img2[i][j])
        return result