import pygame
from pygame.sprite import Sprite

class Fruit(Sprite):
    def __init__(self, game):
        super(Fruit, self).__init__()
        self.screen = game.screen
        self.size = (7, 7)
        fruit_img = pygame.image.load('images/maze/fruit.png')
        fruit_img = pygame.transform.scale(fruit_img, (self.size[0], self.size[1]))
        self.game = game
        self.image = fruit_img
        self.rect = fruit_img.get_rect()        

    def update(self): pass
    def draw(self):
        self.screen.blit(self.image, self.rect)