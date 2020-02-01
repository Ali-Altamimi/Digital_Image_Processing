import numpy as np

x = 512
y = 512

lena = "sources\lena.raw"
lena_edit = "sources\lena_edit.raw"


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
    return t


def write_raw_files(matrix, filename):
    f = open(filename + '.raw', 'wb')

    casted_matrix = np.matrix(matrix).astype('uint8')

    f.write(casted_matrix)
    f.close()


def subtrac_two_imgs(img1, img2):
    result = [[0 for row in range(x)] for column in range(y)]
    for i in range(x):
        for j in range(y):
            result[i][j] = int(img1[i][j]) - int(img2[i][j])

    return result


def inverse(img1):
    result = [[0 for row in range(x)] for column in range(y)]
    for i in range(x):
        for j in range(y):
            result[i][j] = 255 - int(img1[i][j])

    return result


def translation(img, move):
    result = [[0 for row in range(x)] for column in range(y)]
    for i in range(x):
        for j in range(y):
            if ((i + move + 1) <= x and ((j + move + 1) <= y)):
                result[i + move][j + move] = img[i][j]
    return result


img1 = read_raw_files(lena)
img2 = read_raw_files(lena_edit)
result = subtrac_two_imgs(img1, img2)
write_raw_files(result, "lena_subtraction")

inverse_img = inverse(img1)
write_raw_files(inverse_img, "lena_negative")

trans_img = translation(img1, 5)
write_raw_files(trans_img, "lena_translation")
