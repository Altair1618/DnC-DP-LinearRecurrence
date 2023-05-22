import time
import tracemalloc

import dp
import dnc

from inputHandler import *
from utilities import printUtil


if __name__ == "__main__":
    coefficients, baseValue = getRecursiveFunction()
    x: int = int(input("Enter the x value: "))

    print("\nDP:")
    startTime = time.time()
    tracemalloc.start()

    print(dp.solve(x, coefficients, baseValue))

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    printUtil(1000 * (time.time() - startTime), peak)

    print("\nDNC:")
    startTime = time.time()
    tracemalloc.start()

    print(dnc.solve(x, coefficients, baseValue))

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    printUtil(1000 * (time.time() - startTime), peak)
