from src.constants import *
from src.states.entity.EntityWalkState import EntityWalkState
from src.resources import *
import pygame

class PlayerGhostWalkState(EntityWalkState):
    def __init__(self, player, dungeon):
        super(PlayerGhostWalkState, self).__init__(player, dungeon)
        self.player = player
        self.dungeon = dungeon

    def Exit(self):
        pass

    def Enter(self, params):
        self.entity.offset_y = 2
        self.entity.offset_x = 8
        self.entity.ChangeAnimation("ghost_"+self.player.direction)
        self.player.is_ghost = True

    def update(self, dt, events):
        for entity in self.dungeon.current_room.entities:
            if entity.Collides(self.player) and not entity.invulnerable:
                entity.Damage(1)
                entity.SetInvulnerable(0.2)
                gSounds['ghost_eat'].play()
                
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT]:
            self.player.direction = 'left'
            self.player.ChangeAnimation("ghost_"+self.player.direction)
        elif pressedKeys[pygame.K_RIGHT]:
            self.player.direction = 'right'
            self.player.ChangeAnimation("ghost_"+self.player.direction)
        elif pressedKeys[pygame.K_DOWN]:
            self.player.direction = 'down'
            self.player.ChangeAnimation("ghost_"+self.player.direction)
        elif pressedKeys[pygame.K_UP]:
            self.player.direction = 'up'
            self.player.ChangeAnimation("ghost_"+self.player.direction)
        else:
            self.player.ChangeState('ghost_idle')  
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.entity.is_ghost = False
                    self.entity.ChangeState('idle')

        # move and bump to the wall check
        super().update(dt, events)

        #temporal move to the wall (bumping effect)
        if self.bumped:
            if self.entity.direction == 'left':
                self.entity.x = self.entity.x - PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.y + 12
                        self.dungeon.BeginShifting(-WIDTH, 0)

                self.entity.x = self.entity.x + PLAYER_WALK_SPEED * dt

            elif self.entity.direction == 'right':
                self.entity.x = self.entity.x + PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.y + 12
                        self.dungeon.BeginShifting(WIDTH, 0)

                self.entity.x = self.entity.x - PLAYER_WALK_SPEED * dt

            elif self.entity.direction == 'up':
                self.entity.y = self.entity.y - PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.x + 24
                        self.dungeon.BeginShifting(0,  -HEIGHT)

                self.entity.y = self.entity.y + PLAYER_WALK_SPEED * dt

            else:
                self.entity.y = self.entity.y + PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.x + 24
                        self.dungeon.BeginShifting(0,  HEIGHT)

                self.entity.y = self.entity.y - PLAYER_WALK_SPEED * dt