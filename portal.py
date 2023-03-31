import pygame
from pygame.sprite import Sprite

class Portal(Sprite):
    def __init__(self, game):
        super(Portal, self).__init__()
        self.screen = game.screen
        self.size = (7, 7)
        portal_img = pygame.image.load('images/maze/portal.png')
        portal_img = pygame.transform.scale(portal_img, (self.size[0], self.size[1]))
        self.game = game
        self.image = portal_img
        self.rect = portal_img.get_rect()        

    def update(self): pass
    def draw(self):
        self.screen.blit(self.image, self.rect)