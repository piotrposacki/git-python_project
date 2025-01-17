import os
import funkcje

szukaj = "PLP79729"
os.chdir("C:\\logs")

for plik in os.listdir():
    funkcje.naglowek(plik)
    with open(plik) as current:
        funkcje.znajdz(current, szukaj)
