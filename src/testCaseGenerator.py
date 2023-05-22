import random

from projectTypes import *


minValue: int = 1
maxValue: int = 20


def generateTestCaseA():
    for i in range(50):
        filename = f"TestCase{i + 1}.txt"

        with open(f"../test/A/{filename}", "w") as file:
            relationOrder = 5
            file.write(str(relationOrder) + "\n")

            coefficients = [Decimal(random.randint(minValue, maxValue)) for _ in range(relationOrder + 1)]
            file.write("\n".join(str(coefficient) for coefficient in coefficients) + "\n")

            baseValues = [Decimal(random.randint(minValue, maxValue)) for _ in range(relationOrder)]
            file.write("\n".join(str(value) for value in baseValues))


def generateTestCaseB():
    orders = [20, 15, 10, 5, 2]
    for i in range(50):
        filename = f"TestCase{i + 1}.txt"

        with open(f"../test/B/{filename}", "w") as file:
            relationOrder = orders[i // 10]
            file.write(str(relationOrder) + "\n")

            coefficients = [Decimal(random.randint(minValue, maxValue)) for _ in range(relationOrder + 1)]
            file.write("\n".join(str(coefficient) for coefficient in coefficients) + "\n")

            baseValues = [Decimal(random.randint(minValue, maxValue)) for _ in range(relationOrder)]
            file.write("\n".join(str(value) for value in baseValues))


if __name__ == "__main__":
    generateTestCaseA()
