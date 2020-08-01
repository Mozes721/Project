#Import the pygame libraries
import pygame
from pygame_projects.Pong_game.settings import *
from pygame_projects.Pong_game.paddle import *
from pygame_projects.Pong_game.ball import *
from time import sleep

#Open a window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))
pygame.display.set_caption("Pong!")

'''SET UP PADDLES'''
paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 100

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 100

'''SET UP BALL'''
ball = Ball(RED, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

center = ball.rect.x, ball.rect.y
'''scores'''
ScoreA = 0
ScoreB = 0

#list to contain all sprites
all_sprites_group = pygame.sprite.Group()
clock = pygame.time.Clock()

#add the paddles to the list of sprites
all_sprites_group.add(paddleA)
all_sprites_group.add(paddleB)
all_sprites_group.add(ball)

running = True

'''Main loop!'''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    '''Moving paddles'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(MOVE)
    if keys[pygame.K_s]:
        paddleA.moveDown(MOVE)
    if keys[pygame.K_UP]:
        paddleB.moveUp(MOVE)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(MOVE)







    #game logic
    all_sprites_group.update()

    '''Check if ball is bouncing'''
    if ball.rect.x >= 690:
        ScoreA +=1
        sleep(2)
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ScoreB += 1
        sleep(2)
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()


    #clear screen to black
    screen.fill(BLACK)
    #draw net
    pygame.draw.line(screen, WHITE,[349,0], [349,500],5)

    all_sprites_group.draw(screen)

    #Display score
    font = pygame.font.Font(None, 74)
    text = font.render(str(ScoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    font = pygame.font.Font(None, 74)
    text = font.render(str(ScoreB), 1, WHITE)
    screen.blit(text, (450, 10))
    #update screen
    pygame.display.flip()
    #limit to 60 frames per second
    clock.tick(60)

#ones exited quit game
pygame.quit()
