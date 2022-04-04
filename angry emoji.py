import pygame
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 500))
screen.fill('white')
#face
circle(screen, (255,225,0),(200,175),100)
circle(screen, (0,0,0),(200,175),101,1)
#hair
polygon(screen,(0,0,0),[(125,100),(175,120) ], 10)
polygon(screen,(0,0,0),[(220,120),(275,100)],10)
#eyes
circle(screen,(0,0,0,),(150,150),25)
circle(screen,(0,0,0,),(250,150),20)
circle(screen,(255,0,0,),(150,150),12.5)
circle(screen,(255,0,0,),(250,150),10)
#smile
polygon(screen,(0,0,0),[(150,200),(250,200)],10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()