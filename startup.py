# import pygame
# import pygame.font

# from pygame.sprite import Group
# from settings import Settings

# # Globals for ease
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)


# class StartUp():
#     def __init__(self, screen, settings):
#         self.screen = screen
#         self.settings = settings
#         self.screen_rect = screen.get_rect()

#         # Load in ghost images
#         self.ghost1 = pygame.image.load('images/blinky/sprite_00.png')
#         self.ghost2 = pygame.image.load('images/pinky/sprite_00.png')
#         self.ghost3 = pygame.image.load('images/clyde/sprite_00.png')
#         self.ghost4 = pygame.image.load('images/inky/sprite_00.png')
#         self.ghost5 = pygame.image.load('images/panic_ghost/sprite_0.png')

#         # Load in Pacman image
#         self.height = 125
#         self.width = 125
#         img = pygame.image.load('images/pacman/sprite_1.png')
#         img = pygame.transform.scale(img, (self.height, self.width))
#         self.rect = img.get_rect()
#         self.rect.x, self.rect.y = 310, 515
#         self.rect.left -= self.rect.width
#         self.rect.top -= self.rect.height
#         self.pacmanimage = img
#         self.rect = self.pacmanimage.get_rect()

#         self.text_color = (30, 30, 30)
#         self.font = pygame.font.SysFont(None, 48)

#         screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
#         screen.fill(BLACK)

#     def createScreen(self, screen):
#         pygame.init()
#         pygame.display.set_caption("PACMAN")

#         backgroundpage = pygame.Surface(screen.get_size())
#         backgroundpage = backgroundpage.convert()
#         backgroundpage.fill(BLACK)

#         # Display P in front of the PACMAN pic
#         font = pygame.font.Font(None, 144)
#         text1 = font.render("PA", 2, WHITE)
#         textpos1 = text1.get_rect()
#         textpos1 = ((self.settings.screen_width / 2) - 300, (self.settings.screen_height / 8) - 75)
#         font = pygame.font.Font(None, 144)

#         # Display "CMAN" after the PACMAN pic
#         text2 = font.render("MAN", 2, WHITE)
#         textpos2 = text2.get_rect()
#         textpos2 = ((self.settings.screen_width / 2), (self.settings.screen_height / 8) - 75)

#         # Ghosts position and text
#         font = pygame.font.Font(None, 44)
        
#         # Red Ghost
#         text3 = font.render(" BLINKY", 2, (250, 250, 250))
#         textpos3 = text3.get_rect()

#         # Pink Ghost        
#         text4 = font.render(" PINKY", 2, (250, 250, 250))
#         textpos4 = text4.get_rect()

#         # Orange Ghost
#         text5 = font.render(" INKY", 2, (250, 250, 250))
#         textpos5 = text5.get_rect()

#         # Cyan Ghost
#         text6 = font.render(" CLYDE", 2, (250, 250, 250))
#         textpos6 = text6.get_rect()
        
#         # Red Ghost position
#         textpos3 = ((self.settings.screen_width / 2) - 250, (self.settings.screen_height / 2) - 150)
#         redghost = ((self.settings.screen_width / 2) - 220, (self.settings.screen_height / 2) - 100)

#         # Pink Ghost position
#         textpos4 = ((self.settings.screen_width / 2) - 120, (self.settings.screen_height / 2) - 150)
#         orangeghost = ((self.settings.screen_width / 2) + 5, (self.settings.screen_height / 2) - 100)

#         # Orange ghost position
#         textpos5 = ((self.settings.screen_width / 2) + 105, (self.settings.screen_height / 2) - 150)
#         cyanghost = ((self.settings.screen_width / 2) + 110, (self.settings.screen_height / 2) - 100)

#         # Cyan ghost position
#         textpos6 = ((self.settings.screen_width / 2) - 10, (self.settings.screen_height / 2) - 150)
#         pinkghost = ((self.settings.screen_width / 2) - 100, (self.settings.screen_height / 2) - 100)

