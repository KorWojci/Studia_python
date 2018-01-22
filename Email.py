import re

p = re.compile(r"[\w!#$%&’*+/=\-?^_`{|}~]+(\.[\w!#$%&’*+/=\-?^_`{|}~]+)*@[\w-]+(\.[\w]+)*(\.[a-z]{2,})")

print('Podaj linie do analizy:')
l = input()
adresy = []

m = p.search(l)

i = p.finditer(l)

for m in i:
    adresy.append(m.group())

adresy.sort()
print(adresy)
