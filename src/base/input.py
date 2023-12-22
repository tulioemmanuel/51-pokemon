import pygame
from base.system import System


class Input(System):
    def __init__(self, game):
        self.game = game
        self.setup()

    def setup(self):
        super().setup()

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.quit()
                elif event.key == pygame.K_a:
                    self.game.player.move_left()
                elif event.key == pygame.K_d:
                    self.game.player.move_right()
            elif event.type == pygame.KEYUP:     
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.game.player.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.game.player.move_touch(pygame.mouse.get_pos())
            elif event.type == pygame.MOUSEBUTTONUP:
                self.game.player.stop()                    
