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
from highscorepage import HighScore
from button import Button
import sys
import shelve

from pygame.sprite import Sprite, Group

# d = shelve.open('score.txt')  
# d['score'] = 0            
# d['hs_1_score'] = 0           
# d['hs_1_level'] = 1      
# d['hs_2_score'] = 0           
# d['hs_2_level'] = 1     
# d['hs_3_score'] = 0           
# d['hs_3_level'] = 1             
# d.close()

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.disk = shelve.open('score.txt')
        size = self.settings.screen_width, self.settings.screen_height  # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Pacman Portal")

        # self.sound = Sound(bg_music="sounds/startrek.wav")
        self.play_button = Button( "Play", game=self, offsety=200)
        self.hs_button = Button( "High Score", game=self, offsety=280)
        self.back_button = Button( "Back", game=self, offsety=280)
        self.hs = HighScore(game=self)
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
        # self.scoreboard.prep_score()
        # self.scoreboard.draw()

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
        self.scoreboard.update_disk()
        pg.quit()
        sys.exit()

    def check_buttons(self, mouse_x, mouse_y):
        if not self.settings.game_active:
            if not self.settings.hs_active:
                self.check_hs_button(mouse_x, mouse_y)
                self.check_play_button(mouse_x, mouse_y)
            else:
                self.check_back_button(mouse_x, mouse_y)

    def check_back_button(self, mouse_x, mouse_y):
        button_clicked = self.back_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.scoreboard.reset()
            self.settings.hs_active = False

    def check_hs_button(self, mouse_x, mouse_y):
        button_clicked = self.hs_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.scoreboard.reset()
            self.settings.hs_active = True

    def check_play_button(self, mouse_x, mouse_y):
        button_clicked = self.play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.settings.init_speeds()
            self.sound.play_bg()
            pg.mouse.set_visible(False)

            self.scoreboard.reset()
            self.settings.game_active = True

            self.scoreboard.prep_score()
            

    def update_screen(self):

        if not self.settings.game_active:
            # self.space_text.draw_button()
            # self.invaders_text.draw_button()
            self.sound.stop_bg()
            if self.settings.hs_active:
                self.hs.update()
                self.back_button.draw_button()
            else:
                self.launch.update()
                self.play_button.draw_button()
                self.hs_button.draw_button()


    def play(self):
        # self.sound.play_bg()
        while True:
            self.screen.fill(self.settings.black)
            self.handle_events()
            self.ghosts.update()
            self.pacman.update()
            self.fruit.update()
            self.maze.check_collisions()
            self.scoreboard.update()
            for wall in self.walls:
                wall.draw()
            if(pg.time.get_ticks()<3500):
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

