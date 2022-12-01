import math
a=int(input("Введіть значення a "))
b=int(input("Введіть значення b "))
h=int(input("Введіть значення h "))

def fun(a, b, h):
    arr = [a, b, h]
    for i in range(a, b, h):
        x = math.fabs(math.tan(math.fabs(i) + 0.1))
    arr.append(x)
    return arr
