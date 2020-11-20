import pygame

class Owl:
    """A class to manage the Owl"""

    def __init__(self, ei_game):
        """Initialize the owl and set its starting position"""
        #
        self.screen = ei_game.screen
        self.settings = ei_game.settings

        #rect = rectangle - game elements are treated like rectangles
        self.screen_rect = ei_game.screen.get_rect()

        # Load the owl image and get its rect.
        self.image = pygame.image.load('images/owl.bmp')
        self.rect = self.image.get_rect()

        #Start each new owl at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship"s horizontal position.
        #this is done in order to hold floats, because rect only does integer
        self.x = float(self.rect.x)

        #Movement flag - Default owl behavior is motionless
        self.moving_right = False
        self.moving_left = False

#update manages the ships position
    def update(self):
        """Update the owl's position based on the movement flag."""
        #updates the owl's x value, not the rect
        #prevents owl from going off the edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.owl_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.owl_speed
        
        #update rect object from self.x
        self.rect.x = self.x

    #blitme draws the owl to the screen
    def blitme(self):
        """Draw the Owl at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_owl(self):
        """Center the owl on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x - float(self.rect.x)