from random import randint
import pygame as pg
from maze import Maze
from pacman import Pacman
from ghosts import Ghosts
from fruit import Fruit
from settings import Settings
from sound import Sound
from scoreboard import Scoreboard
import sys

from pygame.sprite import Sprite, Group


class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height  # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pacman Portal")

        # self.sound = Sound(bg_music="sounds/startrek.wav")
        self.scoreboard = Scoreboard(game=self)

        # self.maze = Maze(game=self, file="images/blank_maze.png")
        self.maze = Maze(game=self, file="images/maze_with_points.png")
        self.ghosts = Ghosts(game=self)
        self.fruit = Fruit(game=self)
        self.pacman = Pacman(game=self)
        # self.settings.initialize_speed_settings()

        self.walls = Group()
        self.food = Group()
        self.shield = Group()
        self.portal = Group()

        self.portal_list = []

        self.portal_pairs = dict()

        # self.portal_pairs.add((self.portal_list[0].rect.x,self.portal_list[0].rect.y), (self.portal_list[2].rect.x,self.portal_list[2].rect.y-2))
        # self.portal_pairs.append(self.portal_list[0], (self.portal_list[2].rect.x,self.portal_list[2].rect.y-2))
        


        self.maze.populate_maze()

        self.portal_pairs["Portal_0"] = (126,614)
        self.portal_pairs["Portal_1"] = (318,614)
        self.portal_pairs["Portal_2"] = (561,25)
        self.portal_pairs["Portal_3"] = (42,96)


    def restart(self): pass

    def handle_events(self):
        #TODO handle Pacman movement  -- ghosts move by themselves

        for event in pg.event.get():
            if event.type == pg.QUIT: self.game_over()
            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.pacman.right = False
                elif event.key == pg.K_LEFT:
                    self.pacman.left = False
                elif event.key == pg.K_UP:
                    self.pacman.up = False
                elif event.key == pg.K_DOWN:
                    self.pacman.down = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.pacman.up = True
                elif event.key == pg.K_DOWN:
                    self.pacman.down = True
                elif event.key == pg.K_RIGHT:
                    self.pacman.right = True
                elif event.key == pg.K_LEFT:
                    self.pacman.left = True
                elif event.key == pg.K_SPACE:
                    pass
                elif event.key == pg.K_QUIT:
                    sys.exit()



    def game_over(self):
        # self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        # self.sound.play_bg()
        while True:
            # print(self.pacman.x)
            # print(self.pacman.y)
            # print()
            self.screen.fill(self.settings.black)
            self.handle_events()
            # self.screen.fill(self.settings.bg_color)
            # self.maze.update()
            # print(self.pacman.rect.x)
            # print(self.pacman.rect.y)
            # print()
            self.ghosts.update()
            self.pacman.update()
            self.fruit.update()
            self.maze.check_collisions()
            # self.pacman.draw()
            # self.scoreboard.update()
            for wall in self.walls:
                wall.draw()
            for el in self.shield:
                el.draw()
            for el in self.food:
                el.draw()
            for el in self.portal:
                el.draw()
            pg.display.flip()


            # self.screen.fill(self.settings.black)
            # self.handle_events()
            # self.maze.check_collisions()
            # self.pacman.update()
            # for wall in self.walls:
            #     wall.draw()
            # for el in self.shield:
            #     el.draw()
            # for el in self.food:
            #     el.draw()
            # for el in self.portal:
            #     el.draw()
            # self.pacman.draw()
            # pg.display.flip()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()

