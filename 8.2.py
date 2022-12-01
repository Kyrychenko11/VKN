import random
import math
from tkinter import Y
import numpy as np
from numpy import*
m=int(input("Введіть M "))
n=int(input("Введіть N "))
masiv1=np.zeros((m,n))
masiv2=np.zeros((m,n))
for i in range(m):
    for j in range (n):
        masiv1[i][j]=random.randint(1,50)
        masiv2[i][j]=random.randint(1,50)

print("Масив А")
print(masiv1)
print("Масив В")
print(masiv2)
x=masiv1[i][j]+masiv2[i][j]
y=masiv1[i][j]-masiv2[i][j]
c=masiv1[i][j]*masiv2[i][j]
print("Сума ",x)
print("Різниця ",y)
print("Добуток ",c)