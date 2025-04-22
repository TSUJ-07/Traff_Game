import pygame
import random
import Car_sounds #import Config

class Meteor:
    def __init__(self):
        self.type = random.choice(list(Car_sounds.Meteor_Speed.keys()))
        self.speed = Car_sounds.Meteor_Speed[self.type]
        self.sprite = pygame.image.load(random.choice(Car_sounds.Meteor_Path[self.type])).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.rect.topleft = (random.randint(326, 1290 - self.rect.width), 0)
        self.spawn_sound = pygame.mixer.Sound(random.choice(Car_sounds.Meteor_Spawn_Sounds))
        self.spawn_sound.play()
    def fall(self):
        self.rect = self.rect.move(0, self.speed)
    def draw(self, surface):
        surface.blit(self.sprite,(self.rect.topleft))