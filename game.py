from random import randint
import pygame as pg
from maze import Maze
from pacman import Pacman
from ghosts import Ghosts
from fruit import Fruit
from settings import Settings
from sound import Sound
from scoreboard import Scoreboard
from startup import StartUp
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
        self.startup = StartUp(self.screen, self.settings)
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

        self.maze.populate_maze()

        self.portal_pairs["Portal_0"] = (126,614)
        self.portal_pairs["Portal_1"] = (318,614)
        self.portal_pairs["Portal_2"] = (561,25)
        self.portal_pairs["Portal_3"] = (42,96)

        self.startup.createScreen(self.screen)
        self.scoreboard.prep_score()
        self.scoreboard.draw()

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
                    self.pacman.rotate(90)
                elif event.key == pg.K_DOWN:
                    self.pacman.down = True
                    self.pacman.rotate(270)
                elif event.key == pg.K_RIGHT:
                    self.pacman.right = True
                    self.pacman.rotate(0)
                elif event.key == pg.K_LEFT:
                    self.pacman.left = True
                    self.pacman.rotate(180)
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
            # if(pg.time.get_ticks()>2000):
            #     self.shield.remove()
            pg.display.flip()


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()

