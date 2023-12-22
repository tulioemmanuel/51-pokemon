import pygame
from base.game import Game
from base.configuration import Configuration
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
        self.renderer.set_drawables([self.player])

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
