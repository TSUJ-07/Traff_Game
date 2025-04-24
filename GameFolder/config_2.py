import pygame

LOAD= pygame.image.load
# dictionary of obstacle car images
CAR_IMG = {
    "car1": LOAD("img/Silver_MERC.png"),
    "car2": LOAD("img/vecteezy_modern_green.png"),
    "car3": LOAD("img/vecteezy_sport_car.png"),
    "car4": LOAD("img/vecteezy_white_car.png"),
    "car5": LOAD("img/pinterest-bugatti2.png"),
    "car6": LOAD("img/PCar.png"),
    "car7": LOAD("img/sport_red.png"),
}

#sounds
pygame.mixer.init()

sound= pygame.mixer.Sound
MP3= {
    "start" : sound("sound/start_and_rev_sound.mp3"),
    "failure" : sound("sound/end sound.mp3"),
    "crash" : sound("sound/crash_sound.mp3"),
    "swipe" : sound("sound/swipe_sound.mp3"),
    "explosion" : sound("sound/big_explosions2.mp3"),
}


# game settings
resolution = (565, 750)
car_w_h = (50, 100)
user_pos = (225, 625)
blue = (0, 0, 255)
green = (0, 255, 0)
white= (255,255,255)
red= (255,0,0)
speed_min = 1
speed_max = 6
player_speed = 5
lane_width = resolution[0] // 4
lane1 = 0.5 * lane_width
lane2 = (1 + 0.5) * lane_width
lane3 = (2 + 0.5) * lane_width
lane4 = (3 + 0.5) * lane_width
grass_width = int(lane_width * 0.1)
