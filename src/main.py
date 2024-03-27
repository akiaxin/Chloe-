import pygame
import sys
from button import Button
from config import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        pygame.display.set_caption("Game!")

        start_img = pygame.image.load("images/start.png").convert_alpha()
        start_button = Button(100, 200, start_img, 0.5)


    def new(self):
        self.playing = True


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False


    def update(self):
        pass


    def draw(self):
        self.screen.fill(black)
        self.clock.tick(FPS)
        pygame.display.update()

    
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.running = False
    

    def start_screen(self):
        if start_button.draw():
            pass



    def game_over(self):
        pass


g =  Game()
g.start_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()