import math

import utility


def CC(img, template):
    c = [[0 for row in range(img.dimensions[1] - template.dimensions[1] + 1)] for column in
         range(img.dimensions[0] - template.dimensions[0] + 1)]
    k = template.size
    sumR = 0
    sumR2 = 0
    for i in range(42):
        for j in range(45):
            sumR += (template.matrix[i][j])
            sumR2 += ((template.matrix[i][j])) ** 2

    nR = sumR / k
    sR = math.sqrt(sumR2 - k * math.pow(nR, 2))

    # step 2
    for r in range(img.dimensions[0] - template.dimensions[0]):
        for s in range(img.dimensions[1] - template.dimensions[1]):
            sumI = 0
            sumI2 = 0
            sumIR = 0
            for i in range(template.dimensions[0] - 1):
                for j in range(template.dimensions[1] - 1):
                    aI = (img.matrix[r + i][s + j])
                    aR = (template.matrix[i][j])
                    sumI += aI
                    sumI2 += math.pow(aI, 2)
                    sumIR += aI * aR
            nI = (sumI / k)
            c[r][s] = (sumIR - (k * nI * nR)) / (math.sqrt((sumI2 - k) * (math.pow(nI, 2))) * sR)
    return c