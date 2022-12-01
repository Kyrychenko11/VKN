import math
x=int(input("Введіть значення x: "))
y=math.fabs((math.tan(math.fabs(x)))+(math.tan(0.1)))

a=int(input("Введіть нижню границю: "))
b=int(input("Введіть верхню границю: "))
h=int(input("Введіть крок: "))
x=a
y=b
while x<b:
    y=math.fabs((math.tan(math.fabs(x)))+(math.tan(0.1)))
    print("x=%.1f y=%.3f"%(x,y)) 
    x=x+h
print(x)