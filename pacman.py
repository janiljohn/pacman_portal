import pygame as pg

class Pacman:
    def __init__(self, game):
        self.game = game
        self.size = (27, 27)
        self.imgs = [pg.image.load('images/pacman/sprite_0.png'),
                     pg.image.load('images/pacman/sprite_1.png'),
                     pg.image.load('images/pacman/sprite_2.png'),
                     pg.image.load('images/pacman/sprite_3.png')]
        for x in range(0, 4):
            self.imgs[x] = pg.transform.scale(self.imgs[x], (self.size[0], self.size[1]))

        self.rect = self.imgs[0].get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.x, self.y = 300, 500
        self.rect.x = self.x
        self.rect.y = self.y

        self.up, self.down, self.left, self.right = False, False, False, False
        self.direction = "Right"

    def update(self):
        if self.right:
            self.x += self.game.settings.pacmanspeed
        if self.left:
            self.x -= self.game.settings.pacmanspeed
        if self.up:
            self.y -= self.game.settings.pacmanspeed
        if self.down:
            self.y += self.game.settings.pacmanspeed
        self.rect.x = self.x
        self.rect.y = self.y

        self.draw()

    def rotate(self, degree=0):
        print(degree)
        self.imgs = [pg.image.load('images/pacman/sprite_0.png'),
                     pg.image.load('images/pacman/sprite_1.png'),
                     pg.image.load('images/pacman/sprite_2.png'),
                     pg.image.load('images/pacman/sprite_3.png')]
        for x in range(0, 4):
            self.imgs[x] = pg.transform.scale(self.imgs[x], (self.size[0], self.size[1]))
        for x in range(0, 4):
            self.imgs[x] = pg.transform.rotate(self.imgs[x], degree)
        
    def draw(self):
        time = pg.time.get_ticks()%200
        if time <= 50:
            self.game.screen.blit(self.imgs[0], self.rect)
        elif time <= 100:
            self.game.screen.blit(self.imgs[1], self.rect)
        elif time <=150:
            self.game.screen.blit(self.imgs[2], self.rect)
        else:
            self.game.screen.blit(self.imgs[3], self.rect)
