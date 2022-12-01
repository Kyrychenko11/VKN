import math 
x = float(input("x = Введіть число"))
y = float(input("y = Введіть число"))
S = math.cos(x)*math.tan(y)+math.log(math.e**x+4, 5)+1/math.sqrt(math.fabs(x)+0.1)
print(f"S = {S}")