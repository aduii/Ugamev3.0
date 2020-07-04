import pygame, sys
import random
# from Classes import Gemas,Dado,Grafo,Jugador
import Classes.Gemas as Gemas
import Classes.Grafo as Grafo
import Classes.Jugador as Jugador
import Classes.Dado as Dado

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Ubongo')
screen = pygame.display.set_mode((1280, 720), 0, 32)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont(None, 30)

tableroImg = pygame.image.load("Resources/MainImages/ubongoTablero.png")
finalImg = pygame.image.load('Resources/MainImages/_final.png')
final2Img = pygame.image.load('Resources/MainImages/_final 2.png')
amarillaImg = Gemas.amarillaImg
azulImg = Gemas.azulImg
marronImg = Gemas.marronImg
moradaImg = Gemas.moradaImg
rojaImg = Gemas.rojaImg
verdeImg = Gemas.verdeImg


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False

# -------------------------------------------------------
od = Grafo.Grafo(72)
od.crear()


# -------------------------------------------------------

def Base():
    screen.blit(tableroImg, (0, 0))


def Final():
    screen.blit(finalImg, (0, 0))


def Final2():
    screen.blit(final2Img, (0, 0))


def tabla():
    x = 423
    y = 98
    a = 0
    for i in range(12):
        y = 98
        for j in range(6):
            if od.colores[a] == 1 and od.visitados[a] == False:
                screen.blit(amarillaImg, (x, y))
            elif od.colores[a] == 2 and od.visitados[a] == False:
                screen.blit(azulImg, (x, y))
            elif od.colores[a] == 3 and od.visitados[a] == False:
                screen.blit(marronImg, (x, y))
            elif od.colores[a] == 4 and od.visitados[a] == False:
                screen.blit(moradaImg, (x, y))
            elif od.colores[a] == 5 and od.visitados[a] == False:
                screen.blit(rojaImg, (x, y))
            elif od.colores[a] == 6 and od.visitados[a] == False:
                screen.blit(verdeImg, (x, y))
            a = a + 1
            y = y + 51
        x = x + 63


# -------------------------------------------------------

j1 = Jugador.player()
j2 = Jugador.player()
j3 = Jugador.player()
j4 = Jugador.player()


def FinalJuego1():
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        Final()

        pygame.display.update()
        mainClock.tick(60)


def FinalJuego2():
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        Final2()

        pygame.display.update()
        mainClock.tick(60)


