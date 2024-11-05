import pygame


if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode((400, 500))
    pygame.display.set_caption('LabiryntNTFS')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(pygame.color.Color("white"))
        pygame.draw.rect(window, pygame.color.Color("green"), pygame.Rect(25, 25, 25, 25))
        pygame.display.flip()

