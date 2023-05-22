from projectTypes import *


def matrixMultiply(mat1: DecimalMatrix, mat2: DecimalMatrix) -> DecimalMatrix:
    row1, col1 = len(mat1), len(mat1[0])
    row2, col2 = len(mat2), len(mat2[0])

    result = [[Decimal(0) for _ in range(col2)] for _ in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += mat1[i][k] * mat2[k][j]
                result[i][j] %= int(1e9)

    return result


def getExponentMatrix(matrix: DecimalMatrix, power: int) -> DecimalMatrix:
    if power == 1:
        return matrix
    else:
        halfPowerMatrix: DecimalMatrix = getExponentMatrix(matrix, power // 2)
        if power % 2 == 0:
            return matrixMultiply(halfPowerMatrix, halfPowerMatrix)
        else:
            return matrixMultiply(matrixMultiply(halfPowerMatrix, halfPowerMatrix), matrix)


def solve(n: int, coefficient: Coefficients, baseValue: BaseValues) -> Decimal:
    order: int = len(baseValue)

    if n < order:
        return baseValue[n]

    baseMatrix: DecimalMatrix = []
    for i in range(order - 1, -1, -1):
        baseMatrix.append([baseValue[i]])
    baseMatrix.append([coefficient[0]])

    identityMatrix: DecimalMatrix = []
    for i in range(order + 1):
        if i == 0:
            identityMatrix.append(coefficient[1:] + [Decimal(1)])
        elif i == order:
            identityMatrix.append([Decimal(0)] * order + [Decimal(1)])
        else:
            identityMatrix.append([Decimal(0)] * (order + 1))
            identityMatrix[i][i - 1] = Decimal(1)

    resultMatrix: DecimalMatrix = matrixMultiply(getExponentMatrix(identityMatrix, n - order + 1), baseMatrix)
    return resultMatrix[0][0] % int(1e9)
