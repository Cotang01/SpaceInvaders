class Settings:
    """ Класс для настройки игры """
    def __init__(self):
        # настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (100, 100, 200)

        # настройки корабля
        self.ship_speed = 1.0
        self.ship_limit = 3

        # настройки пришельцев
        self.alien_speed = 0.5
        self.fleet_drop_speed = 25
        self.fleet_direction = 1  # 1 - вправо, -1 - влево

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        # настройки пуль
        self.bullet_speed = 1.0
        self.bullet_width = 500
        self.bullet_height = 25
        self.bullet_colour = (60, 200, 200)
        self.bullets_allowed = 3

    def initialize_dynamic_settings(self):
        """ Внедрение изменяемых настроек """
        self.ship_speed = 1
        self.bullet_speed = 1
        self.alien_speed = 0.5
        # подсчёт очков
        self.alien_points = 50
        self.fleet_direction = 1

    def increase_speed(self):
        """ Увеличение скорости """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
