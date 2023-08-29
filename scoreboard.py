import pygame.font
from pygame.sprite import Group
from ship_player import Ship


class Scoreboard:
    """ Класс для вывода статистики """

    def __init__(self, my_game):
        """ Инициализация таблицы со статистикой """
        self.my_game = my_game
        self.screen = my_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = my_game.settings
        self.stats = my_game.stats

        # Шрифт надписей
        self.text_colour = (255, 255, 30)
        self.font = pygame.font.SysFont('calibri', 48)
        # подготовка исходного изображения
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """ Преобразование текущего счёта в графическое изображение """
        rounded_score = round(self.stats.score, -1)
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_colour, self.settings.bg_colour
        )
        # Вывод счёта в правом верхнем углу экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_colour, self.settings.bg_colour
        )
        # выравнивание по центру верхней стороны
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """ Вывод текущего уровня на экран """
        level_str = "Current stage: " + str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_colour, self.settings.bg_colour
        )

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        """ Вывод количества оставшихся жизней в графическом виде """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.my_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """ Вывод счёта и жизней на экран """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
