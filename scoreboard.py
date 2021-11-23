import pygame.font

class Scoreboard:
    """A class which represent an achieved scores."""
    def __init__(self, fb_game):
        """Initialize a scoreboard."""
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.score = fb_game.stats.score
        self.high_score = fb_game.stats.high_score

        # Font settings for scoring information
        self.text_color = (255,255,255)
        self.font = pygame.font.Font('font/04B_19__.TTF',40)
        self.wfont = pygame.font.SysFont(None, 35)
        self.hfont = pygame.font.Font('font/04B_19__.TTF', 25)

        # Prepare the score image
        self.prep_score()

        #Turn the words into the rendered image.
        self.word_image = self.wfont.render('BEST', True, self.text_color)
        self.word_rect = self.word_image.get_rect()

        # Set a word position
        self.word_rect.y = 160
        self.word_rect.x = 114

    def prep_score(self):
        """Turn the score into the rendered image."""
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Display the score at the top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.midtop = self.screen_rect.midtop

    def prep_high_score(self):
        """Turn the score into the rendered image."""
        score_str = str(self.high_score)
        self.score_image = self.hfont.render(score_str, True, self.text_color)

        # Display the score at the top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.x = 140
        self.score_rect.y = 200 
        self.screen.blit(self.score_image, self.score_rect)
        
    def blitword(self):
        self.screen.blit(self.word_image,self.word_rect)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)

    def update_hscore(self):
        self.high_score = max(self.high_score,self.score)

class Restart_Button:
    def __init__(self,fb_game, msg):
        """"Initialize button attributes."""
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.button_color = (186, 0, 0)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,30)
                       
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.x = 105
        self.msg_image_rect.y = 240

    def draw_button(self):
        # Draw bland button and then draw message.
        #self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


