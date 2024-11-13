import pygame

from quiz_ntfs import wyswietl_quiz


def wyswietl_labirynt():
    pozycja = (6, 4)
    pionowe_krawedzie = [
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    ]
    poziome_krawedzie = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    podpowiedzi = [
        ((1, 1), [
            "W systemie plików NTFS istnieje możliwość, aby więcej niż jeden",
            "użytkownik lub proces miał dostęp do tego samego pliku w tym",
            "samym czasie, jednak zależy to od kilku czynników, takich jak rodzaj",
            "dostępu (odczyt, zapis) oraz konkretne operacje wykonywane na pliku."
        ]),
        ((6, 1), [
            "W systemie plików atrybuty plików to informacje, które przechowują",
            "różne cechy i właściwości plików oraz katalogów. Są one przechowywane",
            "razem z danymi pliku i wykorzystywane do zarządzania plikami oraz",
            "ich właściwościami. Atrybuty plików w NTFS obejmują między innymi",
            "takie informacje jak dane o nazwie pliku, uprawnieniach dostępu,",
            "dacie modyfikacji, rozmiarze pliku, czy też zaszyfrowanych danych."
        ]),
        ((11, 1), [
            "Na liście uprawnień ACL znajduje się zestaw wpisów kontroli ACE.",
            "W każdym wpisie zawarta jest informacja o użytkowniku oraz jego",
            "uprawnieniach podstawowych (odczyt, zapis, modyfikacja, wyświetlenie",
            "zawartości folderu, pełna kontrola) i uprawnieniach specjalnych.",
            "Uprawnienia blokujące dostęp są odczytywane przed uprawnieniami",
            "umożliwiającymi dostęp. Uprawnienia są dostępne zarówno dla folderów,",
            "jak i dla plików."
        ]),
        ((1, 7), [
            "Uprawnienia dla folderu są domyślnie dziedziczone przez pliki i podfoldery,",
            "ale można to zmieniać. Dziedziczenie uprawnień w systemie NTFS jest",
            "jednym z podstawowych mechanizmów ułatwiających zarządzanie",
            "dostępem do zasobów w systemie operacyjnym Windows.",
            "Uprawnienia dziedziczone są odczytywane po uprawnieniach",
            "niedziedziczonych.",
            "NTFS to standardowy system plików systemu Windows NT i następców."
        ]),
        ((6, 7), [
            "Oprócz uprawnień podstawowych, w NTFS istnieją również uprawnienia",
            "zaawansowane, które dzielą uprawnienia podstawowye na kilka",
            "o węższym zakresie. Uprawnienia zaawansowane „mapują” na",
            "ustawienia podstawowe. Oznacza to, że wybranie np. uprawnienia",
            "podstawowego „Read” będzie równoznaczne z wyborem 4 uprawnień",
            "zaawansowanych – List folder / read data, Read attributes,",
            "Read extended attributes, Read permissions."
        ]),
        ((11, 7), [
            "Typy uprawnień dostępne w ramach ACL w systemie NTFS to:",
            "pełna kontrola, modyfikacja, odczyt i wykonanie, wyświetlenie zawartości",
            "(jedynie dla folderów), odczyt oraz zapis.",
            "- odczyt pozwala odczytać zawartość pliku/folderu",
            "- zapis pozwala tworzyć pliki/foldery i dodawać do nich dane",
            "- odczyt i wykonanie pozwala odczytać i zapisać zawartość pliku oraz",
            "uruchomić jego zawartość",
            "- modyfikacja zawiera dostęp do odczytu i wykonywania pliku",
            "oraz jego usuwania",
            "- pełna kontrola daje dodatkowo dostęp do usuwania podfolderów i zmiany",
            "uprawnień pliku oraz jego właściciela"
       ]),
    ]

    def czy_podpowiedz():
        for polozenie, tresc in podpowiedzi:
            if pozycja == polozenie:
                return tresc
        return ""

    tekst_podpowiedzi = ""

    little_font = pygame.font.SysFont('Arial', 16)
    big_font = pygame.font.SysFont('Arial', 24)

    window = pygame.display.set_mode((600, 500))
    pygame.display.set_caption('Labirynt NTFS')
    running = True

    przycisk = pygame.Rect(200, 400, 200, 50)
    tekst_przycisk = "Przejdź do quizu"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    if pionowe_krawedzie[pozycja[1] - 1][pozycja[0] - 1] == 0:
                        pozycja = pozycja[0] - 1, pozycja[1]
                        tekst_podpowiedzi = czy_podpowiedz()
                elif keys[pygame.K_RIGHT]:
                    if pionowe_krawedzie[pozycja[1] - 1][pozycja[0]] == 0:
                        pozycja = pozycja[0] + 1, pozycja[1]
                        tekst_podpowiedzi = czy_podpowiedz()
                elif keys[pygame.K_UP]:
                    if poziome_krawedzie[pozycja[1] - 1][pozycja[0] - 1] == 0:
                        pozycja = pozycja[0], pozycja[1] - 1
                        tekst_podpowiedzi = czy_podpowiedz()
                elif keys[pygame.K_DOWN]:
                    if poziome_krawedzie[pozycja[1]][pozycja[0] - 1] == 0:
                        pozycja = pozycja[0], pozycja[1] + 1
                        tekst_podpowiedzi = czy_podpowiedz()
            if event.type == pygame.MOUSEBUTTONUP:
                pozycja_myszki = pygame.mouse.get_pos()
                if przycisk.collidepoint(pozycja_myszki):
                    running = False
                    wyswietl_quiz()

        window.fill(pygame.color.Color("white"))

        pygame.draw.rect(window, pygame.color.Color("green"), (50 * pozycja[0] - 12, 50 * pozycja[1] - 12, 25, 25))
        pygame.draw.rect(window, pygame.color.Color("gray"), przycisk)
        tekst = big_font.render(tekst_przycisk, True, pygame.color.Color("black"))
        window.blit(tekst, (230, 410))

        for polozenie, tresc in podpowiedzi:
            pygame.draw.circle(window, pygame.color.Color("blue"), (50 * polozenie[0], 50 * polozenie[1]), 12)

        for y in range(len(poziome_krawedzie)):
            for x in range(len(poziome_krawedzie[y])):
                if poziome_krawedzie[y][x] == 1:
                    pygame.draw.line(
                        window,
                        pygame.color.Color("black"),
                        (50 * x + 20, 50 * y + 25),
                        (50 * x + 80, 50 * y + 25),
                        10)

        for y in range(len(pionowe_krawedzie)):
            for x in range(len(pionowe_krawedzie[y])):
                if pionowe_krawedzie[y][x] == 1:
                    pygame.draw.line(
                        window,
                        pygame.color.Color("black"),
                        (50 * x + 25, 20 + 50 * y),
                        (50 * x + 25, 80 + 50 * y),
                        10)

        if tekst_podpowiedzi != "":
            pygame.draw.rect(window, pygame.color.Color("lightgray"), (75, 75, 450, 250))
            for i in range(len(tekst_podpowiedzi)):
                tekst = little_font.render(
                    tekst_podpowiedzi[i],
                    True,
                    pygame.color.Color("black"))
                window.blit(tekst, (80, 80 + 20 * i))

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    wyswietl_labirynt()

