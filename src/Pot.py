from src.constants import *
from src.object_defs import GAME_OBJECT_DEFS
from src.GameObject import GameObject
import pygame

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

        self.explosion_radius = POT_EXPLODE_RADIUS  # Radius of explosion in pixels
        self.is_exploding = False
        self.alpha = 255  # Full opacity

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
            if self.CollidesWithWall() or self.throw_timer >= POT_THROWN_TIMER:
                print('initial explosion')
                self.Explode()

    def Throw(self, direction):
        self.is_carried = False
        self.is_touching = False
        self.is_thrown = True
        self.direction = direction
        self.throw_timer = 0  # Reset the timer each time it’s thrown

    def CollidesWithWall(self):
        # This function would check the pot's position relative to the room’s boundaries.
        return self.x <= MAP_RENDER_OFFSET_X + TILE_SIZE or \
            self.x + self.width >= WIDTH - TILE_SIZE * 2 or \
            self.y <= MAP_RENDER_OFFSET_Y + TILE_SIZE - self.height/2 or \
            self.y + self.height >= HEIGHT - (HEIGHT - MAP_HEIGHT * TILE_SIZE) + MAP_RENDER_OFFSET_Y - TILE_SIZE

    def Explode(self):
        self.Break()  # Transition pot to broken state
        self.is_thrown = False
        self.is_exploding = True
        self.explosion_time = POT_EXPLODE_TIMER  # Explosion effect duration in seconds

    def draw_explosion(self, screen):
        # explosion_center = (int(self.x + self.width / 2), int(self.y + self.height / 2))
        # pygame.draw.circle(screen, (255, 0, 0), explosion_center, self.explosion_radius)
        explosion_center = (int(self.x + self.width / 2), int(self.y + self.height / 2))
        explosion_color = (255, 0, 0, self.alpha)  # Include alpha for transparency

        # Create a surface for the explosion with the same size as the explosion radius
        explosion_surface = pygame.Surface((self.explosion_radius * 2, self.explosion_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(explosion_surface, explosion_color, (self.explosion_radius, self.explosion_radius), self.explosion_radius)

        # Blit the explosion surface to the screen at the correct position
        screen.blit(explosion_surface, (explosion_center[0] - self.explosion_radius, explosion_center[1] - self.explosion_radius))

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
