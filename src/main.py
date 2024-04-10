import pygame
import sys
from config import *
from button import Button

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
        start_img = pygame.image.load("images/start.png").convert_alpha() # having an issue right now: if I type src/images/start.png, it works in here but not the terminal; if I just have images/start.png it works in the terminal but not here. ??
        start_button = Button(100, 200, start_img, 5)

        while not self.playing:
            self.events()
            self.screen.fill(dark_red)
            if start_button.draw(self.screen):
                print("you clicked da button!")
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