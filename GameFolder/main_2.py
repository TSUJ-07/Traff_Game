from roadwork_2 import *
import Utilities, roadwork_2
screen = pygame.display.set_mode(resolution)

def main():
    pygame.init()
    roadwork_2.user_movement()

if __name__ == "__main__":
    Utilities.display_window(screen)
    Utilities.prep_text()
    Utilities.event_wait()
    main()