#         # PACMAN position
#         pacman_pos = ((self.settings.screen_width / 2) - 150, (self.settings.screen_height / 8) - 55)

#         # pacman chasing blue ghosts
#         blueghost1 = ((self.settings.screen_width / 2) - 100, (self.settings.screen_height / 2) - 20)
#         blueghost2 = ((self.settings.screen_width / 2) - 80, (self.settings.screen_height / 2) - 20)
#         blueghost3 = ((self.settings.screen_width / 2) - 60, (self.settings.screen_height / 2) - 20)
#         blueghost4 = ((self.settings.screen_width / 2) - 40, (self.settings.screen_height / 2) - 20)

#         # Draw onto screen
#         backgroundpage.blit(text1, textpos1)
#         backgroundpage.blit(self.pacmanimage, pacman_pos)
#         backgroundpage.blit(text2, textpos2)
#         backgroundpage.blit(self.ghost1, redghost)
#         backgroundpage.blit(text3, textpos3)
#         backgroundpage.blit(self.ghost2, pinkghost)
#         backgroundpage.blit(text4, textpos4)
#         backgroundpage.blit(self.ghost3, orangeghost)
#         backgroundpage.blit(text5, textpos5)
#         backgroundpage.blit(self.ghost4, cyanghost)
#         backgroundpage.blit(text6, textpos6)
#         backgroundpage.blit(self.ghost5, blueghost1)
#         backgroundpage.blit(self.ghost5, blueghost2)
#         backgroundpage.blit(self.ghost5, blueghost3)
#         backgroundpage.blit(self.ghost5, blueghost4)

#         # Blit everything to screen
#         screen.blit(self.ghost1, (self.settings.screen_width / 2, self.settings.screen_height / 3))
#         screen.blit(backgroundpage, (200, 200))

#         pygame.display.flip()

#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit()
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     return

#             screen.blit(backgroundpage, (0, 0))
#             pygame.display.flip()



import pygame as pg

