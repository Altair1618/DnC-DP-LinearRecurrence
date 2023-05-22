from projectTypes import *


def solve(n: int, coefficient: Coefficients, baseValue: BaseValues) -> Decimal:
    order: int = len(baseValue)

    if n < order:
        return baseValue[n]

    dp: List[Decimal] = []
    for i in range(n + 1):
        if i < order:
            dp.append(baseValue[i])
        else:
            value: Decimal = Decimal(0)

            for j in range(1, len(coefficient)):
                value += dp[i - j] * coefficient[j]
                value %= int(1e9)

            value += coefficient[0]
            value %= int(1e9)

            dp.append(value)

    return dp[n]


def solveAll(n: int, coefficient: Coefficients, baseValue: BaseValues) -> List[Decimal]:
    order: int = len(baseValue)

    if n < order:
        return baseValue[:n]

    dp: List[Decimal] = []
    for i in range(n + 1):
        if i < order:
            dp.append(baseValue[i])
        else:
            value: Decimal = Decimal(0)
            for j in range(1, len(coefficient)):
                value += dp[i - j] * coefficient[j]
            value += coefficient[0]
            dp.append(value)

    return dp
