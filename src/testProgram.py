import os
import csv
import dnc
import dp
import time
import tracemalloc

from inputHandler import getRecursiveFunctionFile
from projectTypes import *
from utilities import printUtil


def testA(coefficients: Coefficients, baseValues: BaseValues):
    listOfN = [250, 500, 750, 1000, 1500, 2000]

    dpData = []
    for n in listOfN:
        print(f"N: {n}")
        startTime = time.time()
        tracemalloc.start()

        dp.solve(n, coefficients, baseValues)

        duration = 1000 * (time.time() - startTime)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        printUtil(duration, peak)
        dpData.append([n, duration, peak])

    dncData = []
    for n in listOfN:
        print(f"N: {n}")
        startTime = time.time()
        tracemalloc.start()

        dnc.solve(n, coefficients, baseValues)

        duration = 1000 * (time.time() - startTime)
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        printUtil(duration, peak)
        dncData.append([n, duration, peak])

    return dpData, dncData


def testB(coefficients: Coefficients, baseValues: BaseValues):
    order = len(baseValues)
    n = 1000

    # DP
    startTime = time.time()
    tracemalloc.start()

    dp.solve(n, coefficients, baseValues)

    duration = 1000 * (time.time() - startTime)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    printUtil(duration, peak)
    dpData = [order, duration, peak]

    # DNC
    startTime = time.time()
    tracemalloc.start()

    dnc.solve(n, coefficients, baseValues)

    duration = 1000 * (time.time() - startTime)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    printUtil(duration, peak)
    dncData = [order, duration, peak]

    return dpData, dncData


def main():
    testType = "A"  # Don't forget change this value for different test type

    dpData = []
    dncData = []

    if testType == "A":
        dpData.append(["N", "Duration", "Peak Memory"])
        dncData.append(["N", "Duration", "Peak Memory"])
    elif testType == "B":
        dpData.append(["Order", "Duration", "Peak Memory"])
        dncData.append(["Order", "Duration", "Peak Memory"])

    for filename in os.listdir(f"../test/{testType}"):
        print(f"File: {filename}")

        coefficients, baseValues = getRecursiveFunctionFile(f"../test/{testType}/{filename}")
        if testType == "A":
            datas = testA(coefficients, baseValues)

            for data in datas[0]:
                dpData.append(data)

            for data in datas[1]:
                dncData.append(data)

        elif testType == "B":
            datas = testB(coefficients, baseValues)
            dpData.append(datas[0])
            dncData.append(datas[1])

        else:
            # testC(coefficients, baseValues)
            pass

    with open(f"../data/{testType}_DP.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(dpData)

    with open(f"../data/{testType}_DNC.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(dncData)


if __name__ == "__main__":
    main()
