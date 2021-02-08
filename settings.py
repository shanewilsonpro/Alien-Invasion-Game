class Settings:
    """
    a class to store all settings for Alien Invasion
    """

    def __init__(self):
        """
        initialize game's settings
        """
        # screen settings
        self.screen_width = 1200
        self.screen_height = 840
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # alien settings
        self.fleet_drop_speed = 10

        # how quickly game speeds up
        self.speedup_scale = 1.1

        # how quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        initialize settings that change throughout game
        """

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """
        increase speed settings and alien point value
        """

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)