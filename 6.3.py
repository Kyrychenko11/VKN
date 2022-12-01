import math

def function_1(a, b, h):
    x = 0
    arr = [a, b, h]
    for i in range(a, b, h):
        x = math.fabs(math.tan(math.fabs(i) + 0.1))
    arr.append(x)
    return arr

def function_2(a, b, h):
   x = 0
   arr = [a, b, h]
   while a <= b:
       x = math.fabs(math.tan(math.fabs(a) + 0.1))
       a += h
   arr.append(x)
   return arr

lst = []
lst.append(function_1(1, 2, 3))
lst.append(function_2(4, 5, 6))

val = [1, 1]
for i in range(1):
    for j in range(len(lst[i])):
        val[0] *= lst[0][j]
        val[1] *= lst[1][j]
print(val)