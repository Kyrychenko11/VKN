s1=input("Введіть перший рядок ")
s2=input("Введіть другий рядок ")
s = list(set(s1) & set(s2))
print(s)