import pygame

class Owl:
    """A class to manage the Owl"""

    def __init__(self, ei_game):
        """Initialize the owl and set its starting position"""
        #
        self.screen = ei_game.screen
        
        #rect = rectangle - game elements are treated like rectangles
        self.screen_rect = ei_game.screen.get_rect()

        # Load the owl image and get its rect.
        self.image = pygame.image.load('images/owl.bmp')
        self.rect = self.image.get_rect()

        #Start each new owl at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the Owl at its current location."""
        self.screen.blit(self.image, self.rect)