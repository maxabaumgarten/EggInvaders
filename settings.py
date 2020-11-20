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
        self.owl_limit = 3

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 300  #default = 3, use 300+ for testing
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Egg settings
        self.egg_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represtents right; -1 represents left
        self.fleet_direction = 1