import pygame as pg
import sys
from pygame.locals import *
from Classes import Tablero


mainClock = pg.time.Clock()
pg.init()

title = pg.display.set_caption("Ubongo UPC")
clock = pg.time.Clock()
font = pg.font.SysFont(None, 20)
# Backgrounds
imgInicio = pg.image.load('Resources\MainImages\_inicio.jpg')
imgJugar = pg.image.load('Resources\MainImages\CantJugadores.png')
imgInstrucciones = pg.image.load('Resources\MainImages\_instrucciones.jpg')
imgCreditos = pg.image.load('Resources\MainImages\_creditos.jpg')
done = False

# Buttons 1
btn1_Jugar = pg.image.load('Resources\Buttons\_btn1_Jugar.png')
btn1_Instrucciones = pg.image.load('Resources\Buttons\_btn1_Instrucciones.png')
btn1_Creditos = pg.image.load('Resources\Buttons\_btn1_Creditos.png')
btn1_Salir = pg.image.load('Resources\Buttons\_btn1_Salir.png')
# Buttons 2
btn2_Jugar = pg.image.load('Resources\Buttons\_btn2_Jugar.png')
btn2_Instrucciones = pg.image.load('Resources\Buttons\_btn2_Instrucciones.png')
btn2_Creditos = pg.image.load('Resources\Buttons\_btn2_Creditos.png')
btn2_Salir = pg.image.load('Resources\Buttons\_btn2_Salir.png')


# Button splash
class Cursor(pg.Rect):
    def __init__(self):
        pg.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = pg.mouse.get_pos()


class Boton(pg.sprite.Sprite):
    def __init__(self, imagen1, imagen2, x=200, y=200):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left, self.rect.top = (x, y)

    def update(self, pantalla, cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal

        pantalla.blit(self.imagen_actual, self.rect)


btn_Jugar = Boton(btn1_Jugar, btn2_Jugar, 600, 100)
btn_Instrucciones = Boton(btn1_Instrucciones, btn2_Instrucciones, 550, 250)
btn_Creditos = Boton(btn1_Creditos, btn2_Creditos, 585, 400)
btn_Salir = Boton(btn1_Salir, btn2_Salir, 610, 550)

def inicio():
    screen.blit(imgInicio, (0, 0))


def seleccion():
    screen.blit(imgJugar, (0, 0))


def instrucciones():
    screen.blit(imgInstrucciones, (0, 0))


def creditos():
    screen.blit(imgCreditos, (0, 0))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def run():
    cursor1 = Cursor()
    while True:

        screen.fill((0, 0, 0))
        inicio()

        mx, my = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if cursor1.colliderect(btn_Jugar.rect):
                    game()
                if cursor1.colliderect(btn_Instrucciones.rect):
                    instructions()
                if cursor1.colliderect(btn_Creditos.rect):
                    credits()
                if cursor1.colliderect(btn_Salir.rect):
                    pg.quit()
                    sys.exit()
            if event.type == pg.QUIT:
                sys.exit()

        mainClock.tick(60)
        cursor1.update()
        btn_Jugar.update(screen, cursor1)
        btn_Instrucciones.update(screen, cursor1)
        btn_Creditos.update(screen, cursor1)
        btn_Salir.update(screen, cursor1)

        pg.display.update()


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
        creditos()
        pg.display.update()
        mainClock.tick(60)


if __name__ == '__main__':
    run()
