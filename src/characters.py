import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize
        #self.facing

        self.x_change = 0
        self.y_change = 0

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(red)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.collision('x')
        self.rect.y += self.y_change
        self.collision('y')

        self.x_change = 0
        self.y_change = 0


    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change = -player_speed
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change = player_speed
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change = -player_speed
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change = player_speed
            self.facing = 'down'
        # if keys[pygame.KMOD_LSHIFT] or keys[pygame.KMOD_RSHIFT]: # this doesn't work
        #     self.x_change *= 4
        #     self.y_change *= 4

    def collision(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = block_layer
        self.groups = self.game.all_sprites, self.game.blocks

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * tilesize
        self.y = y * tilesize
        self.width = tilesize
        self.height = tilesize

        self.image = pygame.Surface([self.width, self.height]) 
        self.image.fill(yebbow)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    