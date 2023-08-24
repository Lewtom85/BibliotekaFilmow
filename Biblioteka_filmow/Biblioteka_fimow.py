import random
from datetime import datetime

class BibliotekaFilmow:
    def __init__(self, tytul, rok_wydania, gatunek, liczba_odtworzen=0):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzen = liczba_odtworzen

    def play(self, step=1):
        self.liczba_odtworzen += step

    def __str__(self):
        return f'{self.tytul} ({self.rok_wydania})'

class BibliotekaSeriali(BibliotekaFilmow):
    def __init__(self, tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu, liczba_odtworzen=0):
        super().__init__(tytul, rok_wydania, gatunek, liczba_odtworzen)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
    
    def __str__(self):
        return f'{self.tytul} S{self.numer_sezonu:02d} E{self.numer_odcinka:02d}'

def get_movies(biblioteka):
    movies = [item for item in biblioteka if isinstance(item, BibliotekaFilmow)]
    movies.sort(key=lambda x: x.tytul)
    return movies

def get_series(biblioteka):
    series = [item for item in biblioteka if isinstance(item, BibliotekaSeriali)]
    series.sort(key=lambda x: x.tytul)
    return series

def search(biblioteka, tytul):
    results = []
    for item in biblioteka:
        if tytul.lower() in item.tytul.lower():
            results.append(item)
    return results

def generate_views(item):
    item.play(random.randint(1, 100))

def run_generate_views(biblioteka, times=10):
    for _ in range(times):
        random_item = random.choice(biblioteka)
        generate_views(random_item)

def top_titles(biblioteka, n):
    biblioteka.sort(key=lambda x: x.liczba_odtworzen, reverse=True)
    return biblioteka[:n]


biblioteka = []

Wladca_Pierscieni_Druzyna_Pierscienia = BibliotekaFilmow("Wladca Pierscieni: Druzyna Pierscienia", 2001, "Akcja")
Wladca_Pierscieni_Dwie_Wieze = BibliotekaFilmow("Wladca Pierscieni: Dwie Wieze", 2002, "Akcja")
Egzorcysta = BibliotekaFilmow("Egzorcysta", 1973, "Horror")
Rocky = BibliotekaFilmow("Rocky", 1976, "Sport")
Przeminelo_z_wiatrem = BibliotekaFilmow("Przeminelo z Wiatrem", 1939, "Dramat")

Wiedzmin = BibliotekaSeriali("Wiedzmin", 2019, "Fantastyka", 1, 1)
Przyjaciele = BibliotekaSeriali("Przyjaciele", 1994, "Komedia", 4, 12)
Colombo = BibliotekaSeriali("Colombo", 1971, "Kryminal", 3, 2)

biblioteka.extend([Wladca_Pierscieni_Druzyna_Pierscienia, Wladca_Pierscieni_Dwie_Wieze, Egzorcysta, Rocky, Przeminelo_z_wiatrem, Wiedzmin, Przyjaciele, Colombo])

print("Biblioteka filmow")

while True:
    print("\nDodaj nowy element do biblioteki:")
    tytul = input("Tytul: ")
    rok_wydania = int(input("Rok wydania: "))
    gatunek = input("Gatunek: ")

    typ = input("Czy to film czy serial (film/serial): ")
    if typ == "film":
        nowy_element = BibliotekaFilmow(tytul, rok_wydania, gatunek)
    elif typ == "serial":
        numer_odcinka = int(input("Numer odcinka: "))
        numer_sezonu = int(input("Numer sezonu: "))
        nowy_element = BibliotekaSeriali(tytul, rok_wydania, gatunek, numer_odcinka, numer_sezonu)
    
    biblioteka.append(nowy_element)

    kontynuuj = input("Czy chcesz dodac kolejny element do biblioteki? (tak/nie): ")
    if kontynuuj.lower() != "tak":
        break

run_generate_views(biblioteka)

current_date = datetime.now().strftime("%d.%m.%Y")
print("Biblioteka filmow")
print("Najpopularniejsze filmy i seriale dnia", current_date)

top_items = top_titles(biblioteka, 3)
for idx, item in enumerate(top_items, 1):
    print(f"{idx}. {item.tytul} - {item.liczba_odtworzen} odtworzenia")
