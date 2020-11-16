class Settings:
    """A class to store all settings for Egg Invaders"""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        #Owl settings
        self.owl_speed = 1.5