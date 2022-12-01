import  math
area=(0)
t={'t1':'3 4 5','t2':'5 6 7', 't3':'7 8 9'}
for key, value in t.items():
    temp=list(map(int, value.split()))
    if sum(temp)/2 > area:
        area=sum(temp)/2
        name=key
print(area,name)