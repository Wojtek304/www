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
        text_surface = font.render('Hello World!', True, (0, 0, 0))
        window.blit(text_surface, (250, 40))

        pygame.display.flip()
