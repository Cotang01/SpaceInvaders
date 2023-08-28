import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, my_game):
        super().__init__()
        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()
        self.settings = my_game.settings

        self.image = pygame.image.load('images/space_ship_new.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed
        if self.moving_up:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down:
            self.rect.y += self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom > 0:
            self.y += self.settings.ship_speed
        if self.moving_down and self.rect.bottom > self.screen_rect.bottom:
            self.y -= self.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """ Постановка корабля в нижний центр экрана """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
