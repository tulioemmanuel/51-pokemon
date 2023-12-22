import logging
import os
import pygame
import sys
from base.renderer import Renderer
from base.input import Input
from base.configuration import Configuration

logging.basicConfig(level=os.environ.get("LOGLEVEL",Configuration().settings['log_level']))
class Game(object):
    def __init__(self):
        logging.info('Initializing {game}'.format(game=self.__class__.__name__))
        self.renderer = Renderer(self)
        self.input = Input(self)
        self.configuration = Configuration()
        self.clock = pygame.time.Clock()
        self.setup()

    def setup(self):
        pygame.init()
        pygame.font.init()
        self.running = True

    def update(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    async def mainloop(self):
        raise NotImplementedError

    def quit(self):
        logging.info('Quitting {game}'.format(game=self.__class__.__name__))
        self.running = False
