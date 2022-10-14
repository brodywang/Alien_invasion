class GameStats:
    """track gaming information"""

    def __init__(self,ai_game):
        """initialize all information"""
        self.settings = ai_game.settings
        self.reset_stats()
        # True we game just started
        self.game_active = False
        # highest score should not be changed at any time
        self.high_score = 0

    def reset_stats(self):
        """initialize the information which may change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
