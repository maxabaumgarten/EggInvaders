import pygame.font

from pygame.sprite import Group

from owl import Owl


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ei_game):
        """Initialize scorekeeping attributes"""
        self.ei_game = ei_game
        self.screen = ei_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ei_game.settings
        self.stats = ei_game.stats

        #Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_owls()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1) #NOT WORKING
        score_str = "{:,}".format(rounded_score) #NOT WORKING
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
        
        #Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.owls.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        
        #Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def check_high_score(self):
        """Check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)
        
        #Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right =  self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_owls(self):
        """Show how many owls are left."""
        self.owls = Group()
        for owl_number in range (self.stats.owls_left):
            owl = Owl(self.ei_game)
            owl.rect.x = 10 + owl_number + owl.rect.width
            owl.rect.y = 10
            self.owls.add(owl)
