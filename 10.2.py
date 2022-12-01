import os
import shutil
print(os.listdir("C:\\Users\\tanya\\10.2"))
anames=[]
bnames=[]
for i in os.listdir("C:\\Users\\tanya\\10.2"):
    if i[0] == "a":
        anames.append(i)
    elif i[0] == "b":
        bnames.append(i)
os.mkdir("C:\\Users\\tanya\\10.2\\A_NAMES")
os.mkdir("C:\\Users\\tanya\\10.2\\B_NAMES")
for i in anames:
    pardir = "C:\\Users\\tanya\\10.2\\"+i
    shutil.move(pardir, "C:\\Users\\tanya\\10.2\\A_NAMES")
for i in bnames:
    pardir = "C:\\Users\\tanya\\10.2\\"+i
    shutil.move(pardir,"C:\\Users\\tanya\\10.2\\B_NAMES")