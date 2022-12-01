import math


def square(r, R, h):
    # Площа 
    return math.pi * (r ** 2 + R ** 2 + r * R) + math.pi * h * math.sqrt((R - r) ** 2 + h ** 2)


def volume(r, R, h):
    # Об'єм 
    return math.pi * h * (r ** 2 + r * R + R ** 2) / 3


if __name__ == '__main__':
    print(square(5, 6, 7))
    print(volume(5, 6, 7))