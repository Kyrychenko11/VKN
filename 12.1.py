import math


def square(a, b, c):
    # Корені квадратного равняння
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def biquadratic(a, b, c):
    # Корені біквадратного равняння
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1 ** 2, x2 ** 2
    elif d == 0:
        x = -b / (2 * a)
        return x ** 2
    else:
        return None


if __name__ == '__main__':
    print(square(-5, 3, -2))
    print(biquadratic(1, 2, 3))