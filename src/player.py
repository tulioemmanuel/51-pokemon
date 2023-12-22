import os
import math
from enum import Enum
import pygame
from base.entity import Entity
from base.configuration import Configuration
from base.spritesheet import SpriteStripAnim


class PlayerOverworldState(Enum):
    IDLE_UP = 1
    IDLE_DOWN = 2
    IDLE_LEFT = 3
    IDLE_RIGHT = 4
    WALKING_UP = 5
    WALKING_DOWN = 7
    WALKING_LEFT = 8
    WALKING_RIGHT = 9


class Player(Entity):
    def __init__(self, name="player", x=100, y=0):
        Entity.__init__(self)
        self.name = name
        self.vx = 0
        self.vy = 0
        self.screen = pygame.display.get_surface()
        self.animations = self._setup_animations()
        self.state = PlayerOverworldState.IDLE_DOWN
        self.current_animation = self.animations[self.state]
        self.image = self.current_animation.next()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def _setup_animations(self):
        animations = {}
        player_spritesheet_path = os.path.join(
            Configuration.ASSETS_DIR_PATH,
            Configuration.SPRITES_FOLDER_NAME,
            "brendan.png",
        )
        player_spritesheet_colorkey = pygame.Color(0, 80, 159)

        animations[PlayerOverworldState.IDLE_DOWN] = SpriteStripAnim(
            player_spritesheet_path,
            (6, 7, 18, 21),
            1,
            player_spritesheet_colorkey,
            True,
        )
        animations[PlayerOverworldState.IDLE_UP] = SpriteStripAnim(
            player_spritesheet_path,
            (58, 7, 18, 21),
            1,
            player_spritesheet_colorkey,
            True,
        )
        animations[PlayerOverworldState.IDLE_RIGHT] = SpriteStripAnim(
            player_spritesheet_path,
            (111, 9, 17, 21),
            1,
            player_spritesheet_colorkey,
            True,
        )
        animations[PlayerOverworldState.IDLE_LEFT] = SpriteStripAnim(
            player_spritesheet_path,
            (164, 9, 17, 21),
            1,
            player_spritesheet_colorkey,
            True,
        )

        animations[PlayerOverworldState.WALKING_DOWN] = SpriteStripAnim(
            player_spritesheet_path,
            (6, 7, 18, 21),
            3,
            player_spritesheet_colorkey,
            True,
            5,
        )
        animations[PlayerOverworldState.WALKING_UP] = SpriteStripAnim(
            player_spritesheet_path,
            (58, 7, 18, 21),
            3,
            player_spritesheet_colorkey,
            True,
            5,
        )
        animations[PlayerOverworldState.WALKING_RIGHT] = SpriteStripAnim(
            player_spritesheet_path,
            (111, 9, 17, 21),
            3,
            player_spritesheet_colorkey,
            True,
            5,
        )
        animations[PlayerOverworldState.WALKING_LEFT] = SpriteStripAnim(
            player_spritesheet_path,
            (164, 9, 17, 21),
            3,
            player_spritesheet_colorkey,
            True,
            5,
        )
        return animations

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self.image = self.current_animation.next()
        self._move()

    def _move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def _set_state(self, state):
        self.state = state
        self.current_animation = self.animations[state]

    def move_left(self):
        self._set_state(PlayerOverworldState.WALKING_LEFT)
        self.vx -= self.settings["player_speed"]

    def move_right(self):
        self._set_state(PlayerOverworldState.WALKING_RIGHT)
        self.vx += self.settings["player_speed"]

    def move_up(self):
        self._set_state(PlayerOverworldState.WALKING_UP)
        self.vy -= self.settings["player_speed"]

    def move_down(self):
        self._set_state(PlayerOverworldState.WALKING_DOWN)
        self.vy += self.settings["player_speed"]

    def move_touch(self, pos):
        x, y = pos
        screen_width, screen_height = pygame.display.get_window_size()

        if x > 3 * screen_width / 4:
            self.move_right()
        elif x < screen_width / 4:
            self.move_left()
        elif y < screen_height / 4:
            self.move_up()
        elif y > 3 * screen_height / 4:
            self.move_down()

    def stop(self):
        if self.state == PlayerOverworldState.WALKING_DOWN:
            self._set_state(PlayerOverworldState.IDLE_DOWN)
        elif self.state == PlayerOverworldState.WALKING_UP:
            self._set_state(PlayerOverworldState.IDLE_UP)
        elif self.state == PlayerOverworldState.WALKING_LEFT:
            self._set_state(PlayerOverworldState.IDLE_LEFT)
        elif self.state == PlayerOverworldState.WALKING_RIGHT:
            self._set_state(PlayerOverworldState.IDLE_RIGHT)
        self.vx = 0
        self.vy = 0
