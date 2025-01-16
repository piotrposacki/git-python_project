import os
import funkcje.py

szukaj = "PLP79729"
os.chdir("C:\\logs")

for file in os.listdir():
    with open(file) as current:
        naglowek(file)
        znajdz(file, szukaj)
