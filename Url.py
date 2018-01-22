import urllib.request
import re

adresy = []
adresy_fin = []

print('Podaj strone do przeskanowania(http://www.nazwa_strony.domena:')
adres = input()

strona = urllib.request.urlopen(adres)

html = strona.read()

i = re.findall(r'"((http)s?://.*?)"', str(html))

for m in i:
    adresy.append(m[0])

[adresy_fin.append(x) for x in adresy if x not in adresy_fin]
for adres in adresy_fin:
    print(adres)
