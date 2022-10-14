import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """manage the bullet"""

    def __init__(self, ai_game):
        """create a bullet where the ship at"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # create a small bullet(rectangular) at (0, 0) then set the correct location
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the location of the bullet
        self.y = float(self.rect.y)

    def update(self):
        """moving the bullet up"""
        self.y -= self.settings.bullet_speed
        # update the new bullet location
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)