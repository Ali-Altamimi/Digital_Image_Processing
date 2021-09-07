from utilities.subtract import Subtract
from models.image import Image
import utilities.io as io
import math
from utilities.subtract import Subtract as sub
# from subtract.Subtract import Subtract as sub

# Kernal_size
KS_3 = 3
KS_5 = 5
KS_9 = 9
KS_15 = 15
# color
CL_WHITE = 255
CL_BLACK = 0
# Min and Max integers
INT_MAX =9223372036854775807
INT_MIN =-9223372036854775806

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


def find_value_of_out_range(image):
    min = 10000
    max = -1000
    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            if (int(image.matrix[i][j] > max)):
                max = image.matrix[i][j]
            if (int(image.matrix[i][j]) < min):
                min = image.matrix[i][j]
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


def inverse(image:Image):
    result = [[0 for row in range(image.dimensions[0])] for column in range(image.dimensions[1])]
    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            result[i][j] = 255 - int(image.matrix[i][j])
    result = Image(name=image.name +'_negative',matrix=result, dimensions=image.dimensions)
    return result


def translation(image:Image, move:int , name_extention:str='_translation'):
    result = [[0 for column in range(image.dimensions[0])] for row in range(image.dimensions[1])]
    print('Dimensions: '+str(image.dimensions), str([len(image.matrix[0]),len(image.matrix)])+'\n'+'move: '+ str(move))
    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            if ((i + move + 1) <= image.dimensions[0] and ((j + move + 1) <= image.dimensions[1])):
                try:
                    result[i + move][j + move] = image.matrix[i][j]
                except(IndexError):
                    print(i + move, j + move)
    result = Image(name=image.name +name_extention ,matrix=result, dimensions=image.dimensions)
    return result

# >>>>>>>>>>>>>>>>>
def translation2(image:Image, move:int , name_extention:str='_translation'):
    result = [[0 for column in range(image.dimensions[0])] for row in range(image.dimensions[1])]
    print('Dimensions: '+str(image.dimensions), str([len(image.matrix[0]),len(image.matrix)])+'\n'+'move: '+ str(move))
    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            if ((i + move + 1) <= len(result) and ((j + move + 1) <= len(result[0]))):
                    result[i + move][j + move] = image.matrix[i][j]
    result = Image(name=image.name +name_extention ,matrix=result, dimensions=[len(result), len(result[0])])
    return result

def histogram(image:Image):
    intensities = [0 for row in range(255)]
    probability = [0 for row in range(255)]
    cumulative_probability = [0 for row in range(255)]
    result = [[0 for row in range(image.dimensions[0])] for column in range(image.dimensions[1])]
    # building the intensity array (un-normalized histogram).
    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            x = int(image.matrix[i][j])
            intensities[x] = intensities[x] + 1
    # Finding the probability of having the intensity in the whole image
    for i in range(255):
        intensity = int(intensities[i])
        probability[i] = float(intensity / ((image.dimensions[0] * image.dimensions[1]) - 1))
    for i in range(255):
        cumulative_probability[i] = cumulative_probability[i - 1] + probability[i]
    # Equalizing the image
    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            pixel_intensity = int(image.matrix[i][j])
            result[i][j] = int(float(cumulative_probability[pixel_intensity]) * 255)
    result = Image(name=image.name +'_histequal',matrix=result, dimensions=image.dimensions)
    return result

# >>>>>>>>>>>>>
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
def create_matrix(dimensions:list)->list:
    print('creating new list: ' + str(dimensions))
    return [[0 for column in range(dimensions[0])] for row in range(dimensions[1])]

def copy_list(copy_from:list, copy_to:list)->list:
    len_from_row = len(copy_from)
    len_from_column= len(copy_from[0])
    print('column: ' + str(len_from_column), 'row: '+ str(len_from_row))
    for i in range(len_from_row):
        for j in range(len_from_column):
            try:
                copy_to[i][j] = copy_from[i][j]
            except(IndexError):
                print(i, j)
    return copy_to


def increase_dimensions(image:Image, new_dimensions:list, move:int)->Image:

    new_matrix = create_matrix(new_dimensions)
    copy_old_matrix_to_new_matrix = copy_list(image.matrix, new_matrix)
    print(new_dimensions)
    result = Image(name=image.name,matrix=copy_old_matrix_to_new_matrix, dimensions=new_dimensions)
    return translation(result, move, name_extention='')

