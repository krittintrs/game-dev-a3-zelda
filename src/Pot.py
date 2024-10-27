from src.constants import *
from src.object_defs import GAME_OBJECT_DEFS
from src.GameObject import GameObject

class Pot(GameObject):
    def __init__(self, conf, x, y):
        super().__init__(conf, x, y)
        self.is_carried = False
        self.is_touching = False
        self.is_broken = False
        self.is_thrown = False  

        self.speed = POT_THROWN_SPEED  # Adjust as needed
        self.direction = None
        self.throw_timer = 0  # Timer for tracking throw duration

    def update(self, dt):
        if self.is_thrown:
            # Increase throw timer
            self.throw_timer += dt

            # Move the pot based on direction and speed
            if self.direction == 'up':
                self.y -= self.speed * dt
            elif self.direction == 'down':
                self.y += self.speed * dt
            elif self.direction == 'left':
                self.x -= self.speed * dt
            elif self.direction == 'right':
                self.x += self.speed * dt

            # Check for wall collision or time expiration
            if self.CollidesWithWall() or self.throw_timer >= POT_TIMER:
                self.Explode()

    def Throw(self, direction):
        self.is_carried = False
        self.is_touching = False
        self.is_thrown = True
        self.direction = direction
        self.throw_timer = 0  # Reset the timer each time it’s thrown

    def Explode(self):
        self.Break()  # Transition pot to broken state
        self.is_thrown = False
        print("Pot exploded!")

    def CollidesWithWall(self):
        # This function would check the pot's position relative to the room’s boundaries.
        return self.x <= MAP_RENDER_OFFSET_X + TILE_SIZE or \
            self.x + self.width >= WIDTH - TILE_SIZE * 2 or \
            self.y <= MAP_RENDER_OFFSET_Y + TILE_SIZE - self.height/2 or \
            self.y + self.height >= HEIGHT - (HEIGHT - MAP_HEIGHT * TILE_SIZE) + MAP_RENDER_OFFSET_Y - TILE_SIZE

    def Break(self):
        self.is_touching = False
        self.is_broken = True
        self.state = 'broken'
        self.solid = False

    def Lift(self):
        self.is_carried = True
        self.is_touching = False
        self.state = 'bomb'
        self.solid = False

    def Collides(self, target):
        return not(self.x + self.width < target.x or self.x > target.x + target.width or
                   self.y + self.height < target.y or self.y > target.y + target.height)
