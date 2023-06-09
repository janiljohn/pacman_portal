import pygame
from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self, game):
        super(Wall, self).__init__()
        self.screen = game.screen
        self.size = (15, 15)
        wall_img = pygame.image.load('images/maze/square.png')
        wall_img = pygame.transform.scale(wall_img, (self.size[0], self.size[1]))
        self.game = game
        self.image = wall_img
        self.rect = wall_img.get_rect()        

    def update(self): pass
    def draw(self):
        self.screen.blit(self.image, self.rect)