import pygame
from pygame.draw import *
pygame.init()
FPS=30
screen = pygame.display.set_mode((500, 500))
screen.fill('peachpuff')
#sun
circle(screen,(255,255,0),(250,100),20)
#land
rect(screen,(207,204,196),[(0,300),(500,300)],500)
#cloud
rect(screen,(244,193,193),[(0,150),(500,150,)],100)
#rock1
polygon(screen,(238,118,0),[(0,200),(75,110),(75,110),(84,127),(84,127),(120,120),
                            (120,120),(180,180),
                            (180,180),(250,170),
                            (250,170),(300,190),
                            (300,190),(350,200)],)
polygon(screen,(238,118,0),[(360,200),(400,150),
                            (400,150),(450,100),
                            (450,100),(500,80),(500,200)],)
#rock2

polygon(screen,(139,0,0),[(0,300),(75,200),(75,190),(84,200),(84,200),(120,220),
                            (120,200),(180,220),
                            (180,200),(250,230),
                            (250,230),(300,200),(310,100),
                            (320,150),(350,300)],)
polygon(screen,(139,0,0),[(380,300),(400,200),(400,300),(420,250),(470,200),(500,150),(500,300)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()