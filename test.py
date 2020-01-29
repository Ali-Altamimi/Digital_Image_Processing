import binascii
import numpy as np
import math
x = 512
y = 512

lena = "lena.raw"
lena_edit = "lena_edit.raw"


def read_raw_files(file_name):
    t = [[0 for row in range(x)] for column in range(y)]
    with open(file_name, "r+b") as binary_file:
        # Read the whole file at once
        data = binary_file.read()
        string_data = " ".join(map(str, data))
        list_data = string_data.split(" ")
        counter = 0
        for i in range(x):
            for j in range(y):
                t[i][j] = list_data[counter]
                counter = counter + 1
    return np.array(t, dtype="uint8")


def write_raw_files(matrix, filename):
    # w = np.matrix(two_d_array)
    f = open(filename + '.raw', 'wb')

    z = matrix.astype('uint8')

    f.write(z)
    f.close()


def subtrac_two_imgs(img1, img2):
    result = [[0 for row in range(x)] for column in range(y)]
    for i in range(x):
        for j in range(y):
            result[i][j] = int(img1[i][j]) - int(img2[i][j])

    return np.matrix(result)


img1 = read_raw_files(lena)
img2 = read_raw_files(lena_edit)
result = subtrac_two_imgs(img1, img2)
write_raw_files(result, "sub_img")


def inverse(img1):
    result = [[0 for row in range(x)] for column in range(y)]
    for i in range(x):
        for j in range(y):
            result[i][j] = 255 - int(img1[i][j])

    return np.matrix(result)


inverse_img = inverse(img1)
write_raw_files(inverse_img, "inv_img")

write_raw_files(img1, "test_lena")