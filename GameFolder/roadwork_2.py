import pygame
pygame.init()
import sys
import config_2
import pygame.mixer
from traffic_2 import Traffic
from GameFolder.config_2 import *
from GameFolder import HighScore


font = pygame.font.Font(None, 36)

start_ticka = pygame.time.get_ticks()

pygame.display.set_caption("ANIME X TRAFF")

score = 0

# high_score = HighScore.load_high_score()
def collision(user_car, obstacles):
    for obstacle in obstacles:
        if user_car.colliderect(obstacle['rect']):
            print("Collision Detected!")
            config_2.MP3["crash"].play()
            return True
    return False

#In event log
def event_wait():
    while True:
        for i in pygame.event.get(): #Event handling to start game
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif i.type == pygame.KEYDOWN: #any key pressed then we start up game
                return #Enter start-up sound --> {Config.MP3["start"].play()}


class RoadWork:
    def __init__(self, resolution, grass_width, green):
        self.grass_left = pygame.Rect(0, 0, grass_width, resolution[1])
        self.grass_surface = pygame.Surface((grass_width, resolution[1]))
        self.grass_right = pygame.Rect(515, 0, grass_width, resolution[1])
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
            config_2.MP3["failure"].play()
            print("Game Ended")
            pygame.quit()
            sys.exit(0)
        if keys[pygame.K_a] and traffic_obj.user_car_rect.x > 50:
            traffic_obj.user_car_rect.x -= player_speed
            config_2.MP3["swipe"].play()

            if config_2.MP3["swipe"].play():
                continue

        if keys[pygame.K_d] and traffic_obj.user_car_rect.x < 450:
            traffic_obj.user_car_rect.x += player_speed
            config_2.MP3["swipe"].play()
            if config_2.MP3["swipe"].play():
                continue





        if collision(traffic_obj.user_car_rect, traffic_obj.obstacles):
            config_2.MP3["crash"].play()
            pygame.time.delay(10)
            # font = pygame.font.Font(None, 48)
            text_surf = font.render("You Have Crashed!!!", True, (255, 2, 2))
            text_surf2 = font.render(f"Your Score is: {score}", True, (255, 255, 255))
            # high_score_surf = font.render(f"High Score: {high_score}", True, (255, 255, 2))
            text_rect = text_surf.get_rect(midtop=(screen.get_width() / 2, screen.get_height() / 2))
            text_rect2 = text_surf.get_rect(midtop=(screen.get_width() / 2, screen.get_height() / 3))
            high_score_rect = text_surf.get_rect(midtop=(screen.get_width() / 2, screen.get_height() / 4))
            # screen.blit(high_score_surf, high_score_rect)
            screen.blit(text_surf, text_rect)
            screen.blit(text_surf2, text_rect2)
            if config_2.MP3["crash"].play():
                continue

        else:
            traffic_obj.update_obstacles()
            road.draw_road(screen)
            road.draw_grass(screen)
            traffic_obj.draw(screen)

            elasped_time = (pygame.time.get_ticks() - start_ticka) / 1000
            timer_surf = font.render(f"Timer: {elasped_time:.2f} s", True, (0, 0, 5))
            screen.blit(timer_surf, (330, 35))
            score = int(elasped_time * 5 * 14)
            score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_surf, (330, 65))


        pygame.display.flip()
        clock.tick(60)
