from my_io import io


class utility:
    def sub(path1, path2, dimensions, output_name):
        img1 = io.read(path1, dimensions)
        img2 = io.read(path2, dimensions)

        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = int(img1[i][j]) - int(img2[i][j])
        io.write(result, output_name)

    def inverse(path1, dimensions, output_name):
        img1 = io.read(path1, dimensions)
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = 255 - int(img1[i][j])
        io.write(result, output_name)

    def translation(path1, move, dimensions, output_name):
        img1 = io.read(path1, dimensions)
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                if ((i + move + 1) <= dimensions[0] and ((j + move + 1) <= dimensions[1])):
                    result[i + move][j + move] = img1[i][j]
        io.write(result, output_name)