import pygame, random
pygame.init()

#Display Settings
RESOLUTION = (564, 1000)
FPS= 60
XEVENT = pygame.USEREVENT +1

#Math for Perfection
LANE_WIDTH= RESOLUTION[0]// 4 # Divided by number of lanes
LANE1= 0.5 * LANE_WIDTH
LANE2= (1+ 0.5) * LANE_WIDTH
LANE3= (2+ 0.5) * LANE_WIDTH
LANE4= (3+ 0.5) * LANE_WIDTH

BLACK= (0,0,0)
RED= (255,0,0)
BLUE= (0,0,255)
GREEN= (0,255,0)
WHITE= (255,255,255)

#Player Settings
PLAYER_POS= (LANE2, RESOLUTION[1] - 30)
PLAYER_WIDTH= 50
PLAYER_HEIGHT= 100
PLAYER_SPEED= 5

#---Player_Sprites---#
LOAD= pygame.image.load
# PLAYER_IMG= {
#     "User" : LOAD("img/ ______________")
# }

#Obstacle Settings
OBS_WIDTH= 50
OBS_HEIGHT= 100
OBS_LANES= (LANE1, LANE2, LANE3, LANE4) # positions on the screen; x-axis
MIN_SPEED=2
MAX_SPEED=6
#---Obstacle_Sprites---#
CAR_IMG= {
    "car1" : LOAD("img/Silver_MERC.png"),
    "car2" : LOAD("img/vecteezy_modern_green.png"),
    "car3": LOAD("img/vecteezy_sport_car.png"),
    "car4" : LOAD("img/vecteezy_white_car.png"),
    "car5" : LOAD("Caleb Stuff/Garbage.png"),
    "car6" : LOAD("img/PCar.png"),
     "car7": LOAD("img/sport_red.png"),
}

#Road Display
GRASS= LANE_WIDTH * 0.1
# ROAD_SIZE= RESOLUTION[0] - (GRASS *2)

#---Random speed for traffic---#
def car_speed_random():
    return random.randint(MIN_SPEED, MAX_SPEED)

#Sounds
#---Sound_Bar---#
SOUND= pygame.mixer.Sound
MP3= {
    "start" : SOUND("sound/start_and_rev_sound.mp3"),
    "failure" : SOUND("sound/end sound.mp3"),
    "crash" : SOUND("sound/crash_sound.mp3"),
    "swipe" : SOUND("sound/swipe_sound.mp3"),
}

#Diffuclty Builder??
# SPEED_SCALING= 0.5

#--Boundary for player--#
# Taking the width of the entire lane and multiplying by 0.1 gets us the boundary on the left,
# where 0.1 (10% of LANE_WIDTH) was just an approximate guess that would gauge a certain percentage of the entire lane_width.
# So, subtracting that value from the entire width of the display should give us the right boundary of the lane.
# Might change percentage based on background image
BOUND_ON_RIGHT= RESOLUTION[0] - GRASS