class StartUp:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.title_images = []
        self.set_1 = []
        self.animation_1 = []
        self.animation_1_offset = 0
        self.animation_2 = []
        self.animation_2_offset = 0
        self.default_color = (255, 255, 255)
        self.offset = 3
        self.title()
        self.prep_set_1()
        self.prep_animation_1()
        self.prep_animation_2()
        self.current = 0
        self.time = pg.time.get_ticks()

    def title(self):
        self.title_images.append(self.prep_Text("PA", 120, offsetX=140, offsetY=60))
        self.title_images.append(self.prep_Text("CMAN", 120, offsetX=400, offsetY=60))
        pacman = pg.transform.rotozoom(pg.image.load(f'images/pacman/sprite_1.png'), 0, 5)
        self.title_images.append((pacman, (260, 40)))

    
    def prep_set_1(self):
        self.set_1.append(self.prep_Text("BLINKY", 40, color=(255,0,0), offsetX=150, offsetY=300))
        self.set_1.append(self.prep_Text("PINKY", 40, color=(255, 138, 224), offsetX=300, offsetY=300))
        self.set_1.append(self.prep_Text("INKY", 40,color=(77, 216, 255), offsetX=450, offsetY=300))
        self.set_1.append(self.prep_Text("CLYDE", 40, color=(255, 147, 84), offsetX=600, offsetY=300))
        blinky = pg.transform.rotozoom(pg.image.load(f'images/blinky/sprite_00.png'), 0, 1)
        self.set_1.append((blinky, (180, 350)))
        pinky = pg.transform.rotozoom(pg.image.load(f'images/pinky/sprite_00.png'), 0, 1)
        self.set_1.append((pinky, (330, 350)))
        inky = pg.transform.rotozoom(pg.image.load(f'images/inky/sprite_00.png'), 0, 1)
        self.set_1.append((inky, (480, 350)))
        clyde = pg.transform.rotozoom(pg.image.load(f'images/clyde/sprite_00.png'), 0, 1)
        self.set_1.append((clyde, (630, 350)))
    
   
    def prep_animation_1(self):
        blinky = pg.transform.rotozoom(pg.image.load(f'images/blinky/sprite_00.png'), 0, 1)
        self.animation_1.append((blinky, (50, 350)))
        pinky = pg.transform.rotozoom(pg.image.load(f'images/pinky/sprite_00.png'), 0, 1)
        self.animation_1.append((pinky, (90, 350)))
        inky = pg.transform.rotozoom(pg.image.load(f'images/inky/sprite_00.png'), 0, 1)
        self.animation_1.append((inky, (130, 350)))
        clyde = pg.transform.rotozoom(pg.image.load(f'images/clyde/sprite_00.png'), 0, 1)
        self.animation_1.append((clyde, (170, 350)))
        pacman = pg.transform.rotozoom(pg.image.load(f'images/pacman/sprite_1.png'), 0, 1.5)
        self.animation_1.append((pacman, (250, 350)))
        fruit = pg.transform.rotozoom(pg.image.load(f'images/maze/fruit.png'), 0, 1)
        self.animation_1.append((fruit, (300, 350)))

    def prep_animation_2(self):
        ghost = pg.transform.rotozoom(pg.image.load(f'images/panic_ghost/sprite_0.png'), 0, 1)
        self.animation_2.append((ghost, (500, 350)))
        ghost = pg.transform.rotozoom(pg.image.load(f'images/panic_ghost/sprite_0.png'), 0, 1)
        self.animation_2.append((ghost, (540, 350)))
        ghost = pg.transform.rotozoom(pg.image.load(f'images/panic_ghost/sprite_0.png'), 0, 1)
        self.animation_2.append((ghost, (580, 350)))
        ghost = pg.transform.rotozoom(pg.image.load(f'images/panic_ghost/sprite_0.png'), 0, 1)
        self.animation_2.append((ghost, (620, 350)))
        pacman = pg.transform.rotozoom(pg.image.load(f'images/pacman/sprite_1.png'), 180, 1.5)
        self.animation_2.append((pacman, (700, 350)))

        

    def prep_Text(self, msg, size, color=(255,255,255), offsetX=0, offsetY=0):
        font = pg.font.SysFont(None, size)
        text_image = font.render(msg, True, color, self.settings.bg_color)
        rect = text_image.get_rect()
        if offsetY == 0:
            rect.centery = self.screen_rect.centery
        else:
            rect.top = offsetY
        if offsetX == 0:
            rect.centerx = self.screen_rect.centerx
        else:
            rect.left = offsetX

        return (text_image,rect)
    


    def reset(self):
        self.images = []
        # self.prep_aliens()

    def update(self):
        if self.current == 0:
            if pg.time.get_ticks() - self.time > 2000:
                self.current = 1
        elif self.current == 1:
            if self.animation_1_offset > 600:
                self.current = 2
                self.animation_1_offset = 0
            elif (pg.time.get_ticks() - self.time) % 20 == 0:
                self.animation_1_offset += self.offset
        elif self.current == 2:
            if self.animation_2_offset > 600:
                self.current = 0
                self.animation_2_offset = 0
                self.time = pg.time.get_ticks()
            elif (pg.time.get_ticks() - self.time) % 20 == 0:
                self.animation_2_offset += self.offset
            
        self.draw()

    def draw(self):
        for image in self.title_images:
            self.screen.blit(image[0], image[1])
        
        if self.current == 0:
            for image in self.set_1:
                self.screen.blit(image[0], image[1])
        elif self.current == 1:
             for image in self.animation_1:
                x = image[1][0] + self.animation_1_offset 
                y = image[1][1]
                self.screen.blit(image[0], (x,y))
        elif self.current == 2:
             for image in self.animation_2:
                x = image[1][0] - self.animation_2_offset 
                y = image[1][1]
                self.screen.blit(image[0], (x,y))