import pygame
from pygame_projects.Pong_game.settings import *
from random import randint

class Ball(pygame.sprite.Sprite):
    #this class represents the ball it derives from Sprites class in python

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw the ball rectangle
        pygame.draw.rect(self.image, color, [0,0, width, height])

        self.velocity = [randint(4,8), randint(-8,8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] =- self.velocity[0]
        self.velocity[1] =- self.velocity[1]


