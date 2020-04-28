import math


def CC(I, R):
    C = [[0 for row in range(I.dimensions[1] - R.dimensions[1] + 1)] for column in
         range(I.dimensions[0] - R.dimensions[0] + 1)]
    K = R.size
    sumR, sumR2 = 0, 0

    for i in range(R.dimensions[0]):
        for j in range(R.dimensions[1]):
            sumR = sumR + R.matrix[i][j]
            sumR2 = sumR2 + math.pow(R.matrix[i][j], 2)
    nR = sumR / K
    SR = math.sqrt(sumR2 - K * math.pow(nR, 2))

    for r in range(I.dimensions[0] - R.dimensions[0]):
        for s in range(I.dimensions[1] - I.dimensions[1]):
            sumI, sumI2, sumIR = 0, 0, 0
            for i in range(R.dimensions[0] - 1):
                for j in range(R.dimensions[1] - 1):
                    aI = I.matrix[r + i][s + j]
                    aR = R.matrix[i][j]
                    sumI = sumI + aI
                    sumI2 = sumI2 + math.pow(aI, 2)
                    sumIR = sumIR + (aI * aR)
            nI = sumI / K
            C[r][s] = (sumIR - (K * nI * nR)) / (math.sqrt(sumI2 - K * math.pow(nI, 2)) * SR)

    return C
