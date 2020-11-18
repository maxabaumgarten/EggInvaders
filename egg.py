import pygame
from pygame.sprite import Sprite

class Egg(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ei_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ei_game.screen

        #Load the eg image and set its rect attribute.
        self.image = pygame.image.load('images/egg.bmp')
        self.rect = self.image.get_rect()

        #start each new egg near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the egg's exact horizontal postion.
        self.x = float(self.rect.x)