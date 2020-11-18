import pygame
from pygame.sprite import Sprite

class Egg(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ei_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ei_game.screen
        self.settings = ei_game.settings

        #Load the eg image and set its rect attribute.
        self.image = pygame.image.load('images/egg.bmp')
        self.rect = self.image.get_rect()

        #start each new egg near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the egg's exact horizontal postion.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if egg is at the edge of screen."""
        screen_rect =  self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the egg to the right or left."""
        self.x += (self.settings.egg_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x