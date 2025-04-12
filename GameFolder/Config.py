import pygame, random
pygame.init()

#Settings
RESOLUTION = (500, 750)
FPS= 60
XEVENT = pygame.USEREVENT +1

BLACK= (0,0,0)
RED= (255,0,0)
BLUE= (0,0,255)
GREEN= (0,255,0)

#Player Settings

PLAYER_POS= (225,625)
PLAYER_WIDTH= 50
PLAYER_HEIGHT= 100
PLAYER_SPEED= 5
#---Player_Sprites---#
#Insert{}

#Obstacle Settings
TRAFF_WIDTH= 50
TRAFF_HEIGHT= 100
TRAFF_LANES= [100,200,300,400]
MIN_SPEED=2
MAX_SPEED=6
#---Obstacle_Sprites---#
#Insert{}

#Road Display
GRASS= 50
ROAD_SIZE= RESOLUTION[0] - (GRASS *2)
#---Random speed for traffic---#
def car_speed_random():
    return random.randint(MIN_SPEED, MAX_SPEED)
def screen():
    return pygame.display.set_mode(RESOLUTION)

#Sounds
#---Sound_Bar---#
#Insert{}