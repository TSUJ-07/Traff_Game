import pygame, Config
pygame.init()

class Player:
    def __init__(self):
        self.rect= pygame.Rect(
            Config.PLAYER_POS[0],
            Config.PLAYER_POS[1],
            Config.PLAYER_WIDTH,
            Config.PLAYER_HEIGHT
        )
        self.player_surf= pygame.Surface((Config.PLAYER_WIDTH, Config.PLAYER_HEIGHT))
        self.player_surf.fill(Config.BLUE)
        self.player_speed= Config.PLAYER_SPEED
        self.roam= True

    def move_user(self, keys):
        if keys[pygame.K_a] and self.rect.x > Config.GRASS:
            self.rect.x -= self.player_surf
        if keys[pygame.K_d] and self.rect.x < Config.BOUND_ON_RIGHT:
            self.rect.x += self.player_speed

    def collide_check(self, collide_list):
        for car in collide_list:
            if self.rect.colliderect(car.rect):
                self.roam = False
                return True #Function is True; COLLISION
            else:
                return False #Function remains False; NO COLLISION

    # def game_restart(): #If restart button is pressed
    #     self.rect.x= Config.PLAYER_POS[0]
    #     self.rect.y= Config.PLAYER_POS[1]
    #     self.roam= True

    def player_draw(self,screen):
        screen.blit(self.player_surf, self.rect.topleft)