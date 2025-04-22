import pygame

myImage = pygame.image.load(r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\Whimsical-Car-Cartoon-Top-View-Graphic-PNG-300x225.png").convert_alpha()
Image_rect= myImage.get_rect(topleft = (0, 0))
DeathNoise = pygame.mixer.Sound(r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\spongebob-fail.mp3")

class Player:
    def __init__(self):
        self.speed = Car_sounds.SP
        self.sprite = myImage
        self.rect =  self.sprite.get_rect(center=(1080,980))
        self.alive = True
        self.deadSounds = DeathNoise

    def move(self,keys):
        rect_speed = [10,0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)
        if keys[pygame.K_a]:
            if self.rect.x <400:
                print("_")
            else:
                self.rect.x >  30
                rect_speed = [-9, 0]
                self.rect = self.rect.move(rect_speed)
        if keys[pygame.K_d]:
            if self.rect.x > 1100:
                print("_")
            else:
                self.rect.x < 970 - self.rect.width
                rect_speed = [9, 0]
                self.rect = self.rect.move(rect_speed)
        if keys[pygame.K_w]:
            if self.rect.y < 30:
                print("_")
            else:
                self.rect.y <  1885
                rect_speed = [0,-9]
                self.rect = self.rect.move(rect_speed)

        if keys[pygame.K_s]:
            if self.rect.y > 980:
                print("_")
            else:
                self.rect.y > 30 - self.rect.height
                rect_speed = [0, 9]
                self.rect = self.rect.move(rect_speed)
    def draw(self,surface):
        surface.blit(self.sprite,(self.rect.topleft))
import pygame
import Car_sounds #import Config
import sys

myImage = pygame.image.load(r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\Whimsical-Car-Cartoon-Top-View-Graphic-PNG-300x225.png").convert_alpha()
Image_rect= myImage.get_rect(topleft = (0, 0))
DeathNoise = pygame.mixer.Sound(r"C:\Users\panda\PycharmProjects\Traff_Game\GameFolder\sound\crash_sound.mp3")

class Player:
    def __init__(self):
        self.speed = Car_sounds.SP
        self.sprite = myImage
        self.rect =  self.sprite.get_rect(center=(1080,980))
        self.alive = True
        self.deadSounds = DeathNoise

    def move(self,keys):
        rect_speed = [10,0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)
        if keys[pygame.K_a]:
            if self.rect.x <400:
                print("_")
            else:
                self.rect.x >  30
                rect_speed = [-9, 0]
                self.rect = self.rect.move(rect_speed)
        if keys[pygame.K_d]:
            if self.rect.x > 1100:
                print("_")
            else:
                self.rect.x < 970 - self.rect.width
                rect_speed = [9, 0]
                self.rect = self.rect.move(rect_speed)
        if keys[pygame.K_w]:
            if self.rect.y < 30:
                print("_")
            else:
                self.rect.y <  1885
                rect_speed = [0,-9]
                self.rect = self.rect.move(rect_speed)

        if keys[pygame.K_s]:
            if self.rect.y > 980:
                print("_")
            else:
                self.rect.y > 30 - self.rect.height
                rect_speed = [0, 9]
                self.rect = self.rect.move(rect_speed)
    def draw(self,surface):
        surface.blit(self.sprite,(self.rect.topleft))
