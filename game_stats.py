class GameStats:
    """Track statistics for Egg Invaders"""

    
    def __init__(self, ei_game):
        """Initialize statistics."""
        self.settings = ei_game.settings
        self.reset_stats()
        #start Egg Invasion in an active state.
        self.game_active = True
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.owls_left = self.settings.owl_limit