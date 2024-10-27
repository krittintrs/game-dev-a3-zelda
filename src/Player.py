from src.EntityBase import EntityBase
from src.Dependencies import *
from src.resources import *
from src.constants import *
import random

class Player(EntityBase):
    def __init__(self, conf):
        super(Player, self).__init__(conf)
        self.is_ghost = False
        self.damage = 1
        self.powerup_timers = {PowerUpType.GHOST: 0, PowerUpType.DAMAGE: 0}
        self.glitter_particles = []  # List to hold glitter particles
        self.init_glitter_effect()

    def update(self, dt, events):
        super().update(dt, events)

        # Update power-up timers
        for power, timer in self.powerup_timers.items():
            if timer > 0:
                self.powerup_timers[power] -= dt
                # Check if power-up expired
                if self.powerup_timers[power] <= 0:
                    if power == PowerUpType.GHOST:
                        self.return_from_ghost()
                    elif power == PowerUpType.DAMAGE:
                        gSounds['powerup_deactive'].play()
                        self.damage = 1
        
        # Update glitter particles if damage boost is active
        if self.damage > 1:
            self.update_glitter_effect(dt)
    
    def return_from_ghost(self):
        self.powerup_timers[PowerUpType.GHOST] = 0
        gSounds['powerup_deactive'].play()
        self.is_ghost = False
        self.SetInvulnerable(1.5)
        self.ChangeState('idle')

    def Collides(self, target):
        y, height = self.y + self.height/2, self.height-self.height/2

        return not (self.x + self.width < target.x or self.x > target.x + target.width or
                    y + height < target.y or y > target.y + target.height)
    
    def render(self, screen):
        super().render()
        
        # Render glitter effect if damage boost is active
        if self.damage > 1:
            self.render_glitter_effect(screen)

    def init_glitter_effect(self):
        # Initialize glitter particles
        for i in range(10):
            if i < 5:
                x = -self.width/2
                y = -self.height/2 + self.height//5*i
            else:
                x = self.width/2
                y = -self.height/2 + self.height//5*(i-5)
            print(x,y)
            self.glitter_particles.append({'x': x, 'y': y})

    def update_glitter_effect(self, dt):
        # Update glitter particles, making them fade and regenerate
        for particle in self.glitter_particles:
            particle['y'] += 1
            if particle['y'] > self.height/2:
                particle['y'] = -self.height/2

    def render_glitter_effect(self, screen):
        player_pos = (int(self.x + self.width / 2), int(self.y + self.height / 2))
        for particle in self.glitter_particles:
            pos = (player_pos[0] + particle['x'], player_pos[1] + particle['y'])
            color = (255, 215, 0)  # Glitter color (gold/yellow) with fading effect
            pygame.draw.circle(screen, color, pos, 3)

    def CreateAnimations(self):
        self.animation_list = gPlayer_animation_list