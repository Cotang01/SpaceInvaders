
class GameStats:
    """ Отслеживание статистики игры """
    def __init__(self, my_game):
        self.settings = my_game.settings
        # инициализирует high_score в __init__, потому что он не должен
        # сбрасываться
        self.high_score = 0
        # сброс настроек
        self.reset_stats()

        # Игра изначально неактивна
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
