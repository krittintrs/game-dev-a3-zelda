from src.constants import *
from src.object_defs import GAME_OBJECT_DEFS
from src.GameObject import GameObject

class Pot(GameObject):
    def __init__(self, conf, x, y):
        super().__init__(conf, x, y)
        self.is_carried = False 
        self.is_broken = False
        self.speed = 5  
        self.direction = None  

    def update(self, dt):
        pass
