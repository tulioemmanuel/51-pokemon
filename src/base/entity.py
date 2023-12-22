from pygame.sprite import Sprite
from base.configuration import Configuration


class Entity(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.settings = Configuration().settings

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        
    