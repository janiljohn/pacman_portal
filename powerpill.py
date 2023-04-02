import pygame
from pygame.sprite import Sprite

class PowerPill(Sprite):
    def __init__(self, game):
        super(PowerPill, self).__init__()
        self.screen = game.screen
        self.size = (20, 20)
        powerpill_img = pygame.image.load('images/powerpill.png')
        powerpill_img = pygame.transform.scale(powerpill_img, (self.size[0], self.size[1]))
        self.game = game
        self.image = powerpill_img
        self.rect = powerpill_img.get_rect()        

    def update(self): pass
    def draw(self):
        self.screen.blit(self.image, self.rect)