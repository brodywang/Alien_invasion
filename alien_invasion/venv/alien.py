import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """represent a single alien"""

    def __init__(self,ai_game):
        """initialize alien location and set it original position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien picture and set its rect properties
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien located at the topleft of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien's precise location
        self.x = float(self.rect.x)

    def check_edge(self):
        """if alien hit edge of screen, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """moving the alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

