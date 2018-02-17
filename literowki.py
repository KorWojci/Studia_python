# Autorzy:
# Katarzyna Wasilewska
# Kordian Wojciechowski
# Program sprawdza w podanym pliku tekstowym czy w słowach nie ma literówek
# jeżeli słowo ma literówkę (maksymalnie 2 błędy) zostaje wpisane do pliku
# o nazwie poprawione.txt w formacie slowo bazowe -> poprawione


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
    return (baza([slowo]) or baza(zmiana_1(slowo)) or baza(zmiana_2(slowo)) or [slowo])



def baza(slowa):
    # podzbior slow znanych w tekscie referencyjnym
    baza = []
    for w in slowa:
        if w in slownik:
            baza.append(w)
    return baza


def zmiana_1(slowo):
    # zmiana tylko jednej operacji, dodanie, usuniecie, zamiana, wstawianie, podzielenie"
    znaki = 'aąbcćdeęfghijklłmnoóprstuwzźż'
    podzial = []
    usuwanie = []
    przestawienie = []
    zamiana = []
    wstawianie = []
    for i in range(len(slowo)+1):
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
                zamiana.append(L + c + R[1:])

    for L, R in podzial:
        for c in znaki:
            wstawianie.append(L + c + R)

    return set(usuwanie + przestawienie + zamiana + wstawianie)

def zmiana_2(slowo):
    # uzyskanie wszystkich słów z 2 zmianami
    podwarianty = []
#    print('Zmiana 1')
#    print(zmiana_1(slowo))
    for w in zmiana_1(slowo):
        for s in zmiana_1(w):
            podwarianty.append(s)

    return set(podwarianty)

print('Podaj nazwe pliku w formacie plik.txt')
plik = input()

poprawione_slowa = []

file = open(plik, 'r').read().split()

for w in file:
    w2 = w.lower()
    s = popraw(w2)
    if s == w2:
        continue
    else:
        poprawione_slowa.append([w, '->', s])

print(poprawione_slowa)

file_2 = open('poprawione.txt', 'w')
for x in poprawione_slowa:
    linia = x[0] + ' ' + x[1] + ' ' + x[2] + '\n'
    print(linia)
    file_2.write(linia)
file_2.close()
#print('Poprawione słowa:')
#print(popraw(slowo))
