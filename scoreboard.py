import pygame as pg 
# import pygame.font

class Scoreboard:
    def __init__(self, game): 
        self.curr_score = 0
        self.curr_level = 1
        self.high_score = 0
        self.d = game.disk
        self.read_disk()

        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (250, 250, 250)
        self.font_type = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.prep_score()

        self.level_image = None 
        self.level_rect = None
        self.prep_level()

        self.next_level()

    def read_disk(self):
        self.hs_1 = self.d["hs_1_score"]
        self.hs_1_lvl = self.d["hs_1_level"]
        self.hs_2 = self.d["hs_2_score"]
        self.hs_2_lvl = self.d["hs_2_level"]
        self.hs_3 = self.d["hs_3_score"]
        self.hs_3_lvl = self.d["hs_3_level"]

    def update_disk(self):
        if self.score > self.hs_1:
            self.d["hs_1_score"] = self.score
            self.d["hs_1_level"] = self.level
            self.d["hs_2_score"] = self.hs_1
            self.d["hs_2_level"] = self.hs_1_lvl
            self.d["hs_3_score"] = self.hs_2
            self.d["hs_3_level"] = self.hs_2_lvl
        elif self.score > self.hs_2:
            self.d["hs_2_score"] = self.score
            self.d["hs_2_level"] = self.level
            self.d["hs_3_score"] = self.hs_2
            self.d["hs_3_level"] = self.hs_2_lvl
        elif self.score > self.hs_3:
            self.d["hs_3_score"] = self.score
            self.d["hs_3_level"] = self.level

    def increment_score(self): 
        self.curr_score += self.settings.food_points
        self.prep_score()
    
    def next_level(self):
        self.curr_level += 1
        self.prep_level()

    def prep_score(self): 
        score_display = "Score: " + str(self.curr_score)
        self.score_image = self.font_type.render(score_display, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        level_display = "Level: " + str(self.curr_level)
        self.level_image = self.font_type.render(level_display, True, self.text_color, self.settings.bg_color)

        # Display the level at the top right of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 50

    def reset(self): 
        self.curr_score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        