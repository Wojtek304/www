import pygame

if __name__ == '__main__':

    pygame.init()

    big_font = pygame.font.SysFont('Arial', 24)
    little_font = pygame.font.SysFont('Arial', 15)

    window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Quiz')

    punkty = 0

    poprawna_odpowiedź = "B"

    lista = [
        ("A", pygame.Rect(10, 250, 250, 70), ["Nie"]),
        ("B", pygame.Rect(10, 325, 250, 70), ["Tak, pod warunkiem że", "mają odpowiednie uprawnienia"]),
        ("C", pygame.Rect(300, 250, 250, 70), ["Tak, pod warunkiem że", "są nazwane tak samo"]),
        ("D", pygame.Rect(300, 325, 250, 70), ["Tak, niezależnie od uprawnień"])
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                for litera, prostokat, _ in lista:
                    pozycja = pygame.mouse.get_pos()
                    if prostokat.collidepoint(pozycja):
                        print("Kliknięta odpowiedź " + litera)
                        if litera == poprawna_odpowiedź:
                            punkty = punkty + 1

        window.fill(pygame.color.Color("white"))

        punkty_tekst = "Punkty: " + str(punkty)

        text_surface = little_font.render(punkty_tekst, True, pygame.color.Color("black"))
        window.blit(text_surface, (500, 40))

        text_surface = big_font.render('Pytanie 1', True, pygame.color.Color("black"))
        window.blit(text_surface, (250, 40))

        linie = [('Czy z otwartego pliku może korzystać', 0), ('więcej niż jeden użytkownik lub proces?', 30)]
        for linia, wysokosc in linie:
            text_surface = big_font.render(linia, True, pygame.color.Color("black"))
            window.blit(text_surface, (50, 80 + wysokosc))

        for litera, prostokat, tresc in lista:
            pygame.draw.rect(window, pygame.color.Color("lightgray"), prostokat)
            tekst_odpowiedz = little_font.render('Odpowiedź ' + litera, True, pygame.color.Color("black"))
            window.blit(tekst_odpowiedz, prostokat.topleft)
            for i in range(len(tresc)):
                tekst_tresc = little_font.render(tresc[i], True, pygame.color.Color("black"))
                window.blit(tekst_tresc, (prostokat.left, prostokat.top + (i + 1) * 20))

        pygame.display.flip()
