class Settings:
    """A class to store all settings for Egg Invaders"""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        
        #Owl settings
        self.owl_speed = 1
        self.owl_limit = 3

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3  #default = 3, use 300+ for testing
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        #Egg settings
        self.egg_speed = .7
        self.fleet_drop_speed = 3 #default was 10

        #How quickly the game speeds up
        self.speedup_scale = 1.1
        #How quickly the egg point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.owl_speed = 1.5
        self.bullet_speed = 3.0
        self.egg_speed = 1.0
        self.egg_points = 50

        # fleet direction of 1 represtents right; -1 represents left
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings and egg point values."""
        self.owl_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.egg_speed *= self.speedup_scale

        self.egg_points = int(self.egg_points * self.score_scale) #somethings up with this