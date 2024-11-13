import pygame

import labirynt_ext4
from pytanie import Pytanie


def wyswietl_quiz():
    big_font = pygame.font.SysFont('Arial', 24)
    little_font = pygame.font.SysFont('Arial', 15)

    window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Quiz NTFS')

    punkty = 0

    pytania = [
        Pytanie(
            1,
            [
                'Czy z otwartego pliku może korzystać',
                'więcej niż jeden użytkownik lub proces?',
                '(podpunkt a)'
            ],
            "B",
            [
                ["Nie"],
                ["Tak, pod warunkiem że", "mają odpowiednie uprawnienia"],
                ["Tak, pod warunkiem że", "są nazwane tak samo"],
                ["Tak, niezależnie od uprawnień"]]
        ),
        Pytanie(
            2,
            [
                'Co nie jest zapisane w atrybutach pliku w NTFS?',
                '(podpunkt a)'
            ],
            "D",
            [
                ["Data modyfikacji pliku"],
                ["Nazwa pliku"],
                ["Rozmiar pliku"],
                ["Ikona pliku"]]
        ),
        Pytanie(
            3,
            [
                'Alicja ma uprawnienia do modyfikacji pliku.',
                'Czego nie może z nim zrobić?',
                '(podpunkt b)'
            ],
            "D",
            [
                ["Odczytać jego zawartości"],
                ["Zmienić nazwy pliku"],
                ["Usunąć pliku"],
                ["Zmienić uprawnień dostępu do pliku"]]
        ),
        Pytanie(
            4,
            [
                'Co jest zapisane na liście uprawnień ACL?',
                '(podpunkt c)'
            ],
            "C",
            [
                ["Wszystkie możliwe uprawnienia użytkownika"],
                ["Dostępne foldery i pliki"],
                ["Wpisy ACE z uprawnieniami", "poszczególnych użytkowników"],
                ["Uprawnienia edycji folderów"]]
        ),
        Pytanie(
            5,
            [
                'Czy uprawnienia NFTS dla folderu są domyślnie',
                'dziedziczone przez pliki i podfoldery?',
                '(podpunkt d)'
            ],
            "B",
            [
                ["Tak, niezależnie od ustawień"],
                ["Tak, choć można to wyłączyć", "w ustawieniach folderu"],
                ["Tylko przez pliki"],
                ["Nie"]]
        ),
        Pytanie(
            6,
            [
                'Które z uprawnień NFTS zapewniają',
                'możliwość tworzenia plików?',
                '(podpunkt e)'
            ],
            "C",
            [
                ["Wszystkie"],
                ["Tylko pełna kontrola"],
                ["Pełna kontrola, modyfikacja,", "zapis i wykonanie, zapis"],
                ["Żadne"]]
        )
    ]

    obecny_numer_pytania = 0
    blad = ''

    running = True
    while running:
        window.fill(pygame.color.Color("white"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                labirynt_ext4.wyswietl_labirynt()
            if event.type == pygame.MOUSEBUTTONUP:
                for litera, prostokat, _ in lista:
                    pozycja = pygame.mouse.get_pos()
                    if prostokat.collidepoint(pozycja):
                        if litera == poprawna_odpowiedź:
                            punkty = punkty + 1
                            blad = ''
                            obecny_numer_pytania = obecny_numer_pytania + 1
                        else:
                            blad = 'Odpowiedź ' + litera + ' jest niepoprawna'

        if obecny_numer_pytania < len(pytania):
            tekst_blad = big_font.render(
                blad,
                True,
                pygame.color.Color("darkred"))
            window.blit(tekst_blad, (150, 200))

            obecne_pytanie = pytania[obecny_numer_pytania]

            poprawna_odpowiedź = obecne_pytanie.poprawna_odpowiedz

            lista = [
                ("A", pygame.Rect(10, 250, 250, 70), obecne_pytanie.odpowiedzi[0]),
                ("B", pygame.Rect(10, 325, 250, 70), obecne_pytanie.odpowiedzi[1]),
                ("C", pygame.Rect(300, 250, 250, 70), obecne_pytanie.odpowiedzi[2]),
                ("D", pygame.Rect(300, 325, 250, 70), obecne_pytanie.odpowiedzi[3])
            ]

            punkty_tekst = "Punkty: " + str(punkty) + "/" + str(len(pytania))

            text_surface = little_font.render(punkty_tekst, True, pygame.color.Color("black"))
            window.blit(text_surface, (500, 40))

            text_surface = big_font.render('Pytanie ' + str(obecne_pytanie.numer), True, pygame.color.Color("black"))
            window.blit(text_surface, (250, 40))

            linie = obecne_pytanie.tresc
            for i in range(len(linie)):
                text_surface = big_font.render(linie[i], True, pygame.color.Color("black"))
                window.blit(text_surface, (50, 80 + 30 * i))

            for litera, prostokat, tresc in lista:
                pygame.draw.rect(window, pygame.color.Color("lightgray"), prostokat)
                tekst_odpowiedz = little_font.render('Odpowiedź ' + litera, True, pygame.color.Color("black"))
                window.blit(tekst_odpowiedz, prostokat.topleft)
                for i in range(len(tresc)):
                    tekst_tresc = little_font.render(tresc[i], True, pygame.color.Color("black"))
                    window.blit(tekst_tresc, (prostokat.left, prostokat.top + (i + 1) * 20))
        else:
            text_surface = big_font.render('Gratulacje, ukończyłeś quiz!', True, pygame.color.Color("black"))
            window.blit(text_surface, (200, 40))
            text_surface = big_font.render('Zamknij okno, aby przejść do części poświęconej ext4', True, pygame.color.Color("black"))
            window.blit(text_surface, (70, 80))

        pygame.display.flip()


if __name__ == '__main__':

    pygame.init()
    wyswietl_quiz()


