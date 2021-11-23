class Settings:
    """A class to store all game settings."""
    def __init__(self):
        self.screen_width = 288
        self.screen_height = 512

        self.grass_speed = 1.2
        # Bird's settings
        self.fall_speed = 0.002
        self.acceleration = 0.06
        self.acceleration_up = 0.0004
        self.fly_speed = 0.18

        #Pipe's settings
        self.pipe_speed = 1
