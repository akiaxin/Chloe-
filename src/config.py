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
dark_red = (126, 8, 8)

mtndew = (87, 255, 72)
yebbow = (253, 255, 0)
eyesore = (253, 0, 255)

map = [
    "BBBBBBBBBBBBBBBBBBBB",
    "B................B.B",
    "B.........BBBB..BB.B",
    "B....BB.....B.B....B",
    "B....B...BB.B.B.BB.B",
    "B........B.B..B....B",
    "B........B.B..BBBBBB",
    "B........BP.B.B....B",
    "B....B...BB...B.BB.B",
    "B................B.B",
    "B..............B.B.B",
    "B.......B..........B",
    "B..................B",
    "B..................B",
    "BBBBBBBBBBBBBBBBBBBB",
]