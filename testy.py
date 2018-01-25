slowo = input()

podzial = []
for i in range(len(slowo)):
    podzial.append([slowo[:i], slowo[i:]])

print(podzial)