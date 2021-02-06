class Settings:
    """
    a class to store all settings for Alien Invasion
    """

    def __init__(self):
        """
        initialize game's settings
        """
        # screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5