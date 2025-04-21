import pygame, sys, Config, Cars_Obstacle, Player, RoadWork
from pygame.locals import *
#This is just a template for the window
# Discard anything that is not related to the game
#Changes can also be made through Github without the use of PyCharm
#Always remember to 'commit' when finished writing code so the entire source is updated

pygame.init()
pygame.display.set_caption("Traffic_Game")
FPS= Config.FPS
resolution= Config.RESOLUTION
screen= pygame.display.set_mode(resolution)
timer= pygame.time.Clock()
black= Config.BLACK
blue= Config.BLUE
white= Config.WHITE


#Reusable alpha screen for transparency
#Not creating buttons to click on the screen, that's so difficult, so tedious
def display_window(screen):
    var = pygame.Surface(screen.get_size())
    var.set_alpha(100)
    var.fill((128,128,128))
    screen.blit(var, (0,0))

#getting font for transparent start-up window OR any text_layout for the screen; centered
def prep_text(message= "PRESS ANY KEY TO START"):
    fonting = pygame.font.Font(None, 25)
    render_text = fonting.render(message, True, white)
    shade_window = render_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(render_text, shade_window)
    pygame.display.flip()

#In event log
def event_wait():
    while True:
        for i in pygame.event.get(): #Event handling to start game
            if i.type == pygame.QUIT:
                pygame.quit()
                print("Thanks for playing")
                sys.exit(0)
            elif i.type == pygame.KEYDOWN: #any key pressed then we start up game
                #Enter start-up sound
                return
def failure(): #Created to search options between KEY_r and KEY_q to exit or restart game!!
    display_window(screen) #Display cover
    prep_text("Press [R] to Restart -- Press [Q] to Quit")
    while True:
        for event in pygame.event.get(): #event handling for only the restart and quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Thanks for playing")
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == pygame.K_r:
                    return "Restart"
                elif event.key == pygame.K_q:
                    return "Quit"

#-----MAIN-----#
display_window(screen)
prep_text()
event_wait()
def game_loop():
    collide_list = []
    Player.User= Player.User()
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                print("Thanks for playing")
                sys.exit(0)
            if Player.User.collide_check(collide_list):
                question= failure()
                if question == "Restart":
                    game_loop()
                else:
                    pygame.quit()
                    print("Thanks for playing")
                    sys.exit(0)
        pygame.display.flip()
        timer.tick(FPS)