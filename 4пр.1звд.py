import math

x = float(input("x = "))


def fun(x1):
    return ((math.sin(x1) - math.log10(x1)) / math.sqrt(x1 * 7)) + math.pow(x1 + 4, 2 * x1 - 8)

print(fun(x))
