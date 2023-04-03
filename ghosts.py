import pygame as pg 
from pygame.sprite import Sprite, Group


class Ghosts:
    def __init__(self, game):
        self.game = game
        self.ghosts = Group()
        # self.ghost_list = [Blinky(game=game), Inky(game=game), 
        #                    Pinky(game=game), Clyde(game=game)]
        # for ghost in self.ghost_list:
        #     self.ghosts.add(ghost)

        self.ghosts.add(Blinky(game=game))
        self.ghosts.add(Inky(game=game))
        self.ghosts.add(Pinky(game=game))
        self.ghosts.add(Clyde(game=game))

    def update(self): 
        for ghost in self.ghosts:
            if pg.time.get_ticks()>3500:
                ghost.update()
        self.draw()

    def draw(self): 
        for ghost in self.ghosts:
            ghost.draw()


class Ghost(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
    def update(self): pass
    def draw(self): pass


class Blinky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game

        self.size = (27, 27)
        self.imgs = [pg.image.load('images/blinky/sprite_00.png'),
                     pg.image.load('images/blinky/sprite_01.png')]
        for x in range(0, 2):
            self.imgs[x] = pg.transform.scale(self.imgs[x], (self.size[0], self.size[1]))

        self.rect = self.imgs[0].get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.x, self.y = 263, 289
        self.rect.x = self.x
        self.rect.y = self.y

        self.up, self.down, self.left, self.right = False, False, False, False
        self.direction = "Right"

    def update(self):
        if self.direction=="Right":
            self.x += 5
        if self.direction=="Left":
            self.x -= 5
        if self.direction=="Up":
            self.y -= 5
        if self.direction=="Down":
            self.y += 5

        self.rect.x %= 560
        self.rect.y %= 600
        # print(self.x)
        # self.draw()
        
    def draw(self):
        time = pg.time.get_ticks()%200
        if time <= 50:
            self.game.screen.blit(self.imgs[0], self.rect)
        else:
            self.game.screen.blit(self.imgs[1], self.rect)


class Inky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game

        self.size = (27, 27)
        self.imgs = [pg.image.load('images/inky/sprite_00.png'),
                     pg.image.load('images/inky/sprite_01.png')]
        for x in range(0, 2):
            self.imgs[x] = pg.transform.scale(self.imgs[x], (self.size[0], self.size[1]))

        self.rect = self.imgs[0].get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        # self.coor = (300, 500)
        # self.rect.x = self.coor[0]
        # self.rect.y = self.coor[1]

        self.x, self.y = 263+27+3, 289
        self.rect.x = self.x
        self.rect.y = self.y

        self.up, self.down, self.left, self.right = False, False, False, False
        self.direction = "Right"

    def update(self):
        if self.direction=="Right":
            self.x += 1
        if self.direction=="Left":
            self.x -= 1
        if self.direction=="Up":
            self.y -= 1
        if self.direction=="Down":
            self.y += 1

        self.rect.x %= 560
        self.rect.y %= 600

    def draw(self):
        time = pg.time.get_ticks()%200
        if time <= 50:
            self.game.screen.blit(self.imgs[0], self.rect)
        else:
            self.game.screen.blit(self.imgs[1], self.rect)


class Pinky(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game

        self.size = (27, 27)
        self.imgs = [pg.image.load('images/pinky/sprite_00.png'),
                     pg.image.load('images/pinky/sprite_01.png')]
        for x in range(0, 2):
            self.imgs[x] = pg.transform.scale(self.imgs[x], (self.size[0], self.size[1]))

        self.rect = self.imgs[0].get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        # self.coor = (300, 500)
        # self.rect.x = self.coor[0]
        # self.rect.y = self.coor[1]

        self.x, self.y = 263+27+27+3, 289
        self.rect.x = self.x
        self.rect.y = self.y

        self.up, self.down, self.left, self.right = False, False, False, False
        self.direction = "Right"

    def update(self):
        if self.direction=="Right":
            self.rect.x += 1
        if self.direction=="Left":
            self.rect.x -= 1
        if self.direction=="Up":
            self.rect.y -= 1
        if self.direction=="Down":
            self.rect.y += 1

        self.rect.x %= 560
        self.rect.y %= 600
    
    def draw(self):
        time = pg.time.get_ticks()%200
        if time <= 50:
            self.game.screen.blit(self.imgs[0], self.rect)
        else:
            self.game.screen.blit(self.imgs[1], self.rect)


class Clyde(Ghost):
    def __init__(self, game):
        super().__init__(game=game)
        self.game = game

        self.size = (27, 27)
        self.imgs = [pg.image.load('images/clyde/sprite_00.png'),
                     pg.image.load('images/clyde/sprite_01.png')]
        for x in range(0, 2):
            self.imgs[x] = pg.transform.scale(self.imgs[x], (self.size[0], self.size[1]))

        self.rect = self.imgs[0].get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

        self.x, self.y = 263+27+27+27+3, 289
        self.rect.x = self.x
        self.rect.y = self.y

        self.up, self.down, self.left, self.right = False, False, False, False
        self.direction = "Right"

    def update(self):
        if self.direction=="Right":
            self.x += 1
        if self.direction=="Left":
            self.x -= 1
        if self.direction=="Up":
            self.y -= 1
        if self.direction=="Down":
            self.y += 1

        self.rect.x %= 560
        self.rect.y %= 600

        # print(self.rect.x)

    def draw(self):
        time = pg.time.get_ticks()%200
        if time <= 50:
            self.game.screen.blit(self.imgs[0], self.rect)
        else:
            self.game.screen.blit(self.imgs[1], self.rect)
