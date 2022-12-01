#1
number = int(input('N: '))
system = ('Венера', 'Земля', 'Нептун', 'Юпітер', 'Уран', 'Сатурн', 'Уран', 'Меркурій')
T=tuple(system)
list = []
for i in range(0, number, 1):
    list.append(T[i])
print(f"Список: {list}")
