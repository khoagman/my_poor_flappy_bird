import pygame
from pygame.sprite import Sprite

class Top_Pipe(Sprite):
    def __init__(self,fb_game):
        """Initialize two pipes and randomize its position."""
        super().__init__()
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fb_game.settings

        # Load images and get its rect
        self.image = pygame.image.load('assets/pipe-green-usd.png')
        self.rect = self.image.get_rect()

        self.rect.x = 290
        self.rect.y = 0

        self.x = float(self.rect.x)
    
    def move(self):
        self.x -= self.settings.pipe_speed
        self.rect.x = self.x

    def _check_edge(self):
        if self.rect.x <= -52:
            return True
        return False

