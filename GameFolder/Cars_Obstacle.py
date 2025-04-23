import pygame, Config, random
pygame.init()
#Made to monitor movement of oncoming "Traffic" descending from the top screen


class Obstacle:
    def __init__(self):
        self.roam= True
        lanes= random.choice(Config.OBS_LANES)
        self.speed= Config.car_speed_random()
        self.rect= pygame.Rect(
            lanes - Config.OBS_WIDTH//2, #x
            -Config.OBS_HEIGHT, #y
            Config.OBS_WIDTH, #object width
            Config.OBS_HEIGHT #object height
        )
        self.surface= pygame.Surface((Config.OBS_WIDTH, Config.OBS_HEIGHT))
        self.surface.fill(Config.RED)

    def move_obs(self):
        self.rect.y += self.speed
        if self.rect.top > Config.RESOLUTION[1]:
            self.reset()

    def reset(self):
        self.rect.y = -Config.OBS_HEIGHT
        self.speed= Config.car_speed_random()

    def draw_obs(self, screen):
        screen.blit(self.surface, self.rect)