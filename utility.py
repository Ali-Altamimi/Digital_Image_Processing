from my_io import io
import math
from subtract import Subtract as sub


class utility:
    def is_same_pic(img1, img2, dimensions):
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                if (int(img1[i][j]) != int(img2[i][j])):
                    print("Different values:"
                          + "\ni = " + str(i)
                          + "\nj = " + str(j)
                          + "\n\nimg1 value is " + str(img1[i][j])
                          + "\nimg2 value is " + str(img2[i][j]))
                    return False;
        return True;

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

    def translation2(img, move, dimensions):
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                if ((i + move + 1) <= dimensions[0] and ((j + move + 1) <= dimensions[1])):
                    result[i + move][j + move] = img[i][j]
        return result

    def histogram(path1, dimensions, output_name):
        img1 = io.read(path1, dimensions)
        intensities = [0 for row in range(255)]
        probability = [0 for row in range(255)]
        cumulative_probability = [0 for row in range(255)]
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        # building the intensity array (un-normalized histogram).
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                x = int(img1[i][j])
                intensities[x] = intensities[x] + 1
        # normalized histogram
        for i in range(255):
            x = int(intensities[i])
            probability[i] = float(x / ((dimensions[0] * dimensions[1]) - 1))
        for i in range(255):
            cumulative_probability[i] = cumulative_probability[i - 1] + probability[i]

        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                x = int(img1[i][j])

                result[i][j] = int(float(cumulative_probability[x]) * 255)

        io.write(result, output_name)

    def smooth(path1, dimensions):
        new_dimensions = [522, 522]
        img1 = io.read2(path1, 10, new_dimensions)
        new_img1 = utility.translation2(img1, 5, new_dimensions)
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        temp = 0
        sigma = 2
        K = 1.67
        kernel = [[0 for row in range(5)] for column in range(5)]

        for i in range(5):
            for j in range(5):
                kernel[i][j] = K * math.exp(-((i * i) + (j * j)) / (2 * sigma * sigma))

        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                for x in range(5):
                    for y in range(5):
                        temp += float(new_img1[i + 5][j + 5]) * kernel[x][y]
                result[i][j] = int(temp / 25)
                temp = 0
        return result

    def unsharp(img1, img2, dimensions):
        x = sub.Subtract.sub_two_matrices(img2, img1, dimensions)
        result = sub.Subtract.add_two_matrices(img1, x, dimensions)
        io.write(result, "lenda_unsharpmask")

    def sharpening(path1, dimensions):
        new_dimensions = [518, 518]
        img1 = io.read2(path1, 6, new_dimensions)
        new_img1 = utility.translation2(img1, 5, new_dimensions)
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        temp = 0
        sigma = 2
        K = 1.67
        kernel = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                for x in range(3):
                    for y in range(3):
                        temp += float(new_img1[i + 3 + x - 1][j + 3 + y - 1]) * kernel[x][y]
                result[i][j] = int(temp / 9)
                temp = 0

        result = sub.Subtract.add_two_matrices(img1, result, dimensions)
        # x = utility.is_same_pic(img1, result, dimensions)
        # print(x)
        return result
