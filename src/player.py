import pygame
from base.entity import Entity


class Player(Entity):
    def __init__(self, name="player", x=100, y=0):
        Entity.__init__(self)
        self.name = name
        surface = pygame.Surface(
            (self.settings["player_width"], self.settings["player_height"])
        )
        surface.fill(
            (
                255,
                255,
                255,
            )
        )
        self.image = surface
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        self.screen = pygame.display.get_surface()

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)

    def move_left(self):
        self.vx -= self.settings["player_speed"]

    def move_right(self):
        self.vx += self.settings["player_speed"]

    def move_up(self):
        self.vy -= self.settings["player_speed"]

    def move_down(self):
        self.vy += self.settings["player_speed"]

    def move_touch(self, pos):
        pass

    def stop(self):
        self.vx = 0
        self.vy = 0
