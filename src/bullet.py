import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ Класс снарядов корабля """

    def __init__(self, my_game):
        """ Создание снаряда на позиции корабля """
        super().__init__()
        self.screen = my_game.screen
        self.settings = my_game.settings
        self.colour = self.settings.bullet_colour

        self.rect = pygame.Rect(0, 0,
                                self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = my_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        # обновление позиции пули на экране с каждым кадром
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # отрисовка пули
        pygame.draw.rect(self.screen, self.colour, self.rect)
