import pygame
from settings import Settings

class Base:
    """A class to generate the ground and grass."""
    def __init__(self,fb_game):
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        # Load the ground and the grass image and get its rect
        self.image = pygame.image.load("assets/base.png")
        self.rect = self.image.get_rect()

        # Set a default position
        self.rect.bottom = self.screen_rect.bottom
        self.rect.left = self.screen_rect.left

        self.x = float(self.rect.x)

    def blitbase(self):
        self.screen.blit(self.image,self.rect)

    def grass_move(self):
        if self.rect.right <= self.screen_rect.right:
            self.x+=48
        self.x -= self.settings.grass_speed
        self.rect.x = self.x
