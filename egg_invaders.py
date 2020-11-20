import sys

from time import sleep

import pygame

from settings import Settings

from game_stats import GameStats

from button import Button

from owl import Owl

from bullet import Bullet

from egg import Egg


class EggInvaders:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        #instance of settings
        self.settings = Settings()

        #FULLSCREEN mode if wanted
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        #a screen = a surface, which is the part of a screen where a game
        #element can be displayed.  Every element in the game has its own surface
        #screen size using Settings module
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Egg Invaders")
        self.stats = GameStats(self)

        #make an instance of the owl w/ required argument which is the instance EggInvaders
        #This gives access the Owl access to game resources
        self.owl = Owl(self)
        self.bullets = pygame.sprite.Group()
        self.eggs = pygame.sprite.Group()
        self._create_fleet()

        #Make the play button
        self.play_button = Button(self, "Play")

        #set the background color using Settings module
        self.bg_color = (self.settings.bg_color)
        

    def run_game(self):
        """Start the main loop for the game"""

        while True:
            self._check_events()

            if self.stats.game_active:
                #update ships position on each pass through the loop
                self.owl.update()
                #Update bullet postion
                self._update_bullets()
                #update egg position
                self._update_eggs()

            # Redraw the screen during each pass through the loop.
            self._update_screen()

#helper methods does work inside a class but isn't called through an instance.
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_play_button(self, mouse_pos):
        """Start a new game what the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game settings
            self.settings.initialize_dynamic_settings()
            #reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True

            #get rid of any remaining eggs and bullets
            self.eggs.empty()
            self.bullets.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.owl.center_owl()

            #hide the mouse cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to key press"""
        if event.key == pygame.K_RIGHT:
            #Owl moves right as right key is pressed, setting the method true
            self.owl.moving_right = True
        elif event.key == pygame.K_LEFT:
            #Owl moves left as left key is pressed, setting the method true
            self.owl.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            #Stop moving the owl to the right, since the right key was released
            self.owl.moving_right = False
        elif event.key == pygame.K_LEFT:
            #Stop moving the owl to the left, since the left key was released
            self.owl.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #update bullet positions
        self.bullets.update()

        #get rid of bullets that have dissapeared
        #for loops expect list to remain the same, copy lets us modify bullets inside loop
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_owl_collisions()

    def _check_bullet_owl_collisions(self):
        """Respond to bullet-egg collisions"""
        #remove any bullets that have collided
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.eggs, True, True)
        
        if not self.eggs:
            #Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_eggs(self):
        """
        Check if the fleet is at an edge,
            then update then update the postions of all eggs in the fleet
        """
        self._check_fleet_edges()
        self.eggs.update()
        
        #Look for egg-owl collisions
        if pygame.sprite.spritecollideany(self.owl, self.eggs):
            self._owl_hit()
        
        #Look for eggs hitting the bottom of the screen
        self._check_eggs_bottom()

    def _create_fleet(self):
        """Create the fleet of eggs."""
        #Create an egg and find the number of eggs ina  row
        # Spacing between each egg is equal to one egg width
        egg = Egg(self) # need an egg to calculate width/height
        egg_width, egg_height = egg.rect.size #get the egg's w + h from tuple size attribute and store it in a variable
        available_space_x = self.settings.screen_width - (2 * egg_width) #calc horizontal space
        number_eggs_x = available_space_x // (2 * egg_width) #calcs number of eggs in row
        
        #Determine the number of rows of eggs that fit on the screen.
        owl_height = self.owl.rect.height
        #calc the avail space, find vertical space by subtracting the egg height from the top of the game 
        # and the owl height from the bottom + 2 egg heights from bottom
        available_space_y = (self.settings.screen_height -
                                (3 * egg_height) - owl_height)
        number_rows = available_space_y // (2 * egg_height)

        #create the full fleet of eggs.
        for row_number in range(number_rows): # creates number of rows we want
            for egg_number in range(number_eggs_x): #creates the eggs in one row
                self._create_egg(egg_number, row_number) # creates an egg per number of eggs per row
        
    def _create_egg(self, egg_number, row_number):
        """Create an egg and place it in the row"""
        egg = Egg(self) #create an egg
        egg_width, egg_height = egg.rect.size
        #Each egg is pushed to the right one 'egg size' from the left margin. then x2 to account for width of each egg.
        #multiply it by egg position.  Egg.x attribute sets postion of rect.
        egg.x = egg_width + 2 * egg_width * egg_number
        egg.rect.x = egg.x
        egg.rect.y = egg.rect.height + 2 * egg.rect.height * row_number
        self.eggs.add(egg)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any eggs have reached an edge."""
        for egg in self.eggs.sprites():
            if egg.check_edges():
                self._change_fleet_direction()
                break
        
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for egg in self.eggs.sprites():
            egg.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            
    def _owl_hit(self):
        """Respond to the owl being hit by an egg."""
        if self.stats.owls_left > 0:
            #Decrement owls_left.
            self.stats.owls_left -= 1
            #Get rid of any remaining eggs and bullets
            self.eggs.empty()
            self.bullets.empty()
            #create a new fleet and center the owl.
            self._create_fleet()
            self.owl.center_owl()
            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_eggs_bottom(self):
        """Check if any eggs have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for egg in self.eggs.sprites():
            if egg.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the owl got hit
                self._owl_hit
                break


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        #Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)

        #draws the owl on screen
        self.owl.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.eggs.draw(self.screen)

        #Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        #Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ei = EggInvaders()
    ei.run_game()