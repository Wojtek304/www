import pygame

if __name__ == '__main__':

    pozycja = (2, 1) # (6, 4)
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
        ((1, 1), ["tekst podpowiedzi 1"]),
        ((6, 1), ["tekst podpowiedzi 2"]),
        ((11, 1), [
            "Na liście uprawnień ACL znajduje się zestaw wpisów kontroli ACE.",
            "W każdym wpisie zawarta jest informacja o użytkowniku oraz jego",
            "uprawnieniach podstawowych (read – odczyt, write – zapis, modify –",
            "zmiana zawartości lub usuwanie, list folder contents – wyświetlenie",
            "zawartości folderu, full control – pełen zakres uprawnień)", "i uprawnieniach specjalnych.",
            "Uprawnienia blokujące dostęp są odczytywane przed uprawnieniami",
            "umożliwiającymi dostęp. Uprawnienia są dostępne zarówno dla folderów,",
            "jak i dla plików. Uprawnienia są domyślnie dziedziczone z folderu",
            "na podfoldery i pliki. Ustawienie to może być włączone lub wyłączone.",
            "Uprawnienia dziedziczone są odczytywane po uprawnieniach",
            "niedziedziczonych."
    ]),
        ((1, 7), ["tekst podpowiedzi 4"]),
        ((6, 7), ["tekst podpowiedzi 5"]),
        ((11, 7), ["tekst podpowiedzi 6"]),
    ]

    def czy_podpowiedz():
        for polozenie, tresc in podpowiedzi:
            if pozycja == polozenie:
                return tresc
        return ""

    tekst_podpowiedzi = ""

    pygame.init()

    little_font = pygame.font.SysFont('Arial', 16)
    big_font = pygame.font.SysFont('Arial', 24)

    window = pygame.display.set_mode((600, 500))
    pygame.display.set_caption('LabiryntNTFS')
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
                pozycja = pygame.mouse.get_pos()
                if przycisk.collidepoint(pozycja):
                    running = False

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

