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

        self.maze.populate_maze()


    def restart(self): pass

    def handle_events(self):
        #TODO handle Pacman movement  -- ghosts move by themselves

        for event in pg.event.get():
            if event.type == pg.QUIT: self.game_over()

    def game_over(self):
        # self.sound.gameover()
        pg.quit()
        sys.exit()

    def play(self):
        # self.sound.play_bg()
        while True:
            self.handle_events()
            self.screen.fill(self.settings.bg_color)
            self.maze.update()
            self.ghosts.update()
            self.pacman.update()
            self.fruit.update()
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


def main():
    g = Game()
    g.play()


if __name__ == '__main__':
    main()
