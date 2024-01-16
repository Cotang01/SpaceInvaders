import pygame.font


class Button:

    def __init__(self, my_game, msg):
        # инициализация кнопки
        self.screen = my_game.screen
        self.screen_rect = self.screen.get_rect()

        # размеры и свойства кнопки
        self.width = 200
        self.height = 50
        self.button_colour = (0, 200, 100)
        self.text_colour = (255, 255, 255)
        # None - шрифт по умолчанию, 48 - размер
        self.font = pygame.font.SysFont(None, 48)

        # установка кнопки в центр экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # разовое сообщение кнопки
        self._prep_msg(msg)

    def _prep_msg(self, msg: str):
        # отрисовка текста по центру кнопки (экрана)
        self.msg_image = self.font.render(
            msg, True, self.text_colour, self.button_colour)
        # ^ сообщение, сглаживание, цвет текста, цвет фона (кнопки)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # отображение кнопки
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
