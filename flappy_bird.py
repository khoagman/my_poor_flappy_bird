import sys
import time
import pygame
import random

from settings import Settings
from base import Base
from bird import Bird
from t_pipe import Top_Pipe
from b_pipe import Bottom_Pipe
from game_stats import GameStats
from scoreboard import Scoreboard, Restart_Button

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

        # An instance of a game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.button = Restart_Button(self,'RESTART')

    def game_run(self):
        """Start the game loop."""
        while True:
            self._check_event()
            if self.stats.game_start:
                if not self.stats.game_over:
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
                self.sb.score += 1
                #self.sb.prep_score()
                self._create_pipes()
        # Remove pipes if one pair of pipes reach the edge
        for t_pipe in self.t_pipes.copy():
            if t_pipe._check_edge():
                self.t_pipes.remove(t_pipe)
        for b_pipe in self.b_pipes.copy():
            if t_pipe._check_edge():
                self.b_pipes.remove(b_pipe)

    def _check_hit_the_ground(self):
        if self.bird.rect.y >= 375:
            return True
        return False

    def _update_pipe(self):
        if pygame.sprite.spritecollideany(self.bird, self.t_pipes) or pygame.sprite.spritecollideany(self.bird, self.b_pipes) or self._check_hit_the_ground():
            self.stats.game_over = True
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
                if self.stats.game_over:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_restart_button(mouse_pos)
                elif not self.stats.game_over:
                    self._bird_fly()
                self.stats.game_start = True
    
    def _check_restart_button(self,pos):
        """Restart the game if player click on a restart button."""
        button_clicked = self.button.msg_image_rect.collidepoint(pos)
        if button_clicked:
            self.t_pipes.empty()
            self.b_pipes.empty()
            self.bird.replace()
            self.settings.reset_bird()
            self.stats.game_over = False
            self.sb.score = 0
            self.sb.prep_score()

    def _bird_fly(self):
        """Limit a flying speed of the bird."""
        for i in range(1200):
            self.bird.fly()
        # Remove an acceleration
        self.settings.reset_bird()

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

        # Overgame hud
        if self.stats.game_over:
            self.sb.update_hscore()
            self.button.draw_button()
            self.sb.blitword()
            self.sb.prep_high_score()

        # Draw the scoreboard
        self.sb.prep_score()
        self.sb.show_score()

        # Make the most recently drawn screen visible
        pygame.display.flip()
        self.clock.tick(90)
        
if __name__ == '__main__':
    # Make a game instance and run
    fb = FlappyBird()
    fb.game_run()