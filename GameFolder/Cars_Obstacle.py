import pygame, Config
pygame.init()
#Made to monitor movement of oncoming "Traffic" descending from the top screen


class Obstacle:
    def __init__(self, car_in_lane):
        self.roam= True
        self.speed= [0, Config.car_speed_random()]
        self.rect= pygame.Rect(
            Config.TRAFF_LANES[car_in_lane], #x
            -Config.TRAFF_HEIGHT, #y
            Config.TRAFF_WIDTH, #object width
            Config.TRAFF_HEIGHT #object height
        )
        self.surface= pygame.Surface(Config.TRAFF_WIDTH, Config.TRAFF_HEIGHT)
        self.surface.fill(Config.RED)

    def move_obs(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.y > Config.RESOLUTION[1]:
            self.reset()

    def reset(self):
        self.rect.y = -Config.TRAFF_HEIGHT
        self.speed[1]= Config.car_speed_random()

    def draw_obs(self, screen):
        screen.blit(self.surface, self.rect.topleft)