def increase_dimensions2(image:Image, new_dimensions:list, move:int)->Image:

    new_matrix = create_matrix(new_dimensions)
    copy_old_matrix_to_new_matrix = copy_list(image.matrix, new_matrix)
    print(new_dimensions)
    result = Image(name=image.name,matrix=copy_old_matrix_to_new_matrix, dimensions=new_dimensions)
    return translation2(result, move, name_extention='')


def smooth(image:Image, kernel_size:int=KS_5 , sigma:int=2, K:int=1.67):
    dimensions=image.dimensions
    updated_image = increase_dimensions(image, [image.dimensions[0]+(kernel_size*2),image.dimensions[1]+(kernel_size*2)], kernel_size)
    result = [[0 for row in range(dimensions[0])] for column in range(dimensions[1])]
    kernel = [[0 for row in range(kernel_size)] for column in range(kernel_size)]
    for i in range(kernel_size):
        for j in range(kernel_size):
            kernel[i][j] = K * math.exp(-(math.pow(i - 2, 2) + math.pow(j - 2, 2)) / (2 * math.pow(sigma, 2)))
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            temp = 0
            for x in range(kernel_size):
                for y in range(kernel_size):
                    temp += float(updated_image.matrix[i + kernel_size + x - 2][j + kernel_size + y - 2]) * kernel[x][y]
            result[i][j] = int(temp / kernel_size**2)
    result = Image(name=image.name +'_smooth',matrix=result, dimensions=dimensions)
    return result


def unsharp(image:Image, image2:Image):
    result = Subtract.sub_two_matrices(image, image2, image.dimensions)
    result = Subtract.add_two_matrices(image, result, image.dimensions)
    min = INT_MAX
    max = INT_MIN
    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            if int(result.matrix[i][j]) < min:
                min = int(result.matrix[i][j])
    result_min = [[0 for row in range(image.dimensions[0])] for column in range(image.dimensions[1])]
    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            result_min[i][j] = result.matrix[i][j] - min

    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            if int(result_min[i][j]) > max:
                max = int(result_min[i][j])

    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            result.matrix[i][j] = 255 * (result_min[i][j] / max)
    
    return Image(name=image.name +'_unsharpmask',matrix=result.matrix, dimensions=image.dimensions)

def sharpening(image:Image):
    new_dimensions = [518, 518]
    this_image = increase_dimensions(image,new_dimensions,3)
    kernel = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    result = [[0 for row in range(image.dimensions[0])] for column in range(image.dimensions[1])]

    for i in range(image.dimensions[0]):
        for j in range(image.dimensions[1]):
            temp = 0
            for x in range(3):
                for y in range(3):
                    temp += float(this_image.matrix[i + 3 + x - 1][j + 3 + y - 1]) * kernel[x][y]
            result[i][j] = int(temp / 9)
    result = Subtract.sub_two_matrices(image, Image(name=image.name,dimensions=image.dimensions,matrix=result),name=image.name +'_sharpening')
    return result


def threshold(img, dimensions, threshold_point):
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if int(img[i][j]) > threshold_point:
                img[i][j] = 255
            else:
                img[i][j] = 0

    return img


def erosion(image:Image)->Image:
    result = [[0 for row in range(image.dimensions[0])] for column in range(image.dimensions[1])]
    newDimensions=[ image.dimensions[0]+2, image.dimensions[1]+2]

    current_image = increase_dimensions2(image,newDimensions , 1)
    condtion = True
    for i in range(0, image.dimensions[0]):
        for j in range(0, image.dimensions[1]):
            for x in range(0, 3):
                for y in range(0, 3):
                    if current_image.matrix[i+x][j+y] == 0:
                        condtion = False
            if condtion:
                result[i][j] = 255
            else:
                result[i][j] = 0
            condtion = True 
    return Image(name=image.name +'_erosion',matrix=result, dimensions=image.dimensions)

def dilation(image:Image):
    result = [[0 for row in range(image.dimensions[1])] for column in range(image.dimensions[0])]
    condtion = True
    for i in range(1, image.dimensions[0]-2):
        for j in range(1, image.dimensions[1]-2):
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if image.matrix[i-x][j-y] == 255:
                        condtion = False
            if condtion:
                result[i][j] = 0
            else:
                result[i][j] = 255
            condtion = True
    return Image(name=image.name +'_dilation',matrix=result, dimensions=image.dimensions)


def boundaryExtraction(image:Image):
    new_matrix = erosion(image)
    result = Subtract.sub_two_matrices(image, new_matrix, name=image.name +'_boundary')
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


