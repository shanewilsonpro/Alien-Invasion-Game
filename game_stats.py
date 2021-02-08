class GameStats:
    """
    track statistics for alien invasion
    """

    def __init__(self, ai_game):
        """
        initialize statistics
        """

        self.settings = ai_game.settings
        self.reset_stats()

        # start game in inactive state
        self.game_active = False

        # start alien invasion in active state
        self.game_active = True

        # high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """
        initialize stats that can change during the game
        """

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1