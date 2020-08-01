import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        #call the parent class Sprite constructor
        super().__init__()

        #pass the color of the car, and its x, y possiton, widht and height
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #draw the paddle(a rectangle)
        pygame.draw.rect(self.image, color, [0,0, width, height])

        #rect the image
        self.rect = self.image.get_rect()


    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 700:
            self.rect.x = 700

