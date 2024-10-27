from src.states.entity.EntityIdleState import EntityIdleState
from src.resources import *
import pygame

class PlayerGhostIdleState(EntityIdleState):
    def __init__(self, player, dungeon):
        super(PlayerGhostIdleState, self).__init__(player)
        self.player = player
        self.dungeon = dungeon

    def Enter(self, params):
        self.entity.offset_y = 2
        self.entity.offset_x = 8
        super().Enter(params)
        self.entity.ChangeAnimation('ghost_' + self.entity.direction)
        self.player.is_ghost = True

    def Exit(self):
        pass

    def update(self, dt, events):
        for entity in self.dungeon.current_room.entities:
            if entity.Collides(self.player) and not entity.invulnerable:
                entity.Damage(1)
                entity.SetInvulnerable(0.2)
                gSounds['ghost_eat'].play()

        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT] or pressedKeys [pygame.K_RIGHT] or pressedKeys [pygame.K_UP] or pressedKeys [pygame.K_DOWN]:
            self.entity.ChangeState('ghost_walk')

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.entity.is_ghost = False
                    self.entity.ChangeState('idle')