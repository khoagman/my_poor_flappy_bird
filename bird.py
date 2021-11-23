import pygame

from settings import Settings

class Bird:
    """Initialize the bird and its position."""
    def __init__(self,fb_game):
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = fb_game.settings

        # Load the bird
        self.image = pygame.image.load("assets/yellowbird-midflap.png")
        self.rect = self.image.get_rect()

        # Nearly set the bird at center of the screen
        self.rect.midright = self.screen_rect.center

        # Store a decimal value for the bird's vertical
        self.y = float(self.rect.y)
    
    def blitbird(self):
        """Draw the bird"""
        self.screen.blit(self.image,self.rect)

    def fall(self):
        """The bird always fall down."""
        self.y = self.y + self.settings.fall_speed
        self.settings.fall_speed += self.settings.acceleration
        self.rect.y = self.y

    def fly(self):
        """The bird could fly off."""
        self.y-=self.settings.fly_speed
        if self.settings.fly_speed > 0:
            self.settings.fly_speed -= self.settings.acceleration_up
        self.rect.y = self.y