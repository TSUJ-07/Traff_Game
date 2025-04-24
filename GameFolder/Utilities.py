from roadwork_2 import *
import config_2

screen = pygame.display.set_mode(config_2.resolution)

def display_window(screen):
    var = pygame.Surface(screen.get_size())
    var.set_alpha(100)
    var.fill((128,128,128))
    screen.blit(var, (0,0))

#getting font
def prep_text(message= "PRESS ANY KEY TO START", size= 25, color= config_2.white, y_scale= 2):
    fonting = pygame.font.Font(None, size)
    render_text = fonting.render(message, True, color)
    shade_window = render_text.get_rect(midtop=(screen.get_width() // 2, screen.get_height() // y_scale))
    screen.blit(render_text, shade_window)
    pygame.display.flip()

#event log
def event_wait():
    while True:
        for i in pygame.event.get(): #Event handling to start game
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif i.type == pygame.KEYDOWN: #any key pressed then we start up game
                return config_2.MP3["start"].play()

# def record(player, collide_list, score= 0):
#     high_score= HighScore.load_high_score()
#     if player.collide_check(collide_list) and score > high_score:
#         high_score = score
#         HighScore.save_high_score(high_score)
#         prep_text(f"High Score: {high_score}", size=32, color= white)

def failure(): #Created to search options between KEY_r and KEY_q to exit or restart game!!
    prep_text("You Have Crashed!!!", size=48, color=config_2.red, y_scale=4)
    prep_text("Press [R] to Restart -- Press [Q] to Quit", size= 32, y_scale= 3)
    while True:
        for event in pygame.event.get(): #event handling for only the restart and quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "Restart"
                if event.key == pygame.K_q:
                    return "Quit"
# record(player, collide_list) # Highscore