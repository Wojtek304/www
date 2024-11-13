import pygame

from quiz_ext4 import wyswietl_quiz


def wyswietl_labirynt():
    pozycja = (2, 7)
    pionowe_krawedzie = [
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    ]
    poziome_krawedzie = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    podpowiedzi = [
        ((1, 1), [
            "Charakterystyczną cechą ext4 jest mechanizm ekstentów, zastępujący",
            "adresowanie pośrednie bloków znane z ext2 oraz ext3. Ext4 zamiast",
            "adresować pojedyncze bloki, stara się mapować jak największą porcję",
            "danych na ciągły obszar bloków na dysku. Potrzebne są do tego 3 wartości:",
            "- początkowy blok w pliku",
            "- rozmiar obszaru w blokach",
            "- początkowy blok danych zapisanych na dysku",
            "Strukturę przechowującą te wartości nazywamy ekstentem.",
            "Dzięki temu mechanizmowi maksymalny rozmiar pliku w ext4 to 16 TB",
            "(w ext2 było to 2 GB)."
        ]),
        ((11, 1), [
            "System plików ext4 oferuje zwiększenie wielkości plików i partycji",
            "w porównaniu z ext3, a także większą wydajność i skalowalność.",
            "Jest również wydajniejszy i bardziej elastyczny, co pozwala na lepsze",
            "zarządzanie pamięcią i optymalizację wydajności.",
            "Posiada lepsze mechanizmy zarządzania przestrzenią dyskową, w tym",
            "lepszą obsługę dużych plików i lepsze zarządzanie blokami,",
            "co zmniejsza fragmentację.",
            "Wprowadzenie sum kontrolnych dla dziennika pozwala zwiększyć",
            "integralność danych oraz poprawić ochronę przed uszkodzeniami",
            "w przypadku awarii systemu."
        ]),
        ((1, 7), [
            "Wprowadzenie EXT4 pozwoliło na szybsze sprawdzanie systemu plików",
            "po awarii, dzięki pominięciu w tym procesie nieużywanych bloków danych.",
            "Poprawiona została również technika zapisu czasu oraz ominięcie problemu",
            "z rokiem 2038 (przekręcenie licznika systemowego i cofnięcie się",
            "do roku 1901).",
            "EXT4 pozwala na utworzenie nieskończonej liczby podkatalogów",
            "(EXT3 pozwalał tylko na 32 000).",
            "Maksymalna wielkość wolumenów to eksabajt (1000 * 1000 * 1000GB),",
            "natomiast pojedynczy plik może mieć rozmiar 16TB. Na koniec test zapisu",
            "pliku 4GB w EXT4 jest około 2x szybszy niż w systemach EXT3 czy XFS."
        ]),
        ((11, 7), [
            "Opóźniona alokacja jest strategią jak najdłuższego przetrzymywania",
            "danych zapisywanych na dysk w pamięci podręcznej.",
            "W momencie stworzenia pliku, wyszukiwane są wolne bloki w VFS",
            "(Virtual File System), które mogą pomieścić bloki danych oraz metadanych.",
            "Następnie rezerwuje się je, aby mieć pewność, że w momencie",
            "faktycznego zapisu będzie wystarczająco miejsca na dysku.",
            "Zalety opóźnionej alokacji to zwiększona wydajność przy zapisie rosnących",
            "plików oraz zmniejszenie fragmentacji danych.",
            "Wadą opóźnionej alokacji jest zwiększenie ryzyka utraty danych",
            "podczas awarii."
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
    pygame.display.set_caption('Labirynt ext4')
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
            pygame.draw.circle(window, pygame.color.Color("darkorange"), (50 * polozenie[0], 50 * polozenie[1]), 12)

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

