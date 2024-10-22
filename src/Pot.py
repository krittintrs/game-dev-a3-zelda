from src.constants import *
from src.object_defs import GAME_OBJECT_DEFS
from src.GameObject import GameObject

class Pot(GameObject):
    def __init__(self, conf, x, y):
        super().__init__(conf, x, y)
        self.is_carried = False  # To track whether the pot is being carried
        self.speed = 5  # Speed at which the pot moves when thrown
        self.direction = None  # Direction the pot will be thrown

    def update(self, dt):
        pass
