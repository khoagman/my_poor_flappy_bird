class GameStats:
    """A class contains game's statistics."""
    def __init__(self, fb_game):
        """Initialize statistics."""
        self.settings = fb_game.settings
        self.score = 0
        self.high_score = 0
        self.game_start = False
        self.game_over = False