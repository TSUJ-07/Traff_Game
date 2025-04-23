from roadwork_2 import *
import config_2

screen = pygame.display.set_mode(resolution)
road = RoadWork(resolution, 50, (0, 255, 0))

def display_window(screen):
    var = pygame.Surface(screen.get_size())
    var.set_alpha(100)
    var.fill((128,128,128))
    screen.blit(var, (0,0))

#getting font for transparent start-up window OR any text_layout for the screen; centered
def prep_text(message= "PRESS ANY KEY TO START", size= 25, color= config_2.white, y_scale= 2):
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
                return config_2.MP3["start"].play()

def main():
    pygame.init()
    user_movement()

if __name__ == "__main__":
    display_window(screen)
    prep_text()
    event_wait()
    main()
