import sys
import time
import pygame
import random

from settings import Settings
from base import Base
from bird import Bird
from t_pipe import Top_Pipe
from b_pipe import Bottom_Pipe

class FlappyBird:
    """A main class to manage game's assets and behaviors."""
    def __init__(self):
        """Initialize the game and create the game resources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                            self.settings.screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Flappy Bird")

        self.bird = Bird(self)

        self.t_pipes = pygame.sprite.Group()
        self.b_pipes = pygame.sprite.Group()
        
        # Background image
        self.bg = pygame.image.load("assets/background-night.png")
        self.base = Base(self)

    def game_run(self):
        """Start the game loop."""
        while True:
            self._check_event()
            self._check_pipe()
            self._update_pipe()
            self.base.grass_move()
            self._bird_update()
            self._update_screen()

    def _check_pipe(self):
        """Create pipes in a particular situation."""
        # Create pipes if there are no pipe in the group
        if not self.t_pipes:
            self._create_pipes()
        for t_pipe in self.t_pipes.sprites():
            if t_pipe.rect.x == 140:
                self._create_pipes()
        # Remove pipes if one pair of pipes reach the edge
        for t_pipe in self.t_pipes.copy():
            if t_pipe._check_edge():
                self.t_pipes.remove(t_pipe)
        for b_pipe in self.b_pipes.copy():
            if t_pipe._check_edge():
                self.b_pipes.remove(b_pipe)

    def _update_pipe(self):
        for t_pipe in self.t_pipes.sprites():
            t_pipe.move()
        for b_pipe in self.b_pipes.sprites():
            b_pipe.move()

    def _create_pipes(self):
        t_pipe_high = random.randrange(120, 256, 5)
        b_pipe_high = t_pipe_high + 80
        t_pipe = Top_Pipe(self)
        b_pipe = Bottom_Pipe(self)
        t_pipe.rect.y = t_pipe_high - 320
        b_pipe.rect.y = b_pipe_high
        self.t_pipes.add(t_pipe)
        self.b_pipes.add(b_pipe)

    def _bird_update(self):
        self.bird.fall()

    def _check_event(self):
        """Check a mouse event."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._bird_fly()

    def _bird_fly(self):
        """Limit a flying speed of the bird."""
        for i in range(1200):
            self.bird.fly()
        # Remove an acceleration
        self.settings.fall_speed = 0.002
        self.settings.fly_speed = 0.18

    def _update_screen(self):
        # Draw a background
        self.screen.blit(self.bg,(0,0))

        # Draw pipes
        self.t_pipes.draw(self.screen)
        self.b_pipes.draw(self.screen)

        # Draw the surface
        self.base.blitbase()

        # Draw the bird at each loop
        self.bird.blitbird()

        # Make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(90)
        
if __name__ == '__main__':
    # Make a game instance and run
    fb = FlappyBird()
    fb.game_run()