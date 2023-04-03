class Settings():
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 680
        self.bg_color = (40, 40, 40)
        self.black = (0, 0, 0)
        self.pacmanspeed = 2
        self.rectsize = 15
        self.pacmansize = self.rectsize * 5
        self.food_points = 10
        self.game_active = False
        self.hs_active = False

# # TODO: set a ship_limit of 3
        self.ship_limit = 3         # total ships allowed in game before game over

        # self.fleet_drop_speed = 1
        # self.fleet_direction = 1     # change to a Vector(1, 0) move to the right, and ...
        # self.initialize_speed_settings()

    # def initialize_speed_settings(self):
    #     self.alien_speed = 1
    #     self.ship_speed = 3
    #     self.laser_speed = 3

    def increase_speed(self):
        scale = self.speedup_scale
        self.ship_speed *= scale
        self.laser_speed *= scale