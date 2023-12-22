import logging
from abc import ABC,abstractmethod

class System(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def setup(self):
        logging.info('Initializing {0} system'.format(self))
