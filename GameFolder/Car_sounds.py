import pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((480,800))


#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

SP = 12
SPRI = r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\Whimsical-Car-Cartoon-Top-View-Graphic-PNG-300x225.png"

DS = r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\spongebob-fail.mp3"
BackGround = r"C:\Users\panda\PycharmProjects\5HourGrind\.venv\Scripts\bg.png"
Meteor_Speed = {
    "big": 5,
    "medium": 6,
    "small":6,
    "tiny":7,
}
Meteor_Path = {
    "big":[r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\R (1).png"],
    "medium":[r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\UI-Goku-Striking-Pose-Energy-PNG.png"],
    "small":[r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\PCar.png",r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\vecteezy_sport-car-isolated-on-transparent-background-3d-rendering_19612927.png",r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\vecteezy_white-sport-car-on-transparent-background-3d-rendering_25308299.png"],
    "tiny":[r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\—Pngtree—red sports car top view_8950912.png", r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\—Pngtree—f1 car top view_2960088.png"],
}
Meteor_Spawn_Sounds = [
    r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\myinstants.mp3",
    r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\dragon_ball_z_tele.mp3",
    r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\xenoverse-goku-noise.mp3",
    r"C:\Users\panda\PycharmProjects\PythonProject21\.venv\Scripts\audiocutter_ultra-instinct-theme-official-version.mp3"
]
