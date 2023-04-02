import pygame
import pygame.font

from pygame.sprite import Group
from settings import Settings

# Globals for ease
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class StartUp():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        # Load in ghost images
        self.ghost1 = pygame.image.load('images/blinky/sprite_00.png')
        self.ghost2 = pygame.image.load('images/pinky/sprite_00.png')
        self.ghost3 = pygame.image.load('images/clyde/sprite_00.png')
        self.ghost4 = pygame.image.load('images/inky/sprite_00.png')
        self.ghost5 = pygame.image.load('images/panic_ghost/sprite_0.png')

        # Load in Pacman image
        self.height = 125
        self.width = 125
        img = pygame.image.load('images/pacman/sprite_1.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.rect.x, self.rect.y = 310, 515
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.pacmanimage = img
        self.rect = self.pacmanimage.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        screen.fill(BLACK)

    def createScreen(self, screen):
        pygame.init()
        pygame.display.set_caption("PACMAN")

        backgroundpage = pygame.Surface(screen.get_size())
        backgroundpage = backgroundpage.convert()
        backgroundpage.fill(BLACK)

        # Display P in front of the PACMAN pic
        font = pygame.font.Font(None, 144)
        text1 = font.render("PA", 2, WHITE)
        textpos1 = text1.get_rect()
        textpos1 = ((self.settings.screen_width / 2) - 300, (self.settings.screen_height / 8) - 75)
        font = pygame.font.Font(None, 144)

        # Display "CMAN" after the PACMAN pic
        text2 = font.render("MAN", 2, WHITE)
        textpos2 = text2.get_rect()
        textpos2 = ((self.settings.screen_width / 2), (self.settings.screen_height / 8) - 75)

        # Ghosts position and text
        font = pygame.font.Font(None, 44)
        
        # Red Ghost
        text3 = font.render(" BLINKY", 2, (250, 250, 250))
        textpos3 = text3.get_rect()

        # Pink Ghost        
        text4 = font.render(" PINKY", 2, (250, 250, 250))
        textpos4 = text4.get_rect()

        # Orange Ghost
        text5 = font.render(" INKY", 2, (250, 250, 250))
        textpos5 = text5.get_rect()

        # Cyan Ghost
        text6 = font.render(" CLYDE", 2, (250, 250, 250))
        textpos6 = text6.get_rect()
        
        # Red Ghost position
        textpos3 = ((self.settings.screen_width / 2) - 250, (self.settings.screen_height / 2) - 150)
        redghost = ((self.settings.screen_width / 2) - 220, (self.settings.screen_height / 2) - 100)

        # Pink Ghost position
        textpos4 = ((self.settings.screen_width / 2) - 120, (self.settings.screen_height / 2) - 150)
        orangeghost = ((self.settings.screen_width / 2) + 5, (self.settings.screen_height / 2) - 100)

        # Orange ghost position
        textpos5 = ((self.settings.screen_width / 2) + 105, (self.settings.screen_height / 2) - 150)
        cyanghost = ((self.settings.screen_width / 2) + 110, (self.settings.screen_height / 2) - 100)

        # Cyan ghost position
        textpos6 = ((self.settings.screen_width / 2) - 10, (self.settings.screen_height / 2) - 150)
        pinkghost = ((self.settings.screen_width / 2) - 100, (self.settings.screen_height / 2) - 100)

        # PACMAN position
        pacman_pos = ((self.settings.screen_width / 2) - 150, (self.settings.screen_height / 8) - 55)

        # pacman chasing blue ghosts
        blueghost1 = ((self.settings.screen_width / 2) - 100, (self.settings.screen_height / 2) - 20)
        blueghost2 = ((self.settings.screen_width / 2) - 80, (self.settings.screen_height / 2) - 20)
        blueghost3 = ((self.settings.screen_width / 2) - 60, (self.settings.screen_height / 2) - 20)
        blueghost4 = ((self.settings.screen_width / 2) - 40, (self.settings.screen_height / 2) - 20)

        # Draw onto screen
        backgroundpage.blit(text1, textpos1)
        backgroundpage.blit(self.pacmanimage, pacman_pos)
        backgroundpage.blit(text2, textpos2)
        backgroundpage.blit(self.ghost1, redghost)
        backgroundpage.blit(text3, textpos3)
        backgroundpage.blit(self.ghost2, pinkghost)
        backgroundpage.blit(text4, textpos4)
        backgroundpage.blit(self.ghost3, orangeghost)
        backgroundpage.blit(text5, textpos5)
        backgroundpage.blit(self.ghost4, cyanghost)
        backgroundpage.blit(text6, textpos6)
        backgroundpage.blit(self.ghost5, blueghost1)
        backgroundpage.blit(self.ghost5, blueghost2)
        backgroundpage.blit(self.ghost5, blueghost3)
        backgroundpage.blit(self.ghost5, blueghost4)

        # Blit everything to screen
        screen.blit(self.ghost1, (self.settings.screen_width / 2, self.settings.screen_height / 3))
        screen.blit(backgroundpage, (200, 200))

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return

            screen.blit(backgroundpage, (0, 0))
            pygame.display.flip()