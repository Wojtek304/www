import pygame

from pytanie import Pytanie


def wyswietl_quiz():
    big_font = pygame.font.SysFont('Arial', 24)
    little_font = pygame.font.SysFont('Arial', 15)

    window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Quiz ext4')

    punkty = 0

    pytania = [
        Pytanie(
            1,
            [
                'Jaki mechanizm wykorzystuje system ext4',
                'do zwiększenia maksymalnego rozmiaru plików?',
                '(podpunkt a)'
            ],
            "B",
            [
                ["Fragmentację dysku"],
                ["Ekstenty"],
                ["Adresowanie pojedynczych bloków"],
                ["Nie wykorzystuje żadnego"]]
        ),
        Pytanie(
            2,
            [
                'Jaki jest maksymalny rozmiar pliku w ext4?',
                '(podpunkt b)'
             ],
            "C",
            [
                ["16 MB"],
                ["2 GB"],
                ["16 TB"],
                ["Nie ma limitu"]]
        ),
        Pytanie(
            3,
            [
                'Jakie zalety ma system ext4 w stosunku do ext3?',
                '(podpunkt c)'
            ],
            "D",
            [
                ["Nie występuje w nim problem z rokiem 2038"],
                ["Szybsze sprawdzanie systemu plików",
                 "po awarii"],
                ["Większe maksymalny rozmiar",
                 "i szybkość zapisu plików"],
                ["Wszystkie z powyższych"]]
        ),
        Pytanie(
            4,
            [
                'Jaka jest wada użycia opóźnionej alokacji w ext4?',
                '(podpunkt d)'],
            "A",
            [
                ["Zwiększa ryzyko utraty danych"],
                ["Sprawia, że dane pojawiają się",
                 "w pamięci później"],
                ["Zmniejsza fragmentację danych"],
                ["Nie ma wad"]]
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

        pygame.display.flip()


if __name__ == '__main__':

    pygame.init()
    wyswietl_quiz()


