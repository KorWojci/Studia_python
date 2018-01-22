import re
from collections import Counter

def slowa(text):
    return re.findall(r'\w+', text.lower())

slownik = Counter(slowa(open('tekst.txt').read()))

def pstwo(slowo):
    n = sum(slownik.values())
    print('P-stwo wystąpienia słowa')
    return slownik[slowo] / n

print(pstwo('kordian'))