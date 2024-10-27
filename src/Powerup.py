import pygame
from src.constants import *
from src.resources import *
import random

class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = POWER_UP_SIZE  # Width of the power-up
        self.height = POWER_UP_SIZE  # Height of the power-up
        self.type = random.choice([PowerUpType.GHOST, PowerUpType.DAMAGE, PowerUpType.HEAL])
        self.image = powerups_image_list[self.type.value]
        self.active = True  # Indicates if the power-up is active

    def render(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))

    def update(self, dt):
        # Update logic for the power-up can be added here
        pass

    def collect(self, player):
        if self.type == PowerUpType.GHOST:
            gSounds['powerup_ghost'].play()
            player.ChangeState('ghost_idle')
            player.powerup_timers[self.type] = POWER_UP_TIMER
        elif self.type == PowerUpType.DAMAGE:
            gSounds['powerup_damage'].play()
            player.damage = 2
            player.powerup_timers[self.type] = POWER_UP_TIMER
        elif self.type == PowerUpType.HEAL:
            gSounds['powerup_heal'].play()
            player.health = min(player.health + 1, PLAYER_MAX_HEALTH)
