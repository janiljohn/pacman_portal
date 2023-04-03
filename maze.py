import pygame as pg
from wall import Wall
from shield import Shield
from fruit import Fruit
from portal import Portal
from powerpill import PowerPill
import random

class Maze:
    def __init__(self, game, file):
        self.game = game
        self.screen = game.screen
        self.file = file
        self.image = pg.transform.rotozoom(pg.image.load(file), 0, 1.2)

    def update(self):
        # TODO -- update maze as necessary to show points being eaten
        self.draw()

    def draw(self):
        # rect = self.image.get_rect()
        # self.screen.blit(self.image, rect)
        self.screen.fill(000000)
        self.populate_maze()

    def populate_maze(self):
        file = open("layout.txt", "r")
        order = file.read()
        rows = []
        curr_row = []
        for el in order:
            if el != '\n':
                curr_row.append(el)
            else:
                rows.append(curr_row)
                curr_row = []

        offset_horizontal = 0
        offset_vertical = 0

        for row in rows:
            for el in row:
                if el == 'W':
                    new_wall = Wall(self.game)
                    new_wall.rect.x = 13 * offset_horizontal
                    new_wall.rect.y = 13 * offset_vertical
                    (self.game.walls).add(new_wall)
                elif el == 'f':
                    new_fruit = Fruit(self.game)
                    new_fruit.rect.x = 13 * offset_horizontal
                    new_fruit.rect.y = 13 * offset_vertical
                    (self.game.food).add(new_fruit)
                elif el == 'o':
                    new_shield = Shield(self.game)
                    new_shield.rect.x = 12.7 * offset_horizontal
                    new_shield.rect.y = 12.5 * offset_vertical
                    (self.game.shield).add(new_shield)
                elif el == 'h':
                    pass
                elif el == 'P':
                    new_portal = Portal(self.game)
                    new_portal.rect.x = 13 * offset_horizontal
                    new_portal.rect.y = 13 * offset_vertical
                    (self.game.portal).add(new_portal)
                    (self.game.portal_list).append(new_portal)
                elif el == 'p':
                    new_powerpill = PowerPill(self.game)
                    new_powerpill.rect.x = 13 * offset_horizontal
                    new_powerpill.rect.y = 13 * offset_vertical
                    (self.game.food).add(new_powerpill)
                offset_horizontal += 1
            offset_horizontal = 0
            offset_vertical += 1

    def check_collisions(self):
        for wall in self.game.walls:
            if pg.sprite.collide_rect(self.game.pacman, wall):
                self.check_pacman_wall_collisions(wall)
        for shield in self.game.shield:
            if pg.sprite.collide_rect(self.game.pacman, shield) and pg.time.get_ticks()<3500:
                self.check_pacman_shield_collisions(shield)
        for food in self.game.food:
            if pg.sprite.collide_rect(self.game.pacman, food):
                print("Eaten")
                (self.game.food).remove(food)
        for portal in self.game.portal:
            if pg.sprite.collide_rect(self.game.pacman, portal):
                if self.game.pacman.rect.x>=536 and self.game.pacman.rect.x<=580:
                    self.game.pacman.x = self.game.portal_pairs["Portal_0"][0]
                    self.game.pacman.y = self.game.portal_pairs["Portal_0"][1]
                elif self.game.pacman.rect.x>=20 and self.game.pacman.rect.x<=91:
                    self.game.pacman.x = self.game.portal_pairs["Portal_1"][0]
                    self.game.pacman.y = self.game.portal_pairs["Portal_1"][1]
                elif self.game.pacman.rect.x>=99 and self.game.pacman.rect.x<=160:
                    self.game.pacman.x = self.game.portal_pairs["Portal_2"][0]
                    self.game.pacman.y = self.game.portal_pairs["Portal_2"][1]
                elif self.game.pacman.rect.x>=279 and self.game.pacman.rect.x<=360:
                    self.game.pacman.x = self.game.portal_pairs["Portal_3"][0]
                    self.game.pacman.y = self.game.portal_pairs["Portal_3"][1]

    def check_pacman_wall_collisions(self, wall):
        if self.game.pacman.rect.centerx <= wall.rect.centerx:
            self.game.pacman.x -= 1
        else:
            self.game.pacman.x += 1
        if self.game.pacman.rect.y + self.game.pacman.rect.height / 2 <= wall.rect.y + wall.rect.height / 2:
            self.game.pacman.y -= 1
        else:
            self.game.pacman.y += 1

    def check_pacman_shield_collisions(self, shield):
        if self.game.pacman.rect.centerx <= shield.rect.centerx:
            self.game.pacman.x -= 1
        else:
            self.game.pacman.x += 1
        if self.game.pacman.rect.y + self.game.pacman.rect.height / 2 <= shield.rect.y + shield.rect.height / 2:
            self.game.pacman.y -= 1
        else:
            self.game.pacman.y += 1
        

