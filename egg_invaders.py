#Python module used to exit the game
import sys

#Python module used to create and make the game functional
import pygame

#import settings module which allows for simpler settings modifications
from settings import Settings

#import owl module
from owl import Owl


class EggInvaders:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        #instance of settings
        self.settings = Settings()

        #a screen = a surface, which is the part of a screen where a game
        #element can be displayed.  Every element in the game has its own surface
        #screen size using Settings module
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Egg Invaders")

        #make an instance of the owl w/ required argument which is the instance EggInvaders
        #This gives access the Owl access to game resources
        self.owl = Owl(self)

        #set the background color using Settings module
        self.bg_color = (self.settings.bg_color)
        

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()
            # Redraw the screen during each pass through the loop.
            self._update_screen()
            #update ships position on each pass through the loop/
            self.owl.update()

#helper methods does work inside a class but isn't called through an instance.
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Owl moves right as right key is pressed, setting the method true
                    self.owl.moving_right = True
                elif event.key == pygame.K_LEFT:
                    #Owl moves left as left key is pressed, setting the method true
                    self.owl.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    #Stop moving the owl to the right, since the right key was released
                    self.owl.moving_right = False
                elif event.key == pygame.K_LEFT:
                    #Stop moving the owl to the left, since the left key was released
                    self.owl.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)

        #draws the owl on screen
        self.owl.blitme()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ei = EggInvaders()
    ei.run_game()