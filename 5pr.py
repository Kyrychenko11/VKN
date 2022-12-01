import math
x = float(input("Введіть значення аргументу функції x: "))
def f1(x1):
    rez=((2.27*math.e**4*x1+1)+3)
    return(rez)
def f2(x2):
    rez=(0.64*x2**x2+0.1)
    return(rez)
def f3(x3):
    rez=math.log10(math.fabs(x3-math.e**x3))
    return(rez)
y=0.0
if x > 7:
    y = f1(x)
elif 0.5 < x:
    y = f2(x)
else:
    y = f3(x)
print(y)