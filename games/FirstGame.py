#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
 
# Constantes
WIDTH = 640
HEIGHT = 480
 
# Clases
# ---------------------------------------------------------------------
 
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("pow1.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]
 
    def actualizar(self, time, pala_jug):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
            self.image = load_image("pow2.png", True)

 
class Pala(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("Magic_band2.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5
 
    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time
        if self.rect.left >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
        if self.rect.right <= WIDTH:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
 
# ---------------------------------------------------------------------
 
# Funciones
# ---------------------------------------------------------------------
 
def load_image(filename, transparent=False):
#        try: image = pygame.image.load(filename)
        image = pygame.image.load(filename)
#        except pygame.error, message:
#                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, 1)
        return image
 
# ---------------------------------------------------------------------
 
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
 
#    background_image = load_image('images/fondo_pong.png')
    bola = Bola()
    pala_jug = Pala(30)
 
    clock = pygame.time.Clock()
 
    while True:
        screen.fill(1)
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == 'QUIT':
                sys.exit()
 
        bola.actualizar(time, pala_jug)
        pala_jug.mover(time, keys)
#        screen.blit(background_image, (0, 0))
        screen.blit(bola.image, bola.rect)
        screen.blit(pala_jug.image, pala_jug.rect)
        pygame.display.flip()
    return 0
 
if __name__ == '__main__':
    pygame.init()
    main()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("swar1.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]

    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
