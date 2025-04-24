import pygame, sys, Config, Cars_Obstacle, Player, RoadWork, HighScore
from pygame.locals import *
#This is just a template for the window
# Discard anything that is not related to the game
#Changes can also be made through GitHub without the use of PyCharm
#Always remember to 'commit' when finished writing code so the entire source is updated

pygame.init()
pygame.display.set_caption("Traffic_Game")
FPS= Config.FPS
screen= pygame.display.set_mode(Config.RESOLUTION)
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
def prep_text(message= "PRESS ANY KEY TO START", size= 25, color= white, y_scale= 2):
    fonting = pygame.font.Font(None, size)
    render_text = fonting.render(message, True, color)
    shade_window = render_text.get_rect(midtop= (screen.get_width() // 2, screen.get_height() // y_scale))
    screen.blit(render_text, shade_window)
    pygame.display.flip()

#In event log
def event_wait():
    while True:
        for i in pygame.event.get(): #Event handling to start game
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif i.type == pygame.KEYDOWN: #any key pressed then we start up game
                return #Enter start-up sound --> {Config.MP3["start"].play()}

def record(player, collide_list, score= 0):
    high_score= HighScore.load_high_score()
    if player.collide_check(collide_list) and score > high_score:
        high_score = score
        HighScore.save_high_score(high_score)
        prep_text("You Have Crashed!!!", size= 48, color= Config.RED, y_scale= 1)
        prep_text(f"High Score: {high_score}", size=32, color= white)

def failure(): #Created to search options between KEY_r and KEY_q to exit or restart game!!
    prep_text("Press [R] to Restart -- Press [Q] to Quit", y_scale= 3)
    while True:
        for event in pygame.event.get(): #event handling for only the restart and quit option
            if event.type == pygame.QUIT:
                pygame.quit()
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
    player= Player.User()
    road= RoadWork.Road_Work()
    pygame.time.set_timer(Config.XEVENT, 1000)

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif i.type == Config.XEVENT:
                collide_list.append(Cars_Obstacle.Obstacle()) #add car to collide list

        keys = pygame.key.get_pressed()
        player.move_user(keys)
        if player.collide_check(collide_list):
            display_window(screen)  # Display cover
            #Enter Failure sound --> {Config.MP3["failure"].play()}
            record(player, collide_list) # Highscore
            failure()
            question= failure()
            if question == "Restart":
                return game_loop()
            else:
                pygame.quit()
                sys.exit(0)

        pygame.display.flip()
        timer.tick(FPS)
print("Thanks for playing!")