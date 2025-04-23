from GameFolder import HighScore
import pygame
import PlayerA
import Meteor
import random
from GameFolder.HighScore import save_high_score

pygame.init()
pygame.mixer.init()
pygame.time.get_ticks()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1600, 1080))

Meteor_Event = pygame.USEREVENT + 1
pygame.time.set_timer(Meteor_Event, 1000)

BG = pygame.image.load(r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\road_0.png").convert_alpha()
BG_rect = BG.get_rect(topleft=(1600, 1080))

# L_surf = pygame.Surface((1080,1800))
# L_surf.set_alpha(100)
# L_surf.fill((0,0,0))


meteors = []

pygame.display.set_caption("Timer:")

font = pygame.font.Font(None, 36)

start_ticks = pygame.time.get_ticks()

pygame.display.set_caption("ANIME X TRAFF")

score = 0

high_score = HighScore.load_high_score()

player = PlayerA.Player()

running = True

while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == Meteor_Event:
            meteor = Meteor.Meteor()
            meteors.append(meteor)
            meteor.spawn_sound.play()
            pygame.time.set_timer(Meteor_Event, random.randint(250, 500))
            pass

    screen.blit(BG, (260, 0))

    for meteor in meteors:
        meteor.draw(screen)
        meteor.fall()
        if meteor.rect.y > 1050:
            meteors.remove(meteor)
        if meteor.rect.colliderect(player):
            player.alive = False
            meteors.remove(meteor)
            player.deadSounds.play()

    player.move(keys)
    if not player.alive:

        if score > high_score:
            high_score = score
            save_high_score(high_score)

        L_surf = pygame.Surface((1600, 1080))
        L_surf.set_alpha(100)
        L_surf.fill((0, 0, 0))
        screen.blit(L_surf, (0, 0))
        font = pygame.font.Font(None, 48)
        text_surf = font.render("You Have Crashed!!!", True, (255, 255, 255))
        text_surf2 = font.render(f"Your Score is: {score}", True, (255, 255, 255))
        high_score_surf = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        text_rect = text_surf.get_rect(midtop=(screen.get_width() / 2, screen.get_height() / 2))
        text_rect2 = text_surf.get_rect(midtop=(screen.get_width() / 2, screen.get_height() / 3))
        high_score_rect = text_surf.get_rect(midtop=(screen.get_width() / 2, screen.get_height() / 4))
        screen.blit(high_score_surf, high_score_rect)
        screen.blit(text_surf, text_rect)
        screen.blit(text_surf2, text_rect2)

        if score > high_score:
            high_score = score
            save_high_score(high_score)


    else:
        player.draw(screen)
        elasped_time = (pygame.time.get_ticks() - start_ticks) / 1000
        timer_surf = font.render(f"Timer: {elasped_time:.2f} s", True, (255, 255, 255))
        screen.blit(timer_surf, (1150, 60))
        score = int(elasped_time * 5 * 14)
        score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_surf, (1150, 120))

    pygame.display.flip()
    clock.tick(60)
