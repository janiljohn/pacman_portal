import pygame
from pygame.sprite import Sprite

class Shield(Sprite):
    def __init__(self, game):
        super(Shield, self).__init__()
        self.screen = game.screen
        self.size = (35, 35)
        shield_img = pygame.image.load('images/maze/shield.png')
        shield_img = pygame.transform.scale(shield_img, (self.size[0], self.size[1]))
        self.game = game
        self.image = shield_img
        self.rect = shield_img.get_rect()

    def update(self): pass
    def draw(self):
        self.screen.blit(self.image, self.rect)