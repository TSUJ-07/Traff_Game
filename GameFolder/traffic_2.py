import pygame
import random
import pygame.mixer
from config_2 import *



class Traffic:
    def __init__(self):
        self.user_car_rect = pygame.Rect((225, 625), car_w_h)
        self.user_car_surface = pygame.image.load("img/user_car.png")
        self.user_car_surface = pygame.transform.scale(self.user_car_surface, car_w_h)
        self.obstacles = []
        self.speeds = []

        x_positions = [100, 200, 300, 400]  # lane positions
        for x in x_positions:  # create one obstacle per lane
            rect = pygame.Rect(x, 0, *car_w_h)  # start at top of screen
            surface = self.random_image()
            speed = self.random_speed()
            self.obstacles.append({'rect': rect, 'surface': surface})
            self.speeds.append(speed)

    def random_speed(self):
        return random.randint(speed_min, speed_max)

    def random_image(self):
        return pygame.transform.scale(random.choice(list(CAR_IMG.values())), car_w_h)

    def update_obstacles(self):
        count = 0
        for i, car in enumerate(self.obstacles):
            car['rect'].y += self.speeds[i]  # move down @random speed
            if car['rect'].top > resolution[1]:
                car['rect'].y = -car_w_h[1]  # reset position
                car['surface'] = self.random_image()
                self.speeds[i] = self.random_speed()


    def draw(self, screen):
        screen.blit(self.user_car_surface, self.user_car_rect)
        for car in self.obstacles:
            screen.blit(car['surface'], car['rect'])
