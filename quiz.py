import pygame

if __name__ == '__main__':

    pygame.init()

    font = pygame.font.SysFont('Arial', 24)

    window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Quiz')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(pygame.color.Color("white"))

        text_surface = font.render('Pytanie 1', True, pygame.color.Color("black"))
        window.blit(text_surface, (250, 40))

        text_surface = font.render('Czy z otwartego pliku może korzystać więcej niż jeden użytkownik lub proces?', True, pygame.color.Color("black"))
        window.blit(text_surface, (50, 80))

        lista = [
            ("A", (10, 250), "Nie"),
            ("B", (10, 300), "Tak, pod warunkiem że mają odpowiednie uprawnienia"),
            ("C", (400, 250), "Tak, pod warunkiem że są nazwane tak samo"),
            ("D", (400, 300), "Tak, niezależnie od uprawnień")
        ]


        for litera, polozenie, tresc in lista:
            tekst_odpowiedz = font.render('Odpowiedź ' + litera, True, pygame.color.Color("black"))
            tekst_tresc = font.render(tresc, True, pygame.color.Color("black"))
            window.blit(tekst_odpowiedz, polozenie)
            window.blit(tekst_tresc, (polozenie[0], polozenie[1] + 25))

        pygame.display.flip()
