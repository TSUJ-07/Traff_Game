import pygame
pygame.init()
import sys
import pygame.mixer
from traffic_2 import Traffic
from config_2 import *


def collision(user_car, obstacles):
    for obstacle in obstacles:
        if user_car.colliderect(obstacle['rect']):
            print("Collision Detected!")
            crash_sound.play()

            return True
    return False


class RoadWork:
    def __init__(self, resolution, grass_width, green):
        self.grass_left = pygame.Rect(0, 0, grass_width, resolution[1])
        self.grass_surface = pygame.Surface((grass_width, resolution[1]))
        self.grass_right = pygame.Rect(resolution[0] - grass_width, 0, grass_width, resolution[1])
        self.grass_surf2 = pygame.Surface((grass_width, resolution[1]))
        self.grass_surface.fill(green)
        self.grass_surf2.fill(green)
        self.background_road = pygame.image.load("img/Background_Road.png").convert()

    def draw_grass(self, screen):
        screen.blit(self.grass_surface, self.grass_left.topleft)
        screen.blit(self.grass_surf2, self.grass_right.topleft)

    def draw_road(self, screen):
        screen.blit(self.background_road, (0, 0))


def user_movement():
    traffic_obj = Traffic()  # No need to pass resolution here
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Car Game")
    road = RoadWork(resolution, 50, (0, 255, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # user movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            end_sound.play()
            print("Game Ended")
            pygame.quit()
            sys.exit(0)
        if keys[pygame.K_a] and traffic_obj.user_car_rect.x > 50:
            traffic_obj.user_car_rect.x -= player_speed
            swipe_sound.play()
            if swipe_sound.play():
                continue

        if keys[pygame.K_d] and traffic_obj.user_car_rect.x < 450:
            traffic_obj.user_car_rect.x += player_speed
            swipe_sound.play()
            if swipe_sound.play():
                continue



        traffic_obj.update_obstacles()

        # collision check?
        if collision(traffic_obj.user_car_rect, traffic_obj.obstacles):
            crash_sound.play()
            if crash_sound.play():
                continue


        # drawing
        road.draw_road(screen)
        road.draw_grass(screen)
        traffic_obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)
