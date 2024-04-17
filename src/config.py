import pygame

screen_size = (640, 480)
tilesize  = 32
FPS = 60

block_layer = 1
player_layer = 2

player_speed = 5

black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
dark_red = (150, 0, 0)

map = [
    "BBBBBBBBBBBBBBBBBBBB",
    "B..................B",
    "B..................B",
    "B....BB............B",
    "B....B.............B",
    "B..................B",
    "B..................B",
    "B.........P........B",
    "B..............B...B",
    "B..............B...B",
    "B.............BB...B",
    "B..................B",
    "B..................B",
    "B..................B",
    "BBBBBBBBBBBBBBBBBBBB",
]