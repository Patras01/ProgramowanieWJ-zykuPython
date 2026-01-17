import sys

def czytaj_linie(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as f:
            for linia in f:
                yield linia.strip()
    except FileNotFoundError:
        print("Błąd: Plik log.txt nie istnieje!")

def filtruj_logi(gen, poziom):
    for linia in gen:
        if poziom in linia:
            yield linia

def licz_statystyki(gen):
    stat = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for linia in gen:
        for klucz in stat:
            if klucz in linia:
                stat[klucz] += 1
    return stat


plik = "file.log"

generator_bazowy = czytaj_linie(plik)

wynik = licz_statystyki(generator_bazowy)

print("Statystyki logów:")
print(wynik)

print("-" * 30)
gen_pamięć = czytaj_linie(plik)
print(f"Rozmiar generatora: {sys.getsizeof(gen_pamięć)} bajtów")