import pygame
from base.game import Game
from base.configuration import Configuration
from base.tile import Tile
from player import Player


class Pokemon(Game):
    def __init__(self):
        super().__init__()
        self.setup()
        self.mainloop()

    def setup(self):
        super().setup()
        self.settings = Configuration().settings
        self.player = Player()
        self.tiles = []
        self._setup_bg()
        self.renderer.set_drawables([self.tiles, self.player])

    # TODO(tulio): Mudar abordagem de criação do bg
    def _setup_bg(self):
        for y in range(0, self.renderer.screen.get_height(), 16):
            for x in range(0, self.renderer.screen.get_width(), 16):
                self.tiles.append(Tile(x, y))

    def update(self):
        self.player.update()

    def render(self):
        self.renderer.draw()

    def mainloop(self):
        self.input.get_input()
        self.update()
        self.render()
        self.frame_delta = self.clock.tick(self.settings["FPS"])

    def cleanup(self):
        pygame.font.init()
        pygame.quit()
