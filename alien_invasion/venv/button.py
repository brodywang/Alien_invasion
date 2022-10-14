import pygame.font


class Button:

    def __init__(self,ai_game, msg):
        """initiallize button 's properties"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # set size and other properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # set rect object and mediate
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button tag will only create once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """midiate msg and draw the msg as an image"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw a button with certain color to fill with, then drawing text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)