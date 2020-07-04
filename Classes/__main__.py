import pygame as pg
import sys
from pygame.locals import *
from Classes import Tablero
mainClock = pg.time.Clock()
pg.init()

# Definir colores RGB
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
# Defnir Tamano pantalla
size = (1280, 720)

# Ventana principal
screen = pg.display.set_mode(size)
title = pg.display.set_caption("Ubongo UPC")
clock = pg.time.Clock()
font = pg.font.SysFont(None, 20)
inicioImg = pg.image.load('Resources\MainImages\Inicio.png')
seleccionImg = pg.image.load('Resources\MainImages\CantJugadores.png')
instruccionesImg = pg.image.load('Resources\MainImages\Instrucciones.png')
creditosImg = pg.image.load('Resources\MainImages\_final.png')
done = False
#-------------------#

def inicio():
    screen.blit(inicioImg, (0, 0))

def seleccion():
    screen.blit(seleccionImg, (0, 0))

def instrucciones():
    screen.blit(instruccionesImg, (0, 0))

def creditos():
    screen.blit(creditosImg, (0, 0))

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)




click = False

def run():
    while True:


        screen.fill((0, 0, 0))
        #draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pg.mouse.get_pos()

        button_jugar = pg.Rect(860, 180, 145, 50)
        button_instrucciones = pg.Rect(760, 290, 330, 50)
        button_creditos = pg.Rect(825, 390, 205, 50)
        button_salir = pg.Rect(880, 510, 125, 50)
        if button_jugar.collidepoint((mx, my)):
            if click:
                game()
        if button_instrucciones.collidepoint((mx, my)):
            if click:
                instructions()
        if button_creditos.collidepoint((mx, my)):
            if click:
                credits()
        if button_salir.collidepoint((mx, my)):
            if click:
                pg.quit()
                sys.exit()

        #pygame.draw.rect(screen, (255, 0, 0), button_1)
        #pygame.draw.rect(screen, (255, 0, 0), button_2)
        #pygame.draw.rect(screen, (255, 0, 0), button_3)
        #pygame.draw.rect(screen, (255, 0, 0), button_4)

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        inicio()
        pg.display.update()
        mainClock.tick(60)


def game():

    running = True
    while running:


        screen.fill((0, 0, 0))

        mx, my = pg.mouse.get_pos()

        button_j2 = pg.Rect(770, 240, 300, 50)
        button_j3 = pg.Rect(770, 350, 300, 50)
        button_j4 = pg.Rect(770, 455, 300, 50)

        if button_j2.collidepoint((mx, my)):
            if click:
                Tablero.Iniciar()
                pass
        if button_j3.collidepoint((mx, my)):
            if click:
                Tablero.Iniciar()
                pass
        if button_j4.collidepoint((mx, my)):
            if click:
                Tablero.Iniciar()
                pass

        pg.draw.rect(screen, (255, 0, 0), button_j2)
        pg.draw.rect(screen, (255, 0, 0), button_j3)
        pg.draw.rect(screen, (255, 0, 0), button_j4)

        click = False
        #draw_text('game', font, (255, 255, 255), screen, 20, 20)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        seleccion()
        pg.display.update()
        mainClock.tick(60)


def instructions():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('instructions', font, (255, 255, 255), screen, 20, 20)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                Tablero.sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        instrucciones()
        pg.display.update()
        mainClock.tick(60)

def credits():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('credits', font, (255, 255, 255), screen, 20, 20)
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


        pg.display.update()
        mainClock.tick(60)

if __name__ == '__main__':
    run()
