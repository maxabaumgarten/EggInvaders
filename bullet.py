import pygame
#Sprites let you group related elements in your game and act on all group elements at once

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    #__init__ used to inherit the current instance of Egg Invaders
    def __init__(self, ei_game):
        """Create a bullet object at the ship's current position"""
        #super used to inherit properly from Sprite
        super().__init__()
        #Settings for the bullet
        self.screen =  ei_game.screen
        self.settings = ei_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0,0) and then set the correct position"
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                    self.settings.bullet_height)
        self.rect.midtop = ei_game.owl.rect.midtop

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen"""
        #Update the decimal postion of the bullet.
        self.y -= self.settings.bullet_speed
        #update the rect posion.
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)