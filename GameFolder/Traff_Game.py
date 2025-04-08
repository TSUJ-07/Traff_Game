import pygame, sys
from pygame.locals import *
#This is just a template for the window
# Discard anything that is not related to the game
#Changes can also be made through Github without the use of PyCharm
#Always remember to 'commit' when finished writing code so the entire source is updated

pygame.init()
FPS= 60
resolution= (400,400)
screen= pygame.display.set_mode(resolution)
timer= pygame.time.Clock()
black= (0,0,0)
blue= (0,0,255)


rect= pygame.Rect(0,0,20,20)

speed= 50
upNdown= True
while True:
    keys = pygame.key.get_pressed()
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            sys.exit(0)
        if x.type == KEYDOWN and x.type == [K_ESCAPE]:
            sys.exit(0)

    screen.fill(black)

    if upNdown:
        rect.y -=speed
        if rect.top < 0:
            upNdown= False
    else:
        rect.y += speed
        if rect.top > resolution[1]:
            upNdown= True

    pygame.draw.rect(screen,blue,rect)
    pygame.display.flip()
    timer.tick(FPS)
