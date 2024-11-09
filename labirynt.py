import pygame

if __name__ == '__main__':

    pozycja = (6, 4)

    pygame.init()
    window = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('LabiryntNTFS')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    if pozycja[0] > 1:
                        pozycja = pozycja[0] - 1, pozycja[1]
                elif keys[pygame.K_RIGHT]:
                    if pozycja[0] < 11:
                        pozycja = pozycja[0] + 1, pozycja[1]
                elif keys[pygame.K_UP]:
                    if pozycja[1] > 1:
                        pozycja = pozycja[0], pozycja[1] - 1
                elif keys[pygame.K_DOWN]:
                    if pozycja[1] < 7:
                        pozycja = pozycja[0], pozycja[1] + 1

        window.fill(pygame.color.Color("white"))

        pygame.draw.rect(window, pygame.color.Color("green"), (50 * pozycja[0] - 12, 50 * pozycja[1] - 12, 25, 25))

        for i in range(2):
            for j in range(3):
                pygame.draw.circle(window, pygame.color.Color("blue"), (250 * j + 50, 50 + 300 * i), 12)

        for i in range(8):
            pygame.draw.line(
                window,
                pygame.color.Color("black"),
                (25, 50 * i + 25),
                (575, 50 * i + 25),
                10)

        for i in range(12):
            pygame.draw.line(
                window,
                pygame.color.Color("black"),
                (50 * i + 25, 25),
                (50 * i + 25, 375),
                10)

        pygame.display.flip()

