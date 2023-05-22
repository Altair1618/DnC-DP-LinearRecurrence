import sys

from projectTypes import *


def getRecursiveFunction() -> Tuple[Coefficients, BaseValues]:
    relationOrder: int = int(input("Enter the order of the recurrence relation: "))

    coefficients: Coefficients = [Decimal(input("Enter the constant coefficient: "))]

    for i in range(relationOrder):
        coefficients.append(Decimal(input(f"Enter the coefficient of f(x - {i + 1}): ")))

    baseValues: BaseValues = []
    for i in range(relationOrder):
        baseValues.append(Decimal(input(f"Enter the value of f({i}): ")))

    return coefficients, baseValues


def getRecursiveFunctionFile(filepath: str) -> Tuple[Coefficients, BaseValues]:
    sys.stdin = open(filepath)
    relationOrder: int = int(input())

    coefficients: Coefficients = [Decimal(input())]

    for i in range(relationOrder):
        coefficients.append(Decimal(input()))

    baseValues: BaseValues = []
    for i in range(relationOrder):
        baseValues.append(Decimal(input()))

    return coefficients, baseValues


def getFibonacciFunction() -> Tuple[Coefficients, BaseValues]:
    coefficient: Coefficients = [Decimal(0), Decimal(1), Decimal(1)]
    baseValue: BaseValues = [Decimal(0), Decimal(1)]

    return coefficient, baseValue


if __name__ == "__main__":
    getRecursiveFunction()
