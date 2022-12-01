ryad=input("Введіть рядок слів,розділених пробілами ")
slova = ryad.split(" ")
max_lenght = slova[0]
for i in range(len(slova)):
    if slova[i]>max_lenght:
        max_lenght=slova[i]
print("Найдовше слово складається з ", len(max_lenght), "символів,","це слово:", max_lenght)