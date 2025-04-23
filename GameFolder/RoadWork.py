import pygame, Config
pygame.init()
#Background and Grass filling for game

class Road_Work:
    def __init__(self):
        self.grass_left= pygame.Rect(0,0,Config.GRASS, Config.RESOLUTION[1])
        self.grass_surface= pygame.Surface((Config.GRASS, Config.RESOLUTION[1]))

        # py.Rect(x,y,width,height); its just expanded,
        # don't freak out guys
        self.grass_right= pygame.Rect(
            Config.RESOLUTION[0] - Config.GRASS, #x
            0, #y
            Config.GRASS, #width for object
            Config.RESOLUTION[1] #height we want for object
        )

        self.grass_surf2= pygame.Surface((Config.GRASS, Config.RESOLUTION[1]))
        self.grass_surf2.fill(Config.GREEN)

    def grass_draw(self,screen):
        screen.fill(Config.BLACK)
        screen.blit(self.grass_surface, self.grass_left.topleft)
        screen.blit(self.grass_surf2, self.grass_right.topleft)