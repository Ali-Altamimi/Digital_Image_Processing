from my_io import io
import math
from subtract import Subtract as sub


class Utility:
    def is_same_pic(img1, img2, dimensions):
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                if (int(img1[i][j]) != int(img2[i][j])):
                    print("Different values:"
                          + "\ni = " + str(i)
                          + "\nj = " + str(j)
                          + "\n\nimg1 value is " + str(img1[i][j])
                          + "\nimg2 value is " + str(img2[i][j]))
                    return False
        return True

    def is_out_off_range(img1, dimensions):
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                if (int(img1[i][j]) > 255 or img1[i][j] < 0):
                    print("Out of range values:"
                          + "\ni = " + str(i)
                          + "\nj = " + str(j)
                          + "\n\nimg1 value is " + str(img1[i][j]))
                    return False
        return True

    def find_value_of_out_range(img1, dimensions):
        min = 10000
        max = -1000
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                if (int(img1[i][j] > max)):
                    max = img1[i][j]
                if (int(img1[i][j]) < min):
                    min = img1[i][j]
        print("Min is : " + str(min) +
              "\nMax is : " + str(max))

    def normalize(img1, dimensions):
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = img1[i][j] + 255

        return result

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
        # Finding the probability of having the intensity in the whole image
        for i in range(255):
            intensity = int(intensities[i])
            probability[i] = float(intensity / ((dimensions[0] * dimensions[1]) - 1))
        for i in range(255):
            cumulative_probability[i] = cumulative_probability[i - 1] + probability[i]
        # Equalizing the image
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                pixel_intensity = int(img1[i][j])
                result[i][j] = int(float(cumulative_probability[pixel_intensity]) * 255)
        io.write(result, output_name)

    def histogram2(img1, dimensions):
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

        return result

    def smooth(path1, dimensions):
        new_dimensions = [522, 522]
        img1 = io.read2(path1, 10, new_dimensions)
        new_img1 = Utility.translation2(img1, 5, new_dimensions)
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
        sigma = 2
        K = 1.67
        kernel = [[0 for row in range(5)] for column in range(5)]
        # kernel = [[0, 1, 2, 1, 0],
        #           [1, 3, 5, 3, 1],
        #           [2, 5, 9, 5, 2],
        #           [1, 3, 5, 3, 1],
        #           [0, 1, 2, 1, 0]]

        for i in range(5):
            for j in range(5):
                kernel[i][j] = K * math.exp(-(math.pow(i - 2, 2) + math.pow(j - 2, 2)) / (2 * math.pow(sigma, 2)))

        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                temp = 0
                for x in range(5):
                    for y in range(5):
                        temp += float(new_img1[i + x][j + y]) * kernel[x][y]
                result[i][j] = int(temp / 25)

        # x = utility.histogram(result, dimensions)
        # x = Utility.is_same_pic(new_img1, result, dimensions)
        # Utility.find_value_of_out_range(result, dimensions)

        return result

    def unsharp(img1, img2, dimensions):
        result = sub.Subtract.sub_two_matrices(img1, img2, dimensions)
        # x = Utility.is_out_off_range(result, dimensions)
        Utility.find_value_of_out_range(result, dimensions)

        # you have signed integers, you can't have that . -183 is not a valid pixel number .... i think
        # true so do i add 183?
        # I don't think so. The problem is that when you go above 255 you have an integer overflow.... thats bad.. you have to do everything in integers and then divide by the size of the kernel and then turn it into' \
        #      'byte 0-255'
        Utility.find_value_of_out_range(result, dimensions)

        result = sub.Subtract.add_two_matrices(img1, result, dimensions)
        min = 10000
        max = -1000
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                if (int(img1[i][j]) > max):
                    max = int(img1[i][j])
                if (int(img1[i][j]) < min):
                    min = int(img1[i][j])
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = result[i][j] - (min)
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = (result[i][j] / max)
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                result[i][j] = int(result[i][j] * 255)
        # for i in range(dimensions[0]):
        #     for j in range(dimensions[1]):
        #             result[i][j] = result[i][j]& 0xff
        # x = Utility.is_out_off_range(result, dimensions)
        Utility.find_value_of_out_range(result, dimensions)
        io.write(result, "lenda_unsharpmask")

    def sharpening(path1, dimensions):
        new_dimensions = [518, 518]
        img1 = io.read2(path1, 6, new_dimensions)
        new_img1 = Utility.translation2(img1, 5, new_dimensions)
        result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]

        kernel = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                temp = 0
                for x in range(3):
                    for y in range(3):
                        temp += float(new_img1[i + 3 + x - 1][j + 3 + y - 1]) * kernel[x][y]
                result[i][j] = int(temp / 9)

        result = sub.Subtract.sub_two_matrices(img1, result, dimensions)
        # result = Utility.normalize(result, dimensions)

        x = Utility.is_out_off_range(result, dimensions)
        Utility.find_value_of_out_range(result, dimensions)
        # x = utility.is_same_pic(img1, reresult,sult, dimensions)
        # print(x)
        return result
