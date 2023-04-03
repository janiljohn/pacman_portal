# import pygame as pg

# class Button():
#     def __init__(self, msg, game, offsetx=0, offsety=0):
#         self.game = game
#         self.screen = self.game.screen
#         self.screen_rect = self.screen.get_rect()

#         # Set the dimensions and properties of the button.
#         self.width, self.height = 200, 50
#         self.button_color = (31, 105, 224)
#         self.text_color = (255, 255, 255)
#         self.font = pg.font.SysFont(None, 48)

#         # Build the button's rect object and center it.
#         self.rect = pg.Rect(0, 0, self.width, self.height)
#         self.rect.center = self.screen_rect.center
#         self.rect.centerx = self.screen_rect.centerx + offsetx
#         self.rect.centery = self.screen_rect.centery + offsety

#         # The button message needs to be prepped only once.
#         self.button_msg = msg
#         self.prep_msg(msg)

#     def prep_msg(self, msg):
#         self.msg_image = self.font.render(msg, True, self.text_color,
#         self.button_color)
#         self.msg_image_rect = self.msg_image.get_rect()
#         self.msg_image_rect.center = self.rect.center
    
#     def draw_button(self):
#         # Draw blank button and then draw message.
#         self.screen.fill(self.button_color, self.rect)
#         self.screen.blit(self.msg_image, self.msg_image_rect)

#     def hover_on(self):
#         self.button_color = (255,0,0)
#         self.msg_image = self.font.render(self.button_msg, True, self.text_color,
#         self.button_color)
#         self.msg_image_rect = self.msg_image.get_rect()
#         self.msg_image_rect.center = self.rect.center
#         self.draw_button()

#     def hover_off(self):
#         self.button_color = (0,255,0)
#         self.msg_image = self.font.render(self.button_msg, True, self.text_color,
#         self.button_color)
#         self.msg_image_rect = self.msg_image.get_rect()
#         self.msg_image_rect.center = self.rect.center
#         self.draw_button()

import pygame as pg

class Button():
    def __init__(self, msg, game, movex=0, movey=0):
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width = 200
        self.height = 50
        self.button_color = (31, 105, 224)
        self.text_color = (255, 255, 255)
        self.font = pg.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centerx = self.screen_rect.centerx + movex
        self.rect.centery = self.screen_rect.centery + movey

        # The button message needs to be prepped only once.
        self.button_msg = msg
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_draw = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_draw_rect = self.msg_draw.get_rect()
        self.msg_draw_rect.center = self.rect.center
    
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_draw, self.msg_draw_rect)

    def hover_on(self):
        self.button_color = (255,0,0)
        self.msg_image = self.font.render(self.button_msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.draw_button()

    def hover_off(self):
        self.button_color = (0,255,0)
        self.msg_image = self.font.render(self.button_msg, True, self.text_color,
        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        self.draw_button()