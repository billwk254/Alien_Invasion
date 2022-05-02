class GameStats():
    """Track statistics for alien invasion"""
    def __init__(self,ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #The high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        #Start the game in an inactive state
        self.game_active = False
        self.score = 0
        self.level = 1

