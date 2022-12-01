import math
A=float(input("введіть перше число:  "))
B=float(input("введіть друге число:  "))
C=float(input("введіть третє число:  "))
x=float(input("Введіть число x: "))
y=float(input("Введіть число y: "))
M=x,y
if B>A and C>A:
   print('А-найменше')
elif B>C and A>C:
   print('С-найменше')
elif C>B and A>B: 
   print('В-найменше')