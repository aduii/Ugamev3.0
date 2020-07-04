import pygame

imagen1 = pygame.image.load("Resources/CarasImages/cara1.png")
imagen2 = pygame.image.load("Resources/CarasImages/cara2.png")
imagen3 = pygame.image.load("Resources/CarasImages/cara3.png")
imagen4 = pygame.image.load("Resources/CarasImages/cara4.png")
imagen5 = pygame.image.load("Resources/CarasImages/cara5.png")
imagen6 = pygame.image.load("Resources/CarasImages/cara6.png")


def dice(n, screen):
    if n == 1:
        screen.blit(imagen1, (620, 580))
    elif n == 2:
        screen.blit(imagen2, (620, 580))
    elif n == 3:
        screen.blit(imagen3, (620, 580))
    elif n == 4:
        screen.blit(imagen4, (620, 580))
    elif n == 5:
        screen.blit(imagen5, (620, 580))
    elif n == 6:
        screen.blit(imagen6, (620, 580))


def puzzle(enum):
    if (enum == 1):
        from Classes import Puzzle1
        Puzzle1.main()
    if (enum == 2):
        from Classes import Puzzle2
        Puzzle2.main()
    if (enum == 3):
        from Classes import Puzzle3
        Puzzle3.main()
    if (enum == 4):
        from Classes import Puzzle4
        Puzzle4.main()
    if (enum == 5):
        from Classes import Puzzle5
        Puzzle5.main()
    if (enum == 6):
        from Classes import Puzzle6
        Puzzle6.main()
