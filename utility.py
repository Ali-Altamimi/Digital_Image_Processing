import my_io
import math
from subtract import Subtract as sub
from subtract.Subtract import Subtract as sub

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


def normalize(img, dimensions):
    min = 100000000
    max = -100000000
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if float(img[i][j]) < min:
                min = float(img[i][j])
    result_min = [[0 for row in range(dimensions[1])] for column in range(dimensions[0])]
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            result_min[i][j] = img[i][j] - min

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if float(result_min[i][j]) > max:
                max = float(result_min[i][j])

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if max == 0:
                max = 1
            img[i][j] = int(255 * (result_min[i][j] / max))
    return img


def inverse(path1, dimensions, output_name):
    img1 = my_io.read(path1, dimensions)
    result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            result[i][j] = 255 - int(img1[i][j])
    my_io.write8(result, output_name)


def translation(path1, move, dimensions, output_name):
    img1 = my_io.read(path1, dimensions)
    result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if ((i + move + 1) <= dimensions[0] and ((j + move + 1) <= dimensions[1])):
                result[i + move][j + move] = img1[i][j]
    my_io.write8(result, output_name)


def translation2(img, move, dimensions):
    result = [[0 for row in range(dimensions[1])] for column in range(dimensions[0])]
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if ((i + move + 1) <= dimensions[0] and ((j + move + 1) <= dimensions[1])):
                result[i + move][j + move] = img[i][j]
    return result


def histogram(path1, dimensions, output_name):
    img1 = my_io.read(path1, dimensions)
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
    my_io.write8(result, output_name)


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
    img1 = my_io.read2(path1, 10, new_dimensions)
    new_img1 = translation2(img1, 5, new_dimensions)
    result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
    sigma = 2
    K = 1.67
    kernel = [[0 for row in range(5)] for column in range(5)]

    for i in range(5):
        for j in range(5):
            kernel[i][j] = K * math.exp(-(math.pow(i - 2, 2) + math.pow(j - 2, 2)) / (2 * math.pow(sigma, 2)))

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            temp = 0
            for x in range(5):
                for y in range(5):
                    temp += float(new_img1[i + 5 + x - 2][j + 5 + y - 2]) * kernel[x][y]
            result[i][j] = int(temp / 25)

    return result


def unsharp(img1, img2, dimensions):
    result = sub.Subtract.sub_two_matrices(img1, img2, dimensions)
    result = sub.Subtract.add_two_matrices(img1, result, dimensions)
    min = 100000000
    max = -100000000
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if int(result[i][j]) < min:
                min = int(result[i][j])
    result_min = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            result_min[i][j] = result[i][j] - min

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if int(result_min[i][j]) > max:
                max = int(result_min[i][j])

    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            result[i][j] = 255 * (result_min[i][j] / max)

    # for i in range(dimensions[0]):
    #     for j in range(dimensions[1]):
    #         result[i][j] = int(result[i][j] * 255)

    find_value_of_out_range(result, dimensions)
    my_io.write8(result, "lenda_unsharpmask")


def sharpening(path1, dimensions):
    new_dimensions = [518, 518]
    img1 = my_io.read2(path1, 6, new_dimensions)
    new_img1 = translation2(img1, 5, new_dimensions)
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
    return result


def threshold(img, dimensions, threshold_point):
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if int(img[i][j]) > threshold_point:
                img[i][j] = 255
            else:
                img[i][j] = 0

    return img


def erosion(img):
    result = [[0 for row in range(img.dimensions[1])] for column in range(img.dimensions[0])]
    condtion = True
    for i in range(1, img.dimensions[0]-2):
        for j in range(1, img.dimensions[1]-2):
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if img.matrix[i-x][j-y] == "0":
                        condtion = False
            if condtion:
                result[i][j] = 255
            else:
                result[i][j] = 0
            condtion = True
    return result

def dilation(img):
    result = [[0 for row in range(img.dimensions[1])] for column in range(img.dimensions[0])]
    condtion = True
    for i in range(1, img.dimensions[0]-2):
        for j in range(1, img.dimensions[1]-2):
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if img.matrix[i-x][j-y] == "255":
                        condtion = False
            if condtion:
                result[i][j] = 0
            else:
                result[i][j] = 255
            condtion = True
    return result

def boundaryExtraction(img):
    new_matrix = erosion(img)
    result = sub.sub_two_matrices(img.matrix, new_matrix,  img.dimensions)
    return result



# This method increase the size of the matrix by the edges
def increase_matrix_size(img, increase_by):
    new_row = img.dimensions[1] + (increase_by * 2)
    new_column = img.dimensions[0] + (increase_by * 2)
    new_image_matrix = [[255 for row in range(new_row)] for column in
                        range(new_column)]
    for i in range(img.dimensions[0]):
        for j in range(img.dimensions[1]):
            new_image_matrix[i][j] = img.matrix[i][j]
    new_image_matrix_centered = translation2(new_image_matrix, increase_by, [new_column, new_row])
    img.matrix = new_image_matrix_centered
    img.dimensions = [new_column, new_row]


