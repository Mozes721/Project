import pygame
from pygame_projects.Pong_game.settings import *

class Paddle(pygame.sprite.Sprite):
    #initialize init atributes
    def __init__(self, color, width, height):
    #call the parent class constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw a rectangle
        pygame.draw.rect(self.image, color, [0,0, width, height])

        #fetch the image
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0
    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400

