import re
from collections import Counter

def slowa(text):
    return re.findall(r'\w+', text.lower())

slownik = Counter(slowa(open('tekst.txt', encoding='utf-8').read()))

def pstwo(slowo):
    # prawdopodobienstwo wystapienia slowa wedlug tekstu referencyjnego
    n = sum(slownik.values())
    return slownik[slowo] / n

def popraw(word):
    # najbardziej prawdopodobne dopasowanie slowa
    return max(propozycje(word), key=pstwo)

def propozycje(slowo):
    # możliwe propozycje poprawionego słowa
    print('baza')
    print(baza([slowo]))
    print('zmiana_1')
    print(baza(zmiana_1(slowo)))
    print('zmiana_2')
    print(baza(edits2(slowo)))
    print('slowo')
    print([slowo])
    return (baza([slowo]) or baza(zmiana_1(slowo)) or baza(zmiana_2(slowo)) or [slowo])


def baza(slowa):
    # podzbior slow znanych w tekscie referencyjnym
    baza = []
    for w in slowa:
        if w in slownik:
            baza.append(w)
    return baza


def zmiana_1(slowo):
    "zmiana tylko jednej operacji, dodanie, usuniecie, zamiana"
    znaki = 'aąbcćdeęfghijklłmnoóprstuwzźż'
    podzial = []
    usuwanie = []
    przestawienie = []
    zamiana = []
    wstawianie = []
    for i in range(len(slowo)):
        podzial.append([slowo[:i], slowo[i:]])

    for L, R in podzial:
        if R is not None:
            usuwanie.append(L + R[1:])

    for L, R in podzial:
        if len(R) > 1:
            przestawienie.append(L+ R[1] + R[0] + R[2:])

    for L, R in podzial:
        if R is not None:
            for c in znaki:
                zamiana.append(L + c + R)

    for L, R in podzial:
        for c in znaki:
            wstawianie.append(L + c + R)

    return set(usuwanie + przestawienie + zamiana + wstawianie)

def zmiana_2(slowo):
    "zmiany 2 operacji."
    for e1 in zmiana_1(slowo):
        for e2 in zmiana_1(slowo):
            return e2
#    return (e2 for e1 in zmiana_1(slowo) for e2 in zmiana_1(e1))

print('Podaj slowo do poprawy:')
slowo = input()
print('Propozycje:')
print(propozycje(slowo))