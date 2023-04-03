import pygame as pg

class HighScore:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.score_list = []
        self.prep_strings()

    
    def prep_strings(self):
        
        self.prep_Text("High Scores:", 125, offsetY=40)
        
        str1 = "1. Score: " + str(self.game.disk[f"hs_{1}_score"]) + "    Level: " + str(self.game.disk[f"hs_{1}_level"])
        str2 = "2. Score: " + str(self.game.disk[f"hs_{2}_score"]) + "    Level: " + str(self.game.disk[f"hs_{2}_level"])
        str3 = "3. Score: " + str(self.game.disk[f"hs_{3}_score"]) + "    Level: " + str(self.game.disk[f"hs_{3}_level"])

        display_texts = []
        display_texts.append(str1)
        display_texts.append(str2)
        display_texts.append(str3)

        self.prep_Text(display_texts[0], 80, offsetY=200)
        self.prep_Text(display_texts[1], 80, offsetY=300)
        self.prep_Text(display_texts[2], 80, offsetY=400)
    

    def prep_Text(self, msg, size, color=(20,100,255), offsetX=50, offsetY=0):
        font = pg.font.SysFont(None, size)
        text_image = font.render(msg, True, color, self.settings.bg_color)
        rect = text_image.get_rect()
        
        if offsetX == 0:
            rect.centerx = self.screen_rect.centerx
        else:
            rect.left = offsetX
        if offsetY == 0:
            rect.centery = self.screen_rect.centery
        else:
            rect.top = offsetY

        self.score_list.append((text_image,rect))

    def reset(self):
        self.images = []
        self.prep_strings()

    def update(self):
        self.draw()

    def draw(self):
        for image in self.score_list:
            self.screen.blit(image[0], image[1])