import math

from src.states.BaseState import BaseState
from src.HitBox import Hitbox
import pygame
from src.resources import *

class PlayerPotLiftState(BaseState):
    def __init__(self, player, dungeon=None):
        self.player = player
        self.dungeon = dungeon

        
    def Enter(self, params):
        #sounds
        self.player.offset_x = 0
        self.player.offset_y = 15

        self.player.curr_animation.Refresh()
        self.player.ChangeAnimation("pot_lift_"+self.player.direction)

    def Exit(self):
        pass

    def update(self, dt, events):
        # TODO: Implement pot handling
        
        if self.player.curr_animation.times_played > 0:
            self.player.curr_animation.times_played = 0
            self.player.ChangeState("pot_walk")  
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.ChangeState('idle')


    def render(self, screen):
        animation = self.player.curr_animation.image
        screen.blit(animation, (math.floor(self.player.x - self.player.offset_x), math.floor(self.player.y - self.player.offset_y)))

        #hit box debug
        #pygame.draw.rect(screen, (255, 0, 255), pygame.Rect(self.sword_hitbox.x, self.sword_hitbox.y, self.sword_hitbox.width, self.sword_hitbox.height))