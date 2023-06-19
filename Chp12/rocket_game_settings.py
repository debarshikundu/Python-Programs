class Rocket_Game_Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (255, 255, 255)

        # Rocket settings.
        self.rocket_speed = 1.5