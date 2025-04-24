from roadwork_2 import *
import Utilities
screen = pygame.display.set_mode(resolution)

def main():
    pygame.init()
    user_movement()

if __name__ == "__main__":
    Utilities.display_window(screen)
    Utilities.prep_text()
    Utilities.event_wait()
    main()
