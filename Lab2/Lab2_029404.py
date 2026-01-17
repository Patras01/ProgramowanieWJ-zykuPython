
wejscie = input("Podaj liczby (oddzielone spacją): ")

if not wejscie.strip():
    print("Nie wprowadzono żadnych danych.")
else:
    lista_str = wejscie.split()
    liczby = [int(x) for x in lista_str]

    liczba_wszystkich = len(liczby)
    suma = sum(liczby)
    srednia = suma / liczba_wszystkich

    dodatnie = 0
    ujemne = 0
    zera = 0

    for n in liczby:
        if n > 0:
            dodatnie += 1
        elif n < 0:
            ujemne += 1
        else:
            zera += 1

    najwieksza = max(liczby)
    najmniejsza = min(liczby)

    print(f"Liczb wprowadzonych: {liczba_wszystkich}")
    print(f"Suma: {suma}")
    print(f"Średnia: {srednia}")
    print(f"Dodatnie: {dodatnie}, Ujemne: {ujemne}, Zera: {zera}")
    print(f"Największa: {najwieksza}")
    print(f"Najmniejsza: {najmniejsza}")