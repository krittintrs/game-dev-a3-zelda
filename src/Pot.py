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

    def Break(self):
        self.is_broken = True
        self.state = 'broken'
        self.solid = False

    def Collides(self, target):
        return not(self.x + self.width < target.x or self.x > target.x + target.width or
                   self.y + self.height < target.y or self.y > target.y + target.height)
