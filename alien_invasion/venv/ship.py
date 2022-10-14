import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """class managing the ship"""
    def __init__(self, ai_game):
        """initialize the original position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the image and get its outside rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # for every new ship, placing it in the midbottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store the min value of x
        self.x = float(self.rect.x)

        # moving tag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust ship's position based on the moving tag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """draw the ship in certain location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """place the ship in bottom center"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)