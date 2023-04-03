import pygame as pg

class Button():
    def __init__(self, msg, game, movex=0, movey=0):
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width = 200
        self.height = 50
        self.text_color = (255, 255, 255)
        self.button_color = (31, 105, 224)
        self.font = pg.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centerx = self.screen_rect.centerx + movex
        self.rect.centery = self.screen_rect.centery + movey
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_draw = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_draw_rect = self.msg_draw.get_rect()
        self.msg_draw_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_draw, self.msg_draw_rect)