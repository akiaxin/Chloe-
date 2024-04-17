import pygame
import sys
from config import *
from button import Button
from characters import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        pygame.display.set_caption("Game!!!")


    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.createMap()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False


    def createMap(self):
        for i, row in enumerate(map):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)


    def update(self):
        self.all_sprites.update()


    def draw(self):
        self.screen.fill(black)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.running = False
    

    def start_screen(self):
        start_img = pygame.image.load("images/start.png").convert_alpha()
        start_button = Button(100, 200, start_img, 5)

        while not self.playing:
            self.events()
            self.screen.fill(dark_red)
            if start_button.draw(self.screen):
                print("you clicked da button!")
                self.new()
                self.playing = True
            pygame.display.update()



    def game_over(self):
        pass


g = Game()
g.start_screen()

while g.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
        if g.playing:
            g.main()
        g.game_over()

pygame.quit()
sys.exit()