# -------------------------------------------------------
class TableroUbongo(object):
    def __init__(self):
        self.Jugador = 1
        self.fila1 = 0
        self.fila2 = 1
        self.fila3 = 2
        self.fila4 = 3
        self.fila5 = 4
        self.fila6 = 5
        self.tiempo = 60
        self.ronda = 0
        self.enJuego = False

    def bot(self):
        j4.fijarprioridad()
        if self.enJuego:
            if od.colores[self.fila1] == j4.prioridadColor or od.colores[self.fila1 + 6] == j4.prioridadColor:
                od.visitados[self.fila1] = True
                od.visitados[self.fila1 + 6] = True
                j4.tomarGema(self.fila1, od)
                self.fila1 = self.fila1 + 12
                pygame.display.update()
            elif od.colores[self.fila2] == j4.prioridadColor or od.colores[self.fila2 + 6] == j4.prioridadColor:
                od.visitados[self.fila2] = True
                od.visitados[self.fila2 + 6] = True
                j4.tomarGema(self.fila2, od)
                self.fila2 = self.fila2 + 12
                pygame.display.update()
            elif od.colores[self.fila3] == j4.prioridadColor or od.colores[self.fila3 + 6] == j4.prioridadColor:
                od.visitados[self.fila3] = True
                od.visitados[self.fila3 + 6] = True
                j4.tomarGema(self.fila3, od)
                self.fila3 = self.fila3 + 12
                pygame.display.update()
            elif od.colores[self.fila4] == j4.prioridadColor or od.colores[self.fila4 + 6] == j4.prioridadColor:
                od.visitados[self.fila4] = True
                od.visitados[self.fila4 + 6] = True
                j4.tomarGema(self.fila4, od)
                self.fila4 = self.fila4 + 12
                pygame.display.update()
            elif od.colores[self.fila5] == j4.prioridadColor or od.colores[self.fila5 + 6] == j4.prioridadColor:
                od.visitados[self.fila5] = True
                od.visitados[self.fila5 + 6] = True
                j4.tomarGema(self.fila5, od)
                self.fila5 = self.fila5 + 12
                pygame.display.update()
            elif od.colores[self.fila6] == j4.prioridadColor or od.colores[self.fila6 + 6] == j4.prioridadColor:
                od.visitados[self.fila6] = True
                od.visitados[self.fila6 + 6] = True
                j4.tomarGema(self.fila6, od)
                self.fila6 = self.fila6 + 12
                pygame.display.update()
            else:
                od.visitados[self.fila1] = True
                od.visitados[self.fila1 + 6] = True
                j4.tomarGema(self.fila1, od)
                self.fila1 = self.fila1 + 12
                pygame.display.update()
            self.enJuego = False

    def tablero(self):
        running = True
        n = 0
        enum = 0
        while running:
            screen.fill((0, 0, 0))
            draw_text('tablero', font, (255, 255, 255), screen, 20, 20)

            mx, my = pygame.mouse.get_pos()

            button_fila1 = pygame.Rect(300, 98, 30, 30)
            button_fila2 = pygame.Rect(300, 149, 30, 30)
            button_fila3 = pygame.Rect(300, 200, 30, 30)
            button_fila4 = pygame.Rect(300, 251, 30, 30)
            button_fila5 = pygame.Rect(300, 302, 30, 30)
            button_fila6 = pygame.Rect(300, 353, 30, 30)
            button_iniciar = pygame.Rect(1095, 595, 50, 50)
            button_Dado = pygame.Rect(615, 580, 60, 57)

            if button_fila1.collidepoint((mx, my)):
                if click and self.enJuego == True:
                    if self.fila1 <= 60:
                        od.visitados[self.fila1] = True
                        od.visitados[self.fila1 + 6] = True
                        if self.Jugador == 1:
                            j1.tomarGema(self.fila1, od)
                        elif self.Jugador == 2:
                            j2.tomarGema(self.fila1, od)
                        elif self.Jugador == 3:
                            j3.tomarGema(self.fila1, od)
                        elif self.Jugador == 4:
                            j4.tomarGema(self.fila1, od)
                        self.fila1 = self.fila1 + 12
                        self.enJuego = False
                        pygame.display.update()
                    else:
                        pass

            if button_fila2.collidepoint((mx, my)):
                if click and self.enJuego == True:
                    if self.fila2 <= 61:
                        od.visitados[self.fila2] = True
                        od.visitados[self.fila2 + 6] = True
                        if self.Jugador == 1:
                            j1.tomarGema(self.fila2, od)
                        elif self.Jugador == 2:
                            j2.tomarGema(self.fila2, od)
                        elif self.Jugador == 3:
                            j3.tomarGema(self.fila2, od)
                        elif self.Jugador == 4:
                            j4.tomarGema(self.fila2, od)
                        self.fila2 = self.fila2 + 12
                        self.enJuego = False
                        pygame.display.update()
                    else:
                        pass

            if button_fila3.collidepoint((mx, my)):
                if click and self.enJuego == True:
                    if self.fila3 <= 62:
                        od.visitados[self.fila3] = True
                        od.visitados[self.fila3 + 6] = True
                        if self.Jugador == 1:
                            j1.tomarGema(self.fila3, od)
                        elif self.Jugador == 2:
                            j2.tomarGema(self.fila3, od)
                        elif self.Jugador == 3:
                            j3.tomarGema(self.fila3, od)
                        elif self.Jugador == 4:
                            j4.tomarGema(self.fila3, od)
                        self.fila3 = self.fila3 + 12
                        pygame.display.update()
                        self.enJuego = False
                    else:
                        pass

            if button_fila4.collidepoint((mx, my)):
                if click and self.enJuego == True:
                    if self.fila4 <= 63:
                        od.visitados[self.fila4] = True
                        od.visitados[self.fila4 + 6] = True
                        if self.Jugador == 1:
                            j1.tomarGema(self.fila4, od)
                        elif self.Jugador == 2:
                            j2.tomarGema(self.fila4, od)
                        elif self.Jugador == 3:
                            j3.tomarGema(self.fila4, od)
                        elif self.Jugador == 4:
                            j4.tomarGema(self.fila4, od)
                        self.fila4 = self.fila4 + 12
                        self.enJuego = False
                        pygame.display.update()
                    else:
                        pass

            if button_fila5.collidepoint((mx, my)):
                if click and self.enJuego == True:
                    if self.fila5 <= 64:
                        od.visitados[self.fila5] = True
                        od.visitados[self.fila5 + 6] = True
                        if self.Jugador == 1:
                            j1.tomarGema(self.fila5, od)
                        elif self.Jugador == 2:
                            j2.tomarGema(self.fila5, od)
                        elif self.Jugador == 3:
                            j3.tomarGema(self.fila5, od)
                        elif self.Jugador == 4:
                            j4.tomarGema(self.fila5, od)
                        self.fila5 = self.fila5 + 12
                        self.enJuego = False
                        pygame.display.update()
                    else:
                        pass

            if button_fila6.collidepoint((mx, my)):
                if click and self.enJuego == True:
                    if self.fila6 <= 65:
                        od.visitados[self.fila6] = True
                        od.visitados[self.fila6 + 6] = True
                        if self.Jugador == 1:
                            j1.tomarGema(self.fila6, od)
                        elif self.Jugador == 2:
                            j2.tomarGema(self.fila6, od)
                        elif self.Jugador == 3:
                            j3.tomarGema(self.fila6, od)
                        elif self.Jugador == 4:
                            j4.tomarGema(self.fila6, od)
                        self.fila6 = self.fila6 + 12
                        self.enJuego = False
                        pygame.display.update()
                    else:
                        pass

            if button_iniciar.collidepoint((mx, my)):
                if click:
                    self.ronda = self.ronda + 1
                    if self.enJuego == False:
                        self.tiempo = 60
                    self.enJuego = True
                    enum = random.randint(1, 6)
                    n = random.randint(1, 6)

            if button_Dado.collidepoint((mx, my)):
                if click:
                    Dado.puzzle(enum)

            click = False

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT and self.enJuego == True:
                    self.tiempo = self.tiempo - 1
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_a:
                        self.Jugador = 1
                    if event.key == K_b:
                        self.Jugador = 2
                    if event.key == K_c:
                        self.Jugador = 3
                    if event.key == K_d:
                        self.Jugador = 4
                    if event.key == K_p:
                        self.bot()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            j1.mostrar()
            if self.ronda > 17:
                g1 = j1.conteo()
                g2 = j2.conteo()
                if g1 > g2:
                    return FinalJuego1()
                elif g1 < g2:
                    return FinalJuego2()
            Base()
            tabla()
            Gemas.GemasJ1(j1, screen)
            Gemas.GemasJ2(j2, screen)
            Gemas.GemasJ3(j3, screen)
            Gemas.GemasJ4(j4, screen)
            pygame.draw.rect(screen, (255, 0, 0), button_fila1)
            pygame.draw.rect(screen, (255, 0, 0), button_fila2)
            pygame.draw.rect(screen, (255, 0, 0), button_fila3)
            pygame.draw.rect(screen, (255, 0, 0), button_fila4)
            pygame.draw.rect(screen, (255, 0, 0), button_fila5)
            pygame.draw.rect(screen, (255, 0, 0), button_fila6)
            if self.tiempo > 0:
                draw_text(str(self.tiempo), font, (255, 255, 255), screen, 205, 67)
            else:
                draw_text(' se acabó el tiempo ', font, (255, 255, 255), screen, 200, 67)
            draw_text(str(self.ronda), font, (255, 255, 255), screen, 975, 67)
            Dado.dice(n, screen)
            pygame.display.update()
            mainClock.tick(60)

Juego = TableroUbongo()

def Iniciar():
    Juego.tablero()
