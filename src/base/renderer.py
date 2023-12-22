import pygame
from base.system import System
from base.configuration import Configuration


class Renderer(System):
    def __init__(self, game):
        self.game = game
        self.setup()

    def setup(self):
        super().setup()
        self.settings = Configuration().settings
        pygame.display.set_caption(self.settings["title"])
        self.screen = pygame.display.set_mode(
            (self.settings["screen_width"], self.settings["screen_height"])
        )

        if not pygame.font.get_init():
            pygame.font.init()

        self.font = pygame.font.SysFont("Comic Sans MS", 24)


    def _clear(self):
        screen = self.screen
        screen.fill(
            (self.settings["bg_r"], self.settings["bg_g"], self.settings["bg_b"])
        )
    
    def set_drawables(self,drawables):
        self.drawables = pygame.sprite.Group(drawables)

    def draw(self):
        self._clear()
        self.drawables.draw(self.screen)
        pygame.display.flip()
        pygame.display.update()
