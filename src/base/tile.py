import os
import pygame
from pygame.sprite import AbstractGroup
from base.spritesheet import Spritesheet
from base.configuration import Configuration


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        spritesheet = Spritesheet(
            os.path.join(
                Configuration.ASSETS_DIR_PATH,
                Configuration.BACKGROUND_FOLDER_NAME,
                "route101.png",
            )
        )
        self.image = spritesheet.image_at((160, 160, 16, 16